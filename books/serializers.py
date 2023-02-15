from rest_framework import serializers
from books.models import ebook
from django.contrib.auth.models import User




class booksserializer(serializers.ModelSerializer):
   class Meta:
        model = ebook
        fields = ('id','title','author','genre','review','favourite') 
       
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  '__all__'
        