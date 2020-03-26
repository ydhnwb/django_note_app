from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('login', LoginViewSet, basename='login')
router.register('register', RegisterViewSet, basename='register')
router.register('category', CategoryViewSet, basename='category')
router.register('note', NoteViewSet, basename='note')

urlpatterns = [
    path('', include(router.urls))
]