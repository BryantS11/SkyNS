from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save # Object is saved
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.


class NameServiceModel(models.Model):
    class Meta:
        verbose_name = ("SiaNS")
        verbose_name_plural = ("SiaNS")
        ordering = ['id']

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ns")
    name = models.CharField(max_length=46, unique=True)
    skylink = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} by: {self.user.username}'

class PortalModel(models.Model):
    class Meta:
        verbose_name = ("Portal")
        verbose_name_plural = ("Portals")
    
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class UserPortalModel(models.Model):
    class Meta:
        verbose_name = ("User Portal")
        verbose_name_plural = ("User Portal")
    
    user =  models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_portal")
    portal = models.ForeignKey(PortalModel, on_delete=models.CASCADE, related_name="portal", help_text="Select Default Portal")

    def __str__(self):
        return f"{self.user.username}'s Default Portal"

# Signals

@receiver(post_save, sender=User) # When Signal from user is received
def default_portal(sender, instance, created, **kwargs):
    if created: # If new User created
        try:
            user_portal = UserPortalModel.objects.create(user=instance, portal=PortalModel.objects.get(name="Siasky"))
            user_portal.save()
        except ObjectDoesNotExist:
            portal = PortalModel.objects.create(name="Siasky", url="https://siasky.net/")
            portal.save()
            user_portal = UserPortalModel.objects.create(user=instance, portal=portal)
            user_portal.save()
