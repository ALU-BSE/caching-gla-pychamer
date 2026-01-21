from django.shortcuts import render
from rest_framework import viewsets

from users.models import User
from users.serializers import UserSerializer

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(cache_page(60 * 5), name="list")  # cache list endpoint is going to be 5 minutes
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
