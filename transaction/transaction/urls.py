# urls.py for Transaction in transaction

from django.urls import path
from .views import TransactionListCreateView, UserSelectView, TransactionRetrieveUpdateDestroyView

urlpatterns = [
    path('', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('<uuid:id>/', TransactionRetrieveUpdateDestroyView.as_view(), name='transaction-retrieve-update'),
    path('user-select-list/', UserSelectView.as_view(), name='user-select-list'),

]