from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, BaseUserManager
from rest_framework.authtoken.models import Token
# Create your models here.

class UserManager(BaseUserManager):

    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    choices = (
        ('MR', 'Mr'),
        ('MRS', 'Mrs'),
        ('DR', 'Dr'),
        ('MISS', 'Miss'),
        ('PROF', 'Prof'),
    )
    username = None
    email = models.EmailField(max_length=100, unique=True)
    user_id = models.CharField(max_length=50, unique=True)
    title = models.CharField(choices=choices, max_length=255)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    mosque = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='profile/', blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_youth=models.BooleanField(default=False)
    is_adult=models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ['-created_at']
    
    objects = UserManager()
    
    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = self._generate_user_id()
        super().save(*args, **kwargs)
        
    def _generate_user_id(self):
        user_id = User.objects.order_by('id').last()
        new_id = 1 if not user_id else user_id.id + 1
        return f'ID{new_id:04d}'
    
    # EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'address', 'mosque',]

    def __str__(self):
        return self.email
        
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Youth(models.Model):
    user=models.OneToOneField(User, related_name="youth", on_delete=models.CASCADE)
    def __str__(self):
        return self.user.email



class Adult(models.Model):
    user=models.OneToOneField(User, related_name="adult", on_delete=models.CASCADE)
    def __str__(self):
        return self.user.email