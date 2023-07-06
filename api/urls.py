from django.urls import path

from .views import ListCloths,DetailView

urlpatterns = [
    path('cloth_list/',ListCloths.as_view(),name='list'),
    path('details/<int:pk>',DetailView.as_view(),name='details'),
]