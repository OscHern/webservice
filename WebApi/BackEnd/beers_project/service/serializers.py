from django.contrib.auth.models import User 
from rest_framework import serializers

from .models import Beer,  Kind, Selection,  User, UpTake

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class BeerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Beer
        fields = ['IdBeers','percentage','brand','name', 'type','detail' ]

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['Id','name','password','enable']

class KindSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kind
        fields = ['IdKind','name']

class SelectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Selection
        fields = ['IdBeer','IdUser','dateLog','id']


class UpTakeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = UpTake
        fields = ['Id','percentage','brand','name', 'type','cantida','username' ]

