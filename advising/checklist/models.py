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
  fields = models.ManyToManyField("Field", verbose_name="Field of Study", through="DegreeField", null=True)
  def __str__(self):
    return self.degree_name

class Field(models.Model):
  field_name = models.CharField(max_length=200, verbose_name="field of study")  
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
  def __str__(self):
    return"{}_{}".format(self.degree.__str__(), self.field.__str())


class Requirement(models.Model):
  req_domain_name = models.CharField(verbose_name="name of required domain", max_length=200)
  req_domain_abbrev = models.CharField(verbose_name="abbreviation of required domain", max_length=20)
  types = models.ManyToManyField('Type', through="ReqType")

class Type(models.Model):
  type_name = models.CharField(verbose_name="name of required domain type", max_length=200)
  type_abbrev = models.CharField(verbose_name="abbreviation of requirement type", max_length=20, )

class ReqType(models.Model):
  req = models.ForeignKey(Requirement, verbose_name=" required domain", on_delete=models.CASCADE)
  type = models.ForeignKey(Type, verbose_name=" required domain type", null=True, on_delete=models.CASCADE) 

class DegreeFieldReq(models.Model):
  req_totalhours = models.IntegerField(verbose_name="required domain total hours")
  type_totalhours = models.IntegerField(verbose_name="required domain type total hours")
  degreefield = models.ForeignKey(DegreeField,on_delete=models.CASCADE)
  courses = models.ManyToManyField('Course', through="ReqCourses")
  reqtype = models.ForeignKey(ReqType, on_delete=models.CASCADE)

                                        


class Subject(models.Model):                        
  subj_name = models.CharField(max_length=200, verbose_name="subject name")  
  subj_abbrev = models.CharField(max_length=20, verbose_name="subject abbreviation")  
  department = models.ForeignKey(Department, on_delete=models.CASCADE)
  def __str__(self):
    return self.subject_abbrev

class Course(models.Model):
  course_name = models.CharField(max_length=200)          
  course_no = models.IntegerField(verbose_name="course number")
  course_hours = models.IntegerField(verbose_name="course hours")
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
  department = models.ForeignKey(Department, on_delete=models.CASCADE)
  def __str_(self):
    return "{} {}: {}".format(self.subj_abbrev.__str__(), self.course_no.__str__(), self.course_name.__str__())


class ReqCourses(models.Model):
  total_courses = models.IntegerField(verbose_name="total number of courses required")
  course_required = models.BooleanField(null=False, verbose_name="is course required?")
  degreefieldreq = models.ForeignKey(DegreeFieldReq,on_delete=models.CASCADE)
  course = models.ForeignKey(Course,on_delete=models.CASCADE)


class Equiv(models.Model):
  equiv_transfcode = models.IntegerField(verbose_name="equivalent transfer course code")
  equiv_transfname = models.CharField(max_length=200, verbose_name="equivalent transfer course name")
  course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Prereq(models.Model):
  prereq_name = models.CharField(max_length=200, verbose_name="prerequisite course name")          
  prereq_no = models.IntegerField(verbose_name="prerequisite course number")
  prereq_hours = models.IntegerField(verbose_name="prerequisite course hours")


class CoursePrereq(models.Model):
  equiv = models.ForeignKey(Equiv, verbose_name="equivalent transfer course", max_length=200, on_delete=models.CASCADE)
  prereq = models.ForeignKey(Prereq, verbose_name="prerequisite course", max_length=200, on_delete=models.CASCADE)


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
  season_name = models.CharField(choices=season_choices, max_length=20)
  courses = models.ManyToManyField("Course", verbose_name="Field of Study", through="CourseSched")

class CourseSched(models.Model):
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
  yearstart = models.IntegerField(null=True, help_text="start year of course")


"""

ERRORS:
checklist.DegreeField: (fields.E336) The model is used as an intermediate model by 'checklist.Semester.courses', but it does not have a foreign key to 'Semester' or 'Course'.
"""


  
  
