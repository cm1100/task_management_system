from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from accounts.models import CustomUser
from accounts.serializers import UserSerializer
# Create your views here.



class UserViewSet(ModelViewSet):

    permission_classes=[AllowAny]
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer
    http_method_names = ['post','get']



    def get_queryset(self):
        
        queryset= super().get_queryset()
        if self.request.GET.get("email"):
            queryset=queryset.filter(email=self.request.GET.get("email"))
        return queryset


