from rest_framework import serializers
from .models import Product, Student

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 

class SchoolSerializer(serializers.Serializer):
    name = serializers.CharField()
    branch = serializers.CharField()

    def create():
        pass

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()