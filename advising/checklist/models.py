
from django.db import models
# Create your models here.
class College(models.Model):
  college_name = models.CharField(max_length=200)
  def __str__(self):
    return self.college_name
  
class Department(models.Model):
  dept_name = models.CharField(max_length=200, verbose_name="department")   
  college = models.ForeignKey(College, on_delete=models.CASCADE)
  def __str__(self):
    return self.dept_name

class Degree(models.Model):
  degree_name = models.CharField(max_length=200)   
  degree_abbrev = models.CharField(max_length=20, verbose_name="degree abbreviation")   
  college = models.ForeignKey(College, on_delete=models.CASCADE)
  field = models.ManyToManyField("Field", verbose_name="Field of Study", through="DegreeField")
  def __str__(self):
    return self.degree_name

class Field(models.Model):
  field_name = models.CharField(max_length=50, verbose_name="field of study")  
  field_abbrev = models.CharField(max_length=50, verbose_name="field of study abbreviation") 
  department = models.ForeignKey(Department, on_delete=models.CASCADE) 
  def __str__(self):
    return self.field_name

class DegreeField(models.Model):
  degree = models.ForeignKey(Degree, on_delete=models.CASCADE) 
  field = models.ForeignKey(Field, verbose_name="field of study", on_delete=models.CASCADE) 
  degreefieldno = models.IntegerField(verbose_name="degree field of study number")
  degree_minhours = models.IntegerField(verbose_name="degree minimum hours required")
  field_minhours = models.IntegerField(verbose_name="field of study minimum hours required")
  field_maxhours = models.IntegerField(verbose_name="field of study maximum hours")

