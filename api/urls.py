from django.urls import path

from .views import ListCloths, DetailView, UpdateView, DeleteView

urlpatterns = [
    path('cloth_list/',ListCloths.as_view(),name='list'),
    path('details/<int:pk>',DetailView.as_view(),name='details'),
    path('update/<int:pk>', UpdateView.as_view(), name='details'),
    path('delete/<int:pk>', DeleteView.as_view(), name='details'),
]