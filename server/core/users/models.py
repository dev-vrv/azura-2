from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    STATUS_CHOICES = (
        ('new', 'New'),
        ('active', 'Active'),
        ('blocked', 'Blocked'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    
    phone = models.CharField(max_length=15, blank=True, null=True)
    telegram = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'users'
        ordering = ('-created_at',)
        