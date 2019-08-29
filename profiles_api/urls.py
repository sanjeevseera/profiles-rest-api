from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('hello-viewset', views.HellowViewSet, base_name='hello-viewset')
router.register('profiles', views.UserProfileViewSet)

urlpatterns = [
    path('hello_view/', views.HelloApiView.as_view()),
    path('login', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]