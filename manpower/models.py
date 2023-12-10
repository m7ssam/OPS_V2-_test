from django.db import models
from project.models import Name
from simple_history.models import HistoricalRecords
from master.models import Department, Governorate
from dbview.models import DbView


class Job_type(models.Model):
    title = models.CharField(max_length=50, primary_key=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
      return self.title


class Title_list(models.Model):
    title = models.CharField(max_length=50, primary_key=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
      return self.title


class Contract(models.Model):
   contract = models.CharField(max_length=50, primary_key=True)
   description = models.TextField(null=True, blank=True)
   def __str__(self):
      return self.contract

class Code(models.Model):
    mp_code = models.CharField(max_length=7, primary_key=True)
    title = models.ForeignKey(Title_list, on_delete=models.CASCADE) 
    job = models.CharField(max_length=50)
    speciality = models.CharField(max_length=50, default="عام")
    dep = models.ForeignKey(Department,on_delete=models.CASCADE)
    c_calc = [
        ('direct', 'direct'),
        ('indirect', 'indirect'),
    ]
    calc = models.CharField(max_length=10, choices=c_calc)
    job_type = models.ForeignKey(Job_type,on_delete=models.CASCADE)
    displayfields = ['mp_code','title','job', 'speciality','dep']
    search_fields = ['mp_code','title','job', 'speciality']
    list_filter = ['title','job', 'speciality']
    def __str__(self):
      return self.mp_code

def upload_path(instance, filename):
    return f'mp/users/{instance.id}/{filename}'

class Mp_list(models.Model):
  id = models.CharField(max_length=8, primary_key=True)
  first_name = models.CharField(max_length=20, null=False, blank=False)
  middle_name = models.CharField(max_length=20, null=False, blank=False)
  last_name = models.CharField(max_length=20, null=False, blank=False)
  full_name = models.CharField(max_length=100, null=False, blank=False)
  code = models.ForeignKey(Code,on_delete=models.CASCADE)
  full_discription = models.TextField(null=True, blank=True)
  hire = models.DateField(auto_now=False, auto_now_add=False)
  birth = models.DateField(auto_now=False, auto_now_add=False)
  c_sex = [
        ('male', 'male'),
        ('female', 'female'),
  ]
  sex = models.CharField(max_length=10, choices=c_sex)
  contract = models.ForeignKey(Contract,on_delete=models.CASCADE)
  gov = models.ForeignKey(Governorate,on_delete=models.CASCADE)
  national_id = models.BigIntegerField()
  photo = models.ImageField(upload_to=upload_path, default="user.jpg")
  created = models.DateTimeField(auto_now_add=True) 
  update = models.DateTimeField(auto_now=True)
  history = HistoricalRecords()
  displayfields = ['id','first_name','last_name']
  search_fields = ['id','first_name','last_name']
  list_filter = []
  class Meta:
    ordering = ['id']
  def __str__(self):
      return f"{self.id} | {self.first_name}  {self.last_name}"

class Mp_Location(models.Model):
    id = models.CharField(max_length=7, primary_key=True)
    recipient = models.ForeignKey( Name, on_delete=models.CASCADE)
    def __str__(self):
      return f"{self.id} | {self.recipient}"

class Mp_history(models.Model):
    transaction = models.AutoField(primary_key=True)
    id = models.CharField(max_length=7)
    recipient = models.ForeignKey( Name, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
      return f"{self.transaction} | {self.id} | {self.recipient}"
    


