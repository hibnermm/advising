from django.db import models


# Create your models here.


class Program(models.Model):

  level_abbrev = models.CharField(max_length=20, verbose_name="Degree level")   

  major = models.CharField(max_length=200, verbose_name="Major")  

  major_abbrev = models.CharField(max_length=20, verbose_name="Major abbreviation") 

  specialization = models.CharField(max_length=200, verbose_name="Specialization", blank=True)  

  spec_abbrev = models.CharField(max_length=20, verbose_name="Specialization abbreviation", blank=True) 

  def __str__(self):

      return "{}: {}".format(self.level_abbrev, self.major)
  


class Course(models.Model):

  subj_abbrev = models.CharField(verbose_name="Subject abbreviation", max_length=200)          

  no = models.IntegerField(verbose_name="Course number")

  name = models.CharField(verbose_name="Course name", max_length=200)   

  hours = models.IntegerField(verbose_name="Course credit hours")

  programs = models.ManyToManyField('Program', through='ProgramCourses')

  #file_name = models.CharField(max_length=100)

  #file = models.FileField(upload_to='courses/')

  def __str__(self):

    return "{} {}: {}".format(self.subj_abbrev, self.no, self.name)


class ProgramCourses(models.Model):

  programs = models.ForeignKey(Program, on_delete=models.CASCADE)

  courses = models.ForeignKey(Course, on_delete=models.CASCADE)

  is_core = models.BooleanField(verbose_name="Core requirement?", null=True)

  is_degree = models.BooleanField(verbose_name="Degree requirement", null=True)

  is_major = models.BooleanField(verbose_name="Major requirement?", null=True)

  semester = models.IntegerField(verbose_name="Semester code")

  def __str__(self):

    return "{} {}: {} {}".format(self.programs.level_abbrev, self.programs.major_abbrev, self.courses.subj_abbrev, self.courses.no)

  class Meta:

     verbose_name_plural = "Program Courses"
