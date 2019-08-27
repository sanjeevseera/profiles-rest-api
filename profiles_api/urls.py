from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('hello-viewset', views.HellowViewSet, base_name='hello-viewset')
urlpatterns = [
    path('hello_view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]