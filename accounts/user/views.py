# views.py for auth in accounts

from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from accounts.models import User

from accounts.permission import IsManager

from .serializers import UserSerializer, UserUpdateSerializer

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class UserListCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsManager]
    pagination_class = CustomPagination

    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'last_name', 'gender', 'phone_number']

    def get_queryset(self):
        queryset = User.objects.filter(type = 'user', state = 1)
        return queryset


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsManager]

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs.get('id', None), type='user', state = 1)

