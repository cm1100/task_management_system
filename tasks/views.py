from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.



class TaskViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=Task.objects.all()
    serializer_class=TaskSerializer


    def get_queryset(self):

        queryset = super().get_queryset()

        if self.request.GET.get('user_id'):
            queryset = queryset.filter(assigned_users=self.request.GET.get('user_id'))
        

        return queryset


