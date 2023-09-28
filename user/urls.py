from django.urls import path
from .views import UserRegistratinView

urlpatterns = [
path('register/', UserRegistratinView.as_view(), name="user-registration"),


]