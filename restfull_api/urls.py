from django.urls import path, re_path, include
from .import views
from .views import HelloApiView

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view(), name='hello-view'),
]