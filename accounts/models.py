from operator import setitem

from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.core.files.base import ContentFile
from datetime import datetime
import base64

from data.translator import translate_json

USER_TYPES = (
    ('manager', 'Boshqaruvchi'),
    ('worker', 'Ishchi'),
    ('user', 'Foydalanuvchi'),
)

class BaseData(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    created_by = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='%(class)s_creator', null=True)
    updated_by = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='%(class)s_renewer', null=True)

    state = models.SmallIntegerField(default=1)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class Job(BaseData):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class User(AbstractUser, BaseData):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)

    email = models.EmailField(null=True, blank=True, unique=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)

    type = models.CharField(max_length=255, default='user', choices=USER_TYPES)
    gender = models.CharField(max_length=255, default='male', choices=(('male', 'Male'), ('female', 'Female')))
    status = models.BooleanField(blank=True, null=True, default=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True)

    birthday = models.DateField(null=False, blank=False, default=datetime(2004, 12, 31).date())

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-created_at']