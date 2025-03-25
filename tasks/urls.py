from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r"rest",TaskViewSet)



urlpatterns = [

]+router.urls
