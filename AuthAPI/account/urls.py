from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.UserRegistration.as_view(), name="register"),
    path("login/", views.UserLogin.as_view(), name="login"),
    path("profile/", views.UserProfile.as_view(), name='profile'),
    path("changepassword/", views.UserChangePassword.as_view(), name='change_password'),
    path("send-reset-password/", views.SendPasswordResetEmail.as_view(), name='send-reset-password'),
    path("reset-password/<uid>/<token>/", views.UserPasswordReset.as_view(), name='reset-password'),
]