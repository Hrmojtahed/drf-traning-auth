from django.urls import path,include
from .views import TestApiView, HelloViewSet, ProfileViewSet
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register('hello-viewset',HelloViewSet,basename='hello-viewset')
routers.register('profile',ProfileViewSet)



urlpatterns = [
    path('hello/',TestApiView.as_view()),
    path('',include(routers.urls)),
]