import csv
def write_csv(filename, header, data):
   try:
    with open(filename, 'w') as csv_file:
      csv_writer = csv.writer(csv_file)
      csv_writer.writerow(header)
      csv_writer.writerows(data)
      csv_file.close()
   except (IOError, OSError) as csv_file_error:
    print("Unable to write the contents to csv file. Exception:{}".format(csv_file_error))
if __name__ == '__main__':
  header = ['subj_abbrev', 'no', 'name', 'hours']
  data = [['BIOL', 1607, 'Botany II', 3], ['ENGL', 2201, 'Thematic Analysis', 3]]
  filename = 'media/csvfiles/course_output2.csv'
  write_csv(filename, header, data)  

https://pypi.org/project/django-export-csv/
https://docs.djangoproject.com/en/4.2/howto/outputting-csv/
https://pypi.org/project/django-csv-export-view/