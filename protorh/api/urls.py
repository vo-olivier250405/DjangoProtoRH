from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserView.as_view()),
    path('users/<int:id>/', views.UserView.as_view()),
    path('users/create/', views.UserView.as_view())
]
