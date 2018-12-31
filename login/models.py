from django.db import models

from django.db.models.signals import post_delete, post_init, post_migrate, post_save
from django.db.models.signals import pre_delete, pre_init, pre_migrate, pre_save

from django.dispatch import receiver

from django.conf import settings
import os

# Create your models here.

class Profiles(models.Model):
    name = models.CharField(max_length = 20)

    address = models.TextField()

    status = models.BooleanField(
        default = True,
    )
    age     = models.IntegerField(
        default=0,
    )
    fathersname = models.CharField(
        max_length = 20,
        default = "",
    )
    photo = models.FileField(
        default = " ",
        upload_to   = 'upload',
    )

    @property
    def is_qulify(self, *args, **kwargs):
        return True if self.age > 18 else False

    def __str__(self, *args, **kwargs):
        return self.name

class ProfilesBank(models.Model):

    profile = models.ForeignKey(
        'login.Profiles',
        on_delete   = models.CASCADE,
        related_name= "banks",
        null = True,
    )
    details = models.TextField()

    def __str__(self, *args, **kwargs):
        return self.details

@receiver(post_save, sender = Profiles)
def postsavefun(instance, *args, **kwargs):
    print ("in this ")

@receiver(pre_save, sender = Profiles)
def presavefun(instance, *args, **kwargs):
    print ("in this pre")


