from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from register.models import Register
from rest_api.serializers import RegisterModelSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegisteModelViewSet(ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 
    