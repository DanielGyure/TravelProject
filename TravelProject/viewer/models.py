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
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Travel(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    date_of_departure = models.DateField()
    date_of_return = models.DateField()
    people = models.IntegerField()
    type = models.CharField(max_length=15)
    price = models.FloatField(default=0)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
