from django.db import models

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=50, primary_key=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
      return self.department
    

class Governorate(models.Model):
    gov = models.CharField(max_length=50, primary_key=True)
    area = models.IntegerField(null=True, blank=True)
    population = models.IntegerField(null=True, blank=True)
    main_city = models.CharField(max_length=50, null=True, blank=True)
    cities = models.IntegerField(null=True, blank=True)
    centers = models.IntegerField(null=True, blank=True)
    neighborhoods = models.IntegerField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    discription = models.TextField(null=True, blank=True)
    displayfields = ['gov','area','population', 'main_city','cities','centers','centers']
    def __str__(self):
      return self.gov