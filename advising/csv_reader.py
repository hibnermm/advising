import io, csv


def CourseUpload(request):
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


