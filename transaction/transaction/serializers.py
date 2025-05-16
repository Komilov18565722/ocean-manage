# serializers.py for Transaction in transaction

from django.utils import timezone

from rest_framework import serializers
from rest_framework.exceptions import ParseError

from accounts.models import User
from transaction.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'user', 'worker', 'price', 'type', 'status', 'created_by', 'created_at')
        read_only_fields = ('id', 'created_by', 'created_at')

    def to_representation(self, instance):
        res = super().to_representation(instance)
        if instance.worker:
            res['worker'] = {
                'id': instance.worker.id,
                'first_name': instance.worker.first_name,
                'last_name': instance.worker.last_name,
                'job_name': instance.worker.job.name,
            }

        if instance.user:
            res['user'] = {
                'id': instance.user.id,
                'first_name': instance.user.first_name,
                'last_name': instance.user.last_name,
            }

        if instance.created_by:
            res['created_by'] = {
                'id': instance.created_by.id,
                'first_name': instance.created_by.first_name,
                'last_name': instance.created_by.last_name,
            }
        return res
    
    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
    

class UserSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'job', 'phone_number')

    def to_representation(self, instance):
        res = super().to_representation(instance)
        if instance.job:
            res['job'] = {
                'id': instance.job.id,
                'name': instance.job.name,
            }
        return res


class TransactionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'user', 'worker', 'price', 'type', 'status', 'created_by', 'created_at')
        read_only_fields = ('id', 'user', 'worker', 'price', 'type', 'created_by', 'created_at')

    def to_representation(self, instance):
        res = super().to_representation(instance)
        return res

    def validate(self, attrs):
        return super().validate(attrs)

    def update(self, instance, validated_data):
        validated_data['updated_by'] = self.context['request'].user
        validated_data['updated_at'] = timezone.now()
        return super().update(instance, validated_data)

