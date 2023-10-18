from django.db import models

# Create your models here.
class Department(models.Model):
  name = models.CharField(max_length=200, verbose_name="department")   
  def __str__(self):
    return self.name

class Subject(models.Model):                        
  name = models.CharField(max_length=200, verbose_name="subject name")  
  abbrev = models.CharField(max_length=20, verbose_name="subject abbreviation")  
  dept = models.ForeignKey(Department, verbose_name="department", on_delete=models.CASCADE)
  def __str__(self):
    return self.abbrev

class Field(models.Model):
  name = models.CharField(max_length=200, verbose_name="field of study")  
  abbrev = models.CharField(max_length=50, verbose_name="field of study abbreviation", null=True) 
  dept = models.ForeignKey(Department, verbose_name="department", on_delete=models.CASCADE) 
  traininglevels = models.ManyToManyField("TrainingLevel", through="Degree")
  def __str__(self):
    return self.name

class SubField(models.Model):
  name = models.CharField(max_length=20, verbose_name="specialization name for field of study")
  abbrev = models.CharField(max_length=20, verbose_name="specialization abbreviation for field of study", null=True)
  field = models.ForeignKey(Field, verbose_name="field of study", on_delete=models.CASCADE)
  def __str__(self):
    return self.abbrev

class TrainingLevel(models.Model):
  name = models.CharField(max_length=200, verbose_name="training level name")   
  abbrev = models.CharField(max_length=20, verbose_name="training level abbreviation")   
  def __str__(self):
    return self.abbrev

class Degree(models.Model): 
  field = models.ForeignKey(Field, on_delete=models.CASCADE)
  traininglevel = models.ForeignKey(TrainingLevel, on_delete=models.CASCADE)
  code = models.IntegerField(verbose_name="degree code number")
  minhours = models.IntegerField(verbose_name="degree minimum hours required")
  field_minhours = models.IntegerField(verbose_name="field minimum hours required")
  field_maxhours = models.IntegerField(verbose_name="field maximum hours")
  def __str__(self):
    return "{} {}".format(self.traininglevel.__str__(), self.field.__str__())

class Requirement(models.Model):
  name = models.CharField(verbose_name="name of requirement domain", max_length=200)
  abbrev = models.CharField(verbose_name="abbreviation of requirement domain", max_length=20)
  totalhours = models.IntegerField(verbose_name="required domain total hours")
  def __str__(self):
    return self.name

class ReqType(models.Model):
  name = models.CharField(verbose_name="name of requirement domain-type", max_length=200)
  abbrev = models.CharField(verbose_name="abbreviation of requirement domain-type", null=True, max_length=20)
  totalhours = models.IntegerField(verbose_name="required domain type total hours")
  totalno_courses = models.IntegerField(verbose_name="total number of courses")
  req = models.ForeignKey(Requirement, on_delete=models.CASCADE) 
  courses = models.ManyToManyField("Course", through="ReqCourse")
  def __str__(self):
      return "{}: {}".format(self.req.__str__(), self.name)

class Course(models.Model):
  name = models.CharField(verbose_name="course name", max_length=200)          
  no = models.IntegerField(verbose_name="course number")
  hours = models.IntegerField(verbose_name="course hours")
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
  prereqs = models.ManyToManyField('Prereq', through='CoursePrereq')
  semesters = models.ManyToManyField("Semester", through="CourseSched")
  def __str_(self):
    return "{} {}".format(self.no, self.name)

    #doesn't work "{}_{}: {}".format(self.subject.__str__(), self.no, self.name)

class ReqCourse(models.Model):
  reqtype = models.ForeignKey(ReqType,on_delete=models.CASCADE)    
  course= models.ForeignKey(Course,on_delete=models.CASCADE)


class Semester(models.Model):
  FALL = "FAL"
  JANUARY = "JAN"
  SPRING = "SPR"
  MAY = "MAY"
  SUMMER1 = "SU1"
  SUMMER2 = "SU2"

  season_choices = [
    (FALL, "Fall"),
    (JANUARY, "January"),
    (SPRING, "Spring"),
    (MAY, "May"),
    (SUMMER1, "Summer1"),
    (SUMMER2, "Summer2")
  ]
  season = models.CharField(choices=season_choices, max_length=20)
  year = models.IntegerField(null=True, help_text="academic year")
  courses = models.ManyToManyField('Course', through='CourseSched')
  def __str__(self):
     return "{} {}".format(self.season, self.year)

class CourseSched(models.Model):
  semester = models.ForeignKey('Semester', on_delete=models.CASCADE)
  course = models.ForeignKey('Course', on_delete=models.CASCADE)


class Equiv(models.Model):
  transf_code = models.IntegerField(verbose_name="equivalent transfer course code")
  transf_name = models.CharField(max_length=200, verbose_name="equivalent transfer course name")
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  def __init__(self):
    return "{} {}".format(self.name, self.code)

class Prereq(models.Model):
  prereq_name = models.CharField(max_length=200, verbose_name="prerequisite course name")          
  prereq_no = models.IntegerField(verbose_name="prerequisite course number")
  prereq_hours = models.IntegerField(verbose_name="prerequisite course hours")
  def __init__(self):
    self.name

class CoursePrereq(models.Model):
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  prereq = models.ForeignKey(Prereq, verbose_name="prerequisite course", on_delete=models.CASCADE)