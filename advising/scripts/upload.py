from advising.models import Course, Program, ProgramCourses
import csv

def run():
  with open('media/course.csv') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
      print(row)
      program, _ = Program.objects.get_or_create(name=row[-1])
      course = Course(subj_abbrev=row[0], no=row[1], name=row[3], hours=row[4], program=row[5])
      course.save()




  """
    courseupload= io.TextIOWrapper(request.FILES['coursefile'].file)
    try:
      with open(filename, newline='') as csv_file:     #try with resources, then closes automatically
          course_dict = csv.DictReader(csv_file)     #reads file, converts into Dict
          course_list = list(course_dict)
          for record in csv_reader:
              print(record)
    except (IOError, OSError) as file_read_error:       #doesn't show stack trace/methods called to user
      print("Unable to open the csv file. Exception:{}".format(file_read_error))
    if __name__ == '__main__':
        read_csv('course.csv')


        """