from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class NameServiceModel(models.Model):
    class Meta:
        verbose_name = "SiaNS Model"
        ordering = ['id']

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ns")
    name = models.CharField(max_length=46, unique=True)
    skylink = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} by: {self.user.username}'
