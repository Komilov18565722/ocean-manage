# urls.py for worker in accounts

from django.urls import path
from .views import WorkerListCreateView, WorkerRetrieveUpdateDestroyView, JobView

urlpatterns = [
    path('', WorkerListCreateView.as_view(), name='worker-list-create'),
    path('<uuid:id>/', WorkerRetrieveUpdateDestroyView.as_view(), name='worker-retrieve-update-destroy'),

    path('job-select-list/', JobView.as_view(), name='job-select-list'),
]

