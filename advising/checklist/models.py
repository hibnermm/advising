from django.db import models

# Create your models here.

class Subject(models.Model):
  subject_abbrev = models.CharField(max_length=20, verbose_name="subject abbreviation", null=True)
  subject_name = models.CharField(max_length=200)
  def __str__(self):
    return self.subject_abbrev

class Course(models.Model):
  course_number = models.IntegerField()
  course_name = models.CharField(max_length=500)
  credit_hours = models.IntegerField()
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
  def __str__(self):
    return self.course_name


class Student(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  phone = models.IntegerField()         #need to reformat this
  email = models.EmailField()
  school_id = models.CharField(blank=True, max_length=20)
  course = models.ManyToManyField('Course', through='StudentCourses')
  def __str__(self):
    return f"{self.first_name} {self.last_name}"

class StudentCourses(models.Model):
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  course_status = models.BooleanField(verbose_name="course completed?", null=False)

"""is the StudentCourses table necessary, should course_status be elsewhere


?Different ways to think about or hints for.....?
should prerequisites and transfer credits be separate tables?
Does it need intermediary tables if M2M but no additional info?   

Model COURSE: MGT4339    =   Model PREREQ  MGT1302 || MKT1403

Model COURSE: ENGL1028    =   Model TRANSFER: AP ENG || HERT103   

"""