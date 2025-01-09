from django.urls import path, re_path, include
from rest_framework.authtoken.views import ObtainAuthToken

from .import views
from .views import HelloApiView,home
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewSet', views.HelloViewSet, basename='hello-viewSet')
router.register('profile',views.UserProfileViewSet)
router.register('login', views.LoginViewSet, basename='login')


urlpatterns = [

    path(' login/', ObtainAuthToken.as_view(), name='login'),

    path('home',home.as_view(),name='home'),

    path('hello-view/', views.HelloApiView.as_view(), name='hello-view'),
    path('', include(router.urls)),
]