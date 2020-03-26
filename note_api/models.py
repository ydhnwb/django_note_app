from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin



class UserAccountManager(BaseUserManager):
    def create_user(self,email, name, password = None):
        if not email:
            raise ValueError("User must have an email address")

        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")

        email = self.normalize_email(email)
        user = self.model(email = email, name = name)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, name, password):
        email = self.normalize_email(email)
        user = self.model(email = email, name = name)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    password = models.CharField(max_length=255, validators=[MinLengthValidator(8)])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def __str__(self):
        return "{0} - {1}".format(self.name, self.email)


class Category(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=255, blank=True, null=False)
    description = models.TextField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='note')
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.title