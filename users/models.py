from django.db import models

class User_id(models.Model):
  id = models.CharField(max_length=7, primary_key=True)
  first_name = models.CharField(max_length=50)
  middle_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  def __str__(self):
      return f"{self.id} - {self.first_name} {self.last_name}"
  class Meta:
    ordering = ['-id']