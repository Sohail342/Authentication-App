from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from account.renderers import UserRenderers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializers import(
    UserRegistrationSerializer, 
    UserLoginSerializer, 
    UserProfilSerializer, 
    UserChangePasswordSerializer, 
    SendPasswordResetEmailSerializer,
    UserPasswordResetSerializer
    )

# Creating tokens(JWT) manually 
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistration(APIView):

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token':token, "msg": "Registration Successful"}, status=status.HTTP_201_CREATED)
    
class UserLogin(APIView):
    renderer_classes = [UserRenderers]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token':token, "msg":"Login Successful"}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':['Email or Password is not Valid']}, status=status.HTTP_401_UNAUTHORIZED)


class UserProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfilSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class UserChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':"Password Changed Successfully"}, status=status.HTTP_200_OK)


class SendPasswordResetEmail(APIView):
    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg':"Password Reset Link send. Please check your Email"},status=status.HTTP_200_OK)


class UserPasswordReset(APIView):
    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':"Password Reset Successfully"},status=status.HTTP_200_OK)