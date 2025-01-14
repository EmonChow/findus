from django.db import models
from django.db.models.fields import BigAutoField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField

from PIL import Image

class Permission(models.Model):
     name = models.CharField(max_length=255, unique=True)

     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
     updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)

     class Meta:
          ordering = ('name',)

     def __str__(self):
          return self.name
     
     def save(self, *args, **kwargs):
          self.name = self.name.replace(' ', '_').upper()
          super().save(*args, **kwargs)



class Role(models.Model):
     name = models.CharField(max_length=255, unique=True)
     permissions = models.ManyToManyField(Permission, blank=True)

     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)

     updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
     
     class Meta:
          ordering = ('name',)

     def __str__(self):
          return self.name
     
     def save(self, *args, **kwargs):
          self.name = self.name.replace(' ', '_').upper()
          super().save(*args, **kwargs)




class UserManager(BaseUserManager):
     def create_user(self, first_name, last_name, email, gender,username=None, password=None):
          """
          Creates and saves a User with the given email, date of
          birth and password.
          """
          if not email:
               raise ValueError('Users must have an email address')

          user = self.model(
               first_name= first_name,
               last_name = last_name,
               email=self.normalize_email(email),
               gender = gender,
               username = username
          )

          user.set_password(password)
          user.save(using=self._db)
          return user

     def create_superuser(self, first_name, last_name, email, gender,username=None ,password=None):
          """
          Creates and saves a superuser with the given email, date of
          birth and password.
          """
          user = self.create_user(
               email=self.normalize_email(email),
               password=password,
               first_name= first_name,
               last_name = last_name,
               gender = gender,
               username = username
          )
          user.is_admin = True
          user.save(using=self._db)
          return user
     
 



class User(AbstractBaseUser):
     class Gender(models.TextChoices):
          MALE = 'male', _('Male')
          FEMALE = 'female', _('Female')
          OTHERS = 'others', _('Others')

     first_name = models.CharField(max_length=100,null=True, blank=True)
     last_name = models.CharField(max_length=100, null=True, blank=True)
    
     username = models.CharField(max_length=100, null=True, blank=True, unique=True)
     email = models.EmailField(verbose_name='email address', max_length=255, null=True, blank=True, unique=True)

     gender = models.CharField(max_length=6, choices=Gender.choices, default=Gender.MALE, null=True, blank=True)

     user_type = models.CharField(max_length=255, null=True, blank=True)

     date_of_birth = models.DateField(null=True, blank=True)

     is_active = models.BooleanField(default=True)
     is_admin = models.BooleanField(default=False)

     role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
 
     primary_phone = PhoneNumberField(null=True, blank=True, unique=True)
     secondary_phone = PhoneNumberField(null=True, blank=True, unique=True)
     image = models.ImageField(upload_to="authentication/User/", null=True, blank=True)


     created_at = models.DateTimeField(auto_now_add=True, null=True,  blank=True)
     updated_at = models.DateTimeField(auto_now=True, null=True,  blank=True)
     deleted_at = models.DateTimeField(auto_now=True, null=True,  blank=True)

     created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
     updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)

     objects = UserManager()

     USERNAME_FIELD = 'username'
     REQUIRED_FIELDS = ['first_name', 'last_name', 'gender', 'email']

     class Meta:
          ordering = ('-id',)

     def __str__(self):
          return self.username or ''


     def has_perm(self, perm, obj=None):
          "Does the user have a specific permission?"
          # Simplest possible answer: Yes, always
          return True

     def has_module_perms(self, app_label):
          "Does the user have permissions to view the app `app_label`?"
          # Simplest possible answer: Yes, always
          return True

     @property
     def is_staff(self):
          "Is the user a member of staff?"
          # Simplest possible answer: All admins are staff
          return self.is_admin



class LoginHistory(models.Model):
     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)

     ip_address = models.CharField(max_length=255, null=True, blank=True)
     mac_address = models.CharField(max_length=255, null=True, blank=True)
     g_location_info = models.CharField(max_length=500, null=True, blank=True)
     is_device_blocked = models.BooleanField(default=False)

     login_time = models.DateTimeField(null=True, blank=True)
     logout_time = models.DateTimeField(null=True, blank=True)

     status = models.CharField(max_length=255, null=True, blank=True)

     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
     updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)

     class Meta:
          verbose_name_plural = 'LoginHistories'
          ordering = ('-id',)

     def __str__(self):
          return self.user.username if self.user else self.user



class ActivityLog(models.Model):
     # activity_type = models.ForeignKey(Permission, on_delete=models.PROTECT, related_name='permission_activitylogs')
     activity_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='user_activitylogs', null=True)
     comment = models.CharField(max_length=500, null=True, blank=True)

     created_at = models.DateTimeField(auto_now_add=True)

     class Meta:
          verbose_name_plural = 'ActivityLogs'
          ordering = ('-id',)

     def __str__(self):
          return self.activity_by.username


