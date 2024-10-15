from rest_framework import serializers
from .models import Employee, PhoneNumber
from django.contrib.auth.models import User

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberSerializer()

    class Meta:
        model = Employee
        fields = '__all__'

    # To handle nested phone number creation
    def create(self, validated_data):
        phone_data = validated_data.pop('phone_number')
        phone = PhoneNumber.objects.create(**phone_data)
        employee = Employee.objects.create(phone_number=phone, **validated_data)
        return employee
    
    def update(self, instance, validated_data):
        phone_number_data = validated_data.pop('phone_number', None)
        
        # Update the Employee fields
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.save()

        # Update or create the phone number if provided
        if phone_number_data:
            phone_number = instance.phone_number
            phone_number.number = phone_number_data.get('number', phone_number.number)
            phone_number.save()

        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user