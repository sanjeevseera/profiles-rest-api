from django.urls import path
from . import views

urlpatterns = [
    path('hello_view/', views.HelloApiView.as_view()),
]