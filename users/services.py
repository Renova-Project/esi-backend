import datetime
import jwt
from django.conf import settings
from .models import User

def create_user(user) -> "User":
    instance = User(
        first_name=user["first_name"],
        last_name=user["last_name"],
        email=user["email"]
    )

    if user["password"] is not None:
        instance.set_password(user['password'])

    instance.save()

    return instance


def user_email_selector(email: str) -> "User":
    user = User.objects.filter(email=email).first()

    return user


def create_token(user_id: int) -> str:
    payload = dict(
        id=user_id,
        exp=datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        iat=datetime.datetime.utcnow()
    )
    
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm='HS256')

    return token