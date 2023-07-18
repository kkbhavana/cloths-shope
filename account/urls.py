from django.urls import path

from .views import Register, MyTokenObtainPairView

urlpatterns = [
    path('register/',Register.as_view(),name='register'),
    path('login/',MyTokenObtainPairView.as_view(),name='login'),
]