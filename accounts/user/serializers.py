# serializers.py for auth in accounts
import uuid

from django.utils import timezone

from rest_framework import serializers
from rest_framework.exceptions import ParseError

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'gender', 'birthday', 'status')
        read_only_fields = ('id', 'status')

    def to_representation(self, instance):
        res = super().to_representation(instance)
        return res
    
    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        validated_data['username'] = f"user_{uuid.uuid4()}"
        validated_data['type'] = 'user'
        return super().create(validated_data)
    

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'birthday',  'gender', )
        read_only_fields = ('id', 'status')

    def to_representation(self, instance):
        res = super().to_representation(instance)
        return res

    def validate(self, attrs):
        return super().validate(attrs)

    def update(self, instance, validated_data):
        validated_data['updated_by'] = self.context['request'].user
        validated_data['updated_at'] = timezone.now()
        return super().update(instance, validated_data)

