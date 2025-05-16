# views.py for Transaction in transaction

from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from accounts.models import User
from accounts.permission import IsManager
from transaction.models import Transaction

from accounts.user.views import CustomPagination

from .serializers import TransactionSerializer, UserSelectSerializer, TransactionUpdateSerializer


class UserSelectView(generics.ListAPIView):
    serializer_class = UserSelectSerializer
    permission_classes = [IsManager]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='role',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='role',
                required=True,
                enum=['worker', 'user',],
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        request_user = self.request.user
        _role = self.request.GET.get('role', None)
        queryset = User.objects.filter(type=_role, state = 1)  # noqa

        return queryset  # noqa


class TransactionListCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='status',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Transaction status',
                required=True,
                enum=['all', 'pending', 'archive', 'canceled'],
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        request_user = self.request.user
        _status = self.request.GET.get('status', 'all')
        if request_user.type == 'manager':
            queryset = Transaction.objects.filter(state = 1) # noqa
        elif request_user.type == 'worker':
            queryset = Transaction.objects.filter(worker__job = request_user.job, state = 1) # noqa
        if _status != 'all':
            queryset = queryset.filter(status = _status) # noqa

        return queryset # noqa


class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Transaction, pk=self.kwargs.get('id', None), state = 1)

    def destroy(self, request, *args, **kwargs):
        object = self.get_object()
        object.state = 0
        object.save()
        return Response('Successfully deleted', status=204)


