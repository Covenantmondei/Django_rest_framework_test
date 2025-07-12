from rest_framework import serializers
from .models import Product, Student, School

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

    def create(self, validated_data):
        return School.objects.create(**validated_data)



class StudentSerializer(serializers.Serializer):
    name = serializers.CharField

    def create(self, validated_data):
        school = self.context['school']
        school = School.objects.get(id=school)
        return Student.objects.create(school_id=school , **validated_data)