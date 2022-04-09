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


class Travel(models.Model):
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=False, blank=False)
    date_of_departure = models.DateField(null=False, blank=False)
    date_of_return = models.DateField(null=False, blank=False)
    people = models.IntegerField(null=False, blank=False)
    type = models.CharField(max_length=15, null=False, blank=False)
    price = models.FloatField(null=True, blank=True, default=0)
    description = models.TextField

    def __str__(self):
        return self.name
