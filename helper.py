import os
import sys

def create_d_funk(app_name, func_name):
    # Asosiy app katalogini yaratish
    app_path = os.path.join(os.getcwd(), app_name)
    if not os.path.exists(app_path):
        os.makedirs(app_path)

    # Ichida funksiya katalogini yaratish
    func_path = os.path.join(app_path, func_name)
    if not os.path.exists(func_path):
        os.makedirs(func_path)

    # Kerakli fayllarni yaratish
    files = ['serializers.py', 'views.py', 'urls.py']
    for file in files:
        file_path = os.path.join(func_path, file)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                if file == 'views.py':
                    file_code = f"""
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from {app_name}.models import {func_name}

from notify.views import CustomPagination

from .serializers import {func_name}Serializer, {func_name}UpdateSerializer

class {func_name}ListCreateView(generics.ListCreateAPIView):
    '''
        Errors list:
            '400' : "your_error",
    '''
    serializer_class = {func_name}Serializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        request_user = self.request.user

        queryset = {func_name}.objects.filter(state = 1)
        
        return queryset


class {func_name}RetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = {func_name}UpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404({func_name}, pk=self.kwargs.get('id', None), state = 1)
    
    def destroy(self, request, *args, **kwargs):
        object = self.get_object()
        object.state = 0
        object.save()
        return Response('Successfully deleted', status=status.HTTP_204_NO_CONTENT)

"""
                elif file == 'serializers.py':
                    file_code = f"""
from django.utils import timezone

from rest_framework import serializers
from rest_framework.exceptions import ParseError

from {app_name}.models import {func_name}


class {func_name}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {func_name}
        fields = ('id', )
        read_only_fields = ('id', )

    def to_representation(self, instance):
        res = super().to_representation(instance)
        return res
    
    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
    

class {func_name}UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = {func_name}
        fields = ('id', )
        read_only_fields = ('id', )
    
    def to_representation(self, instance):
        res = super().to_representation(instance)
        return res
    
    def validate(self, attrs):
        return super().validate(attrs)
    
    def update(self, instance, validated_data):
        validated_data['updated_by'] = self.context['request'].user
        validated_data['updated_at'] = timezone.now()
        return super().update(instance, validated_data)
"""
                elif file == 'urls.py':
                    file_code = f"""
from django.urls import path
from .views import {func_name}ListCreateView, {func_name}RetrieveUpdateDestroyView

urlpatterns = [
    path('', {func_name}ListCreateView.as_view(), name='{func_name}list-create'),
    path('<uuid:id>/', {func_name}RetrieveUpdateDestroyView.as_view(), name='{func_name}retrieve-update-destroy'),
]
"""
                f.write(f"# {file} for {func_name} in {app_name}\n{file_code}\n")

    print(f"'{func_name}' function folder and required files created inside '{app_name}' app.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_d_funk.py <app_name> <func_name>")
    else:
        create_d_funk(sys.argv[1], sys.argv[2])
