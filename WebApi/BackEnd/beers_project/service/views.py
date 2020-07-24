from django.shortcuts import render

from rest_framework import viewsets

from .serializers import BeerSerializer, UsersSerializer, KindSerializer, SelectionSerializer, UpTakeSerializer
from .models import Beer,  Kind, Selection,  User, UpTake

class BeerViewSet(viewsets.ModelViewSet):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

class KindViewSet(viewsets.ModelViewSet):
    queryset = Kind.objects.all()
    serializer_class = KindSerializer

class SelectionViewSet(viewsets.ModelViewSet):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer

class UpTakeViewSet(viewsets.ModelViewSet):
    queryset = UpTake.objects.all()
    serializer_class = UpTakeSerializer