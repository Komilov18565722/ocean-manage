from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.response import Response

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
import os, json
from drf_yasg.generators import OpenAPISchemaGenerator


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title="TradePro-app",
        default_version="v1",
        description="TradePro",
        contact=openapi.Contact(email="komilov185657@gmail.com"),
        license=openapi.License(name="NOT License"),
    ),
    public=True,
    generator_class=BothHttpAndHttpsSchemaGenerator,
    permission_classes=[permissions.AllowAny]
    
)

urlpatterns = [
    
    path('admin/', admin.site.urls),



    # Auth
    path('api/v1/auth/', include('accounts.auth.urls'),  name = 'auth'),



    # User
    path('api/v1/user/', include('accounts.user.urls')),




    # Worker
    path('api/v1/worker/', include('accounts.worker.urls')),





    # Transaction
    path('api/v1/transaction/', include('transaction.transaction.urls')),





    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
