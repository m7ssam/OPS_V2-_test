from django.db import models

# Create your models here.

class Name(models.Model):
  recipient = models.CharField(max_length=6, primary_key=True)
  project_name = models.CharField(max_length=50)
  photo = models.ImageField(upload_to = f'project/%Y/%m/%d/', default = "default.jpg")
  def __str__(self):
      return f"{self.recipient} | {self.project_name}"

