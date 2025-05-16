# serializers.py for auth in accounts
import uuid

from django.utils import timezone

from rest_framework import serializers
from rest_framework.exceptions import ParseError

from accounts.models import User, Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'name')

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'job', 'password', 'first_name', 'last_name', 'phone_number', 'status')
        read_only_fields = ('id', 'status')

    def to_representation(self, instance):
        res = super().to_representation(instance)
        if instance.job:
            res['job'] = {
                'id': instance.job.id,
                'name': instance.job.name,
            }
        res.pop('password', None)
        return res

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        validated_data['username'] = f"user_{uuid.uuid4()}"
        validated_data['type'] = 'worker'
        worker = super().create(validated_data)
        worker.set_password(validated_data.get('password', ''))
        worker.save()
        return worker


class ManagerUpdateSerializer(serializers.ModelSerializer):
    class Meta: # noqa
        model = User
        fields = ('id', 'email', 'job', 'first_name', 'last_name', 'phone_number', 'status')
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

