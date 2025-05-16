from rest_framework_simplejwt.views import  TokenRefreshView

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import  status
from rest_framework.exceptions import ParseError
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import  User

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.contrib.auth import authenticate
from django.db.models import Q

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token), # noqa
        "user_id": str(user.id),
        "type": user.type
    }


@swagger_auto_schema(
    method="post",
    operation_description="Check if the provided OTP is valid for a user.",
    manual_parameters=[
        openapi.Parameter(
            "username",
            openapi.IN_QUERY,
            description="Phone number or email",
            type=openapi.TYPE_STRING,
            required=True
        ),
        openapi.Parameter(
            "password",
            openapi.IN_QUERY,
            description="password",
            type=openapi.TYPE_STRING,
            required=True
        )
    ]
)
@api_view(["POST"])
def login_view(request):
    username = request.query_params.get("username", None).lower()
    password = request.query_params.get("password", None)

    if not username or not password:
        return Response({"detail": "username_and_password_are_required"}, status=status.HTTP_400_BAD_REQUEST)

    user_obj = User.objects.filter(Q(email__iexact=username) | Q(phone_number=username))
    if not user_obj.exists():

        raise ParseError('user_not_found')
    else:
        user_obj = user_obj.first()

    user_name = user_obj.username
    user = authenticate(request, username=user_name, password=password)
    if not user:
        return Response({"detail": "invalid_username_or_password"}, status=status.HTTP_400_BAD_REQUEST)

    elif '@' in username and user_obj.type == 'user':
        raise ParseError('this_user_dont_verify')

    if user is not None:
        tokens = get_tokens_for_user(user)
        return Response(tokens, status=status.HTTP_200_OK)
    else:
        return Response({"detail": "invalid_username_or_password"}, status=status.HTTP_400_BAD_REQUEST)