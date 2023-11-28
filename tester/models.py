from django.db import models


class T1(models.Model):
  id = models.AutoField(primary_key=True)
  a = models.CharField(max_length=10, blank=True, null=True)
  b = models.CharField(max_length=10, blank=True, null=True)
  c = models.CharField(max_length=10, blank=True, null=True)
  displayfields = ["a", "b", "c"]
  search_fields = ["a", "b", "c"]
  class Meta:
    ordering = ['id']
  def __str__(self):
      return str(self.a)
  
class T2(models.Model):
  id = models.AutoField(primary_key=True)
  d = models.CharField(max_length=10, blank=True, null=True)
  e = models.ForeignKey("T1", verbose_name=("e from T1"), on_delete=models.CASCADE)
  displayfields = ["d", "e"]
  search_fields = ["d", "e"]
  def __str__(self):
      return str(self.d)
  

