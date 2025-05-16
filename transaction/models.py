from django.db import models
from accounts.models import BaseData
# Create your models here.


class Transaction(BaseData):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name='transaction_user')
    worker = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name='transaction_worker')
    price = models.FloatField(default=0)
    type = models.CharField(max_length=20, default='cash', choices=(
        ('cash', 'Naqt'),
        ('transfer', 'Kartaga o`tkazma'),
        ('card', 'Karta'),
        ('bank', 'Bank')
    ))

    status = models.CharField(max_length=20, default='pending', choices=(
        ('archive', 'Xizmat korsatilgan'),
        ('pending', 'Navbatda'),
        ('cancelled', 'Bekor qilindi'),
    ))


