from django.urls import path, re_path, include
from .import views
from .views import HelloApiView,home
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile',views.UserProfileViewSet)

urlpatterns = [

    path('home',home.as_view(),name='home'),

    path('hello-view/', views.HelloApiView.as_view(), name='hello-view'),
    path('', include(router.urls)),
]