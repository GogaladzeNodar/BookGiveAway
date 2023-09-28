from django.urls import path
from .views import UserRegistratinView, UserLoginView, UserLogoutView

urlpatterns = [
path('register/', UserRegistratinView.as_view(), name="user-registration"),
path('login/', UserLoginView.as_view(), name="user-login"),
path("logout/", UserLogoutView.as_view(), name="user-logout"),
]