
from django.urls import path
from rest_framework.routers import DefaultRouter
from accounts.views import UserViewSet

router = DefaultRouter()
router.register(r"user/rest",UserViewSet)

urlpatterns = [



]+router.urls
