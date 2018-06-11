from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps django work with custom User model"""

    def create_user(self, email, name, password):
        """ Create new user profile object """

        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """Create a new super user object"""

        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """User profile inside system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserProfileManager()

    USERNAME_FIELD = 'email' # Field user will use to login
    REQUIRED_FIELDS = ['name']

    # helper functions
    def get_full_name(self):
        """To get users full name"""

        return self.name

    def get_short_name(self):
        """ To get users last name"""

        return self.name

    def __str__(self):
        """Django uses this to convert obj to string"""

        return self.email
