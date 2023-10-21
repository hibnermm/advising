from django.db import models


# Create your models here.
class Degree(models.Model):
  level = models.CharField(max_length=200, verbose_name="Degree level")
  level_abbrev = models.CharField(max_length=20, verbose_name="Degree level abbreviation")   
  major = models.CharField(max_length=200, verbose_name="Major")  
  major_abbrev = models.CharField(max_length=20, verbose_name="Major abbreviation") 
  specialization = models.CharField(max_length=200, verbose_name="Specialization", blank=True)  
  spec_abbrev = models.CharField(max_length=20, verbose_name="Specialization abbreviation", blank=True) 
  def __str__(self):
      return "{}: {}".format(self.level_abbrev, self.major)


class Requirement(models.Model):
  req = models.CharField(verbose_name="Requirement", max_length=200)
  req_abbrev = models.CharField(verbose_name="Requirement abbrevation", max_length=20)
  reqtype = models.CharField(verbose_name="Requirement type", max_length=200, blank=True)
  reqtype_abbrev = models.CharField(verbose_name="Requirement type abbrevation/code", max_length=20, blank=True)
  degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
  def __str__(self):
    return "{}  {}".format(self.req, self.reqtype)


class Course(models.Model):
  subj_abbrev = models.CharField(verbose_name="Subject abbreviation", max_length=200)          
  no = models.IntegerField(verbose_name="Course number")
  name = models.CharField(verbose_name="Course name", max_length=200)   
  hours = models.IntegerField(verbose_name="Course credit hours")
  reqs = models.ManyToManyField('Requirement', verbose_name="Requirement", through='ProgramCourses')
  def __str__(self):
    return "{} {}: {}".format(self.subj_abbrev, self.no, self.name)

class ProgramCourses(models.Model):
  reqs = models.ForeignKey(Requirement, verbose_name = "Requirements",on_delete=models.CASCADE)    
  courses = models.ForeignKey(Course, on_delete=models.CASCADE)
  completed = models.BooleanField(verbose_name="Course completion status", null=True)
  def __str__(self):
    return "{} - {}".format(self.reqs, self.courses)


class Prerequisite(models.Model):
  subj_abbrev = models.CharField(verbose_name="subject abbreviation", max_length=200)          
  no = models.IntegerField(verbose_name="Course number")
  name = models.CharField(verbose_name="Course name", max_length=200)   
  hours = models.IntegerField(verbose_name="Course credit hours")
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  def __str__(self):
    return "{} {}: {}".format(self.subj_abbrev, self.no, self.name)

