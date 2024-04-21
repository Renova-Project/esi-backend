from rest_framework import authentication, exceptions
from rest_framework.permissions import BasePermission
import jwt
from django.conf import settings

from .models import User


class UserAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get("jwt")

        if not token:
            return None

        try:
            payload = jwt.decode(
                token, settings.JWT_SECRET, algorithms=['HS256'])
        except:
            raise exceptions.AuthenticationFailed('Unauthorized')

        utilisateur = User.objects.filter(id=payload['id']).first()

        return (utilisateur, None)


class IsUser(BasePermission):
    def has_permission(self, request, view):
        try:
            user = request.user
            return bool(user and user.is_authenticated)
        except:
            return False


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        try:
            user = request.user
            user_type = user.type
        except:
            return False
        return bool(user and user_type == "ADMIN")


class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        try:
            user = request.user
            user_type = user.type
        except:
            return False
        return bool(user and user_type == "SUPER_ADMIN")
