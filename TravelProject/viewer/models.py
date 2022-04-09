from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=10)
    code = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name



