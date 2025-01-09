from django.urls import path, re_path, include
from .import views
from .views import HelloApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile',views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view(), name='hello-view'),
    path('', include(router.urls)),
]