from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db.models.signals import post_delete, pre_delete, post_save, pre_save
from django.db.models.signals import post_migrate, pre_migrate, post_init, pre_init

from django.dispatch import receiver

from django.utils.safestring import mark_safe

import datetime

# Create your models here.

# Fields which are common
# null = Default False
# blank = Default False
# verbose_name = No Default
# default = need to set
# validators = no default

class UserProfile(models.Model):
    fullname = models.CharField(
        max_length=30, # This is must
        # null=True,
        # blank=True,
    )
    active = models.BooleanField(
        default=True,
    )
    added_on = models.DateTimeField(
        auto_now_add=True,
    )
    lastupdate = models.DateTimeField(
        auto_now=True,
    )

    birthdate = models.DateField()

    login_time = models.TimeField()

    balance = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default = 0.0,
        validators = [
            MinValueValidator(0)
        ]
    )

    tax = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default = 0.0,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(100),
        ]
    )

    logincount = models.IntegerField(
        default=0,
    )

    email = models.EmailField()

    gender = models.CharField(
        max_length = 2,
        choices = (
            ("M", "Male"),
            ("F", "Female"),
        ),
        default="M",
    )

    @property
    def age(self, *args, **kwargs):
        return datetime.datetime.now().date() - self.birthdate

    @property
    def gotoGoogle(self, *args, **kwargs):
        return mark_safe("""<a href="https://google.com" target="_blank"> Go to Google </a>""")
    def __str__(self, *args, **kwargs):
        return self.fullname

class Address(models.Model):
    address = models.TextField()

    profile = models.ForeignKey(
        'profiles.UserProfile',
        on_delete = models.CASCADE,
        related_name="address",
    )

class Relation(models.Model):
    to_rel = models.ForeignKey(
        'profiles.UserProfile',
        on_delete = models.CASCADE,
        related_name="relation_with",
    )
    from_rel = models.ForeignKey(
        'profiles.UserProfile',
        on_delete = models.CASCADE,
        related_name="my_relation",
    )
    relationdd = models.CharField(
        max_length = 2,
        choices = (
            ("MO", "Mother"),
            ("FA", "Father"),
            ("SI", "Sister"),
            ("BR", "Brother"),
            ("DA", "Daughter"),
            ("SO", "Son"),
        )
    )

reverse_relation = {
    "FA" : { "M": "SO", "F":"DA"},
    "MO" : { "M": "SO", "F":"DA"},
    "SI" : { "M": "BR", "F": "SI" },
    "BR" : { "M": "BR", "F": "SI" },
    "DA" : { "M": "FA", "F": "MO"},
    "SO" : { "M": "FA", "F": "MO"},
}

@receiver(post_save, sender=Relation)
@receiver(post_save, sender=UserProfile)
def demoPostSave(sender, instance, *args, **kwargs):
    print ("IN POST SAVE THROUGH : " + str(sender))

@receiver(post_save, sender=Relation)
def CreateReverseRelation(sender, instance, *args, **kwargs):
    # kwargs['created'] = True
    print ("IN THIS ")
    if kwargs['created']:
        print ("2")
        try: 
            Relation.objects.get(
                to_rel = instance.from_rel,
                from_rel = instance.to_rel,
                relation = reverse_relation[instance.relation][instance.from_rel.gender],
            )
        except models.ObjectDoesNotExist as e:
            Relation.objects.create(
                from_rel = instance.to_rel,
                to_rel = instance.from_rel,
                relation = reverse_relation[instance.relation][instance.from_rel.gender]
            )