from rest_framework import serializers
from .models import User
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .utils import Util

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', 'terms_conditions']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # Validating password and confirm password while registration
    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password don't match")
        return data

    # Override the create method to handle password and password2
    def create(self, validated_data):
        # Remove password2 from the validated data
        validated_data.pop('password2')
        
        # Create the user with the remaining data
        user = User.objects.create_user(**validated_data)
        
        return user
    
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200)
    class Meta:
        model = User
        fields = ['email', 'password']


class UserProfilSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200)
    class Meta:
        model = User
        fields = ['id', 'email', 'name']

class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=250, style={'input_type':'password'}, write_only=True)
    password2 = serializers.CharField(max_length=250, style={'input_type':'password'}, write_only=True)
    class Meta:
        fields = ['password', 'password2']
        
    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        user = self.context.get('user')

        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password don't match")
        user.set_password(password)
        user.save()
        return data
    
class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=280)
    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            user_id = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user=user)
            link = 'http://127.0.0.1:8000/api/user/reset-password/'+user_id+'/'+token+'/'


            # Send mail
            body = 'Click the following link to reset your password \n'+link
            data = {
                'email_subject':'Reset Your Password',
                'body':body,
                'to_mail':user.email
            }
            Util.send_mail(data=data)
            return attrs
        else:
            raise serializers.ValidationError("You are not a registered User")

class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=250, style={'input_type':'password'}, write_only=True)
    password2 = serializers.CharField(max_length=250, style={'input_type':'password'}, write_only=True)
    class Meta:
        fields = ['password', 'password2']
        
    def validate(self, data):
        try:
            password = data.get('password')
            password2 = data.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')

            if password != password2:
                raise serializers.ValidationError("Password and Confirm Password don't match")
            
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError("Token is not valid or Expired")
            user.set_password(password)
            user.save()
            return data
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)
            raise serializers.ValidationError('Token is not valid or Expired')


    
        