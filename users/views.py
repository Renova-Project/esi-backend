from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView
from rest_framework import status

from .serializers import UserSerializer
from . import services
from . import authentication


# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         data = serializer.validated_data

#         serializer.instance = services.create_user(user=data)

#         return Response(data=serializer.data)
    
class RegisterView(CreateAPIView):
    serializer_class=UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LoginView(APIView):
    def post(self, request):
        try:
            email = request.data["email"]
            password = request.data["password"]
        except:
            raise AuthenticationFailed("Please enter email and password")

        user = services.user_email_selector(email=email)

        if user is None:
            raise AuthenticationFailed("Invalid credentials")

        if not user.check_password(raw_password=password):
            raise AuthenticationFailed("Invalid password")
        
        instance = UserSerializer(user)
        token = services.create_token(user_id=user.id)

        res = Response(data=instance.data)
        res.set_cookie(key="jwt", value=token, httponly=True)

        return res


class UserView(APIView):
    authentication_classes = [authentication.UserAuthentication]
    permission_classes = [authentication.IsUser]

    def get(self, request):
        user = request.user

        serializer = UserSerializer(user)

        return Response(serializer.data)


class LogoutView(APIView):
    authentication_classes = [authentication.UserAuthentication]
    permission_classes = [authentication.IsUser]

    def post(self, request):
        res = Response()
        res.delete_cookie('jwt')
        res.data = {'message': 'Disconnected successfuly'}

        return res
