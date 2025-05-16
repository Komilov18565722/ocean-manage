# urls.py for auth in accounts

from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('<uuid:id>/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
]
