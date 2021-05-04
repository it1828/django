from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.urls import reverse

# Create your models here.

def poster_path(instance, filename):
    return "bands/"+ str(instance.id) + "/poster/"+ filename

class Band(models.Model):
    band_name = models.CharField(max_length=40, verbose_name="Band name")
    genre = models.CharField(max_length=50, verbose_name="Genre")
    est_date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.",verbose_name="Establishing date")
    about = models.TextField(blank=True, null=True, verbose_name="About", max_length=500)
    poster = models.ImageField(upload_to=poster_path, blank=True, null=True, verbose_name="Poster")

    class Meta:
        ordering = ["band_name"]

    def __str__(self):
        return self.band_name





class Person(models.Model):
    last_name = models.CharField(max_length=30, verbose_name="Last name")
    first_name = models.CharField(max_length=45, verbose_name="First name")
    birthdate = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.",verbose_name="Birthdate")
    biography = models.TextField(blank=True, null=True, verbose_name="Biography", max_length=500)

    class Meta:
        ordering = ["last_name"]

    def __str__(self):
        return self.first_name  + ' ' + self.last_name


class Member(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    person_name = models.ForeignKey(Person, on_delete=models.CASCADE)
    instrument = models.CharField(max_length=30, verbose_name="Instrument")
    member_since = models.DateField(verbose_name="Member since", help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    member_to = models.DateField(blank=True, null=True, verbose_name="*Member to", help_text="Please use the following format: <em>YYYY-MM-DD</em>.")

    class Meta:
        ordering = ["instrument"]

    def __str__(self):
        return self.instrument











