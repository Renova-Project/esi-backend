from django.contrib.auth import models as auth_models
from django.utils.translation import gettext_lazy as _
from django.db import models


class UserManager(auth_models.BaseUserManager):
    def create_user(self, first_name: str, last_name: str, email: str, password: str, type: str = "USER", is_staff=False, is_superuser=False, is_active=True) -> "User":
        if not email:
            raise ValueError('user must have an email')
        if not first_name:
            raise ValueError('user must have a first name')
        if not last_name:
            raise ValueError('user must have a last name')

        user = self.model(email=self.normalize_email(email))

        user.first_name = first_name
        user.last_name = last_name
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.type = type
        user.is_active = is_active

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, first_name: str, last_name: str, email: str, password: str, type="SUPER_ADMIN") -> "User":
        self.create_user(
            first_name, last_name, email, password, type, is_staff=True, is_superuser=True)


class UserType(models.TextChoices):
    STUDENT = "STUDENT", _("Student")
    TEACHER = "TEACHER", _("Teacher")
    ADMIN = "ADMIN", _("Admin")
    SUPER_ADMIN = "SUPER_ADMIN", _("Super admin")
    STUDIES_DIRECTION = "STUDIES_DIRECTION", _("Studies direction")
    ALUMNI = "ALUMNI", _("Alumni")
    PARTNER = "PARTNER", _("Partner")


class User(auth_models.AbstractUser):
    email = models.EmailField(blank=False, max_length=255, unique=True)
    password = models.CharField(default='', max_length=255)
    type = models.CharField(
        max_length=63,
        choices=UserType
    )
    username = None
    last_login = None

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        db_table = 'users'
