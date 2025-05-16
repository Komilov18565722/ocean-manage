# views.py for auth in accounts

from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from accounts.models import User, Job

from accounts.permission import IsManager

from .serializers import ManagerSerializer, ManagerUpdateSerializer, JobSerializer


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class WorkerListCreateView(generics.ListCreateAPIView):
    serializer_class = ManagerSerializer
    permission_classes = [IsManager]
    pagination_class = CustomPagination

    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'email', 'job__name',  'last_name', 'gender', 'phone_number']

    def get_queryset(self):
        queryset = User.objects.filter(type = 'worker', state = 1)
        return queryset


class WorkerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ManagerUpdateSerializer
    permission_classes = [IsManager]

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs.get('id', None), type='worker', state = 1)



class JobView(generics.ListAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all() # noqa
