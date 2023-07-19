from django.urls import path

from .views import Register, MyTokenObtainPairView, VerifyUser

urlpatterns = [
    path('register/',Register.as_view(),name='register'),
    path('login/',MyTokenObtainPairView.as_view(),name='login'),
    path('verifyuser/', VerifyUser.as_view(), name='verify'),

]