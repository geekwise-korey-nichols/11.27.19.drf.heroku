from django.contrib.auth.models import User, Group
from .serializers import User_Serializer, Group_Serializer
from rest_framework import viewsets

class User_Viewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_Serializer

class Group_Viewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = Group_Serializer