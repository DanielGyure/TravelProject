from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=10)
    code = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    cover = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.name


class Travel(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    date_of_departure = models.DateField()
    date_of_return = models.DateField()
    people = models.IntegerField()
    price = models.FloatField(default=0)
    description = models.TextField(null=True, blank=True)
    cover = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    country = models.CharField(max_length=20, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Booking(models.Model):
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE, null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.travel.name + ' - ' + self.profile.user.username