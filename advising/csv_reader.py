import csv
def read_csv(filename):
  try:
    with open(filename, newline='') as csv_file:
      csv_reader = csv.reader(csv_file)
      for record in csv_reader:
        print(record)
  except (IOError, OSError) as file_read_error:
    print("Unable to open the csv file. Exception:{}".format(file_read_error))
  if __name__ == '__main__':
    read_csv('csv_file.csv')
  

  def write_csv(filename, header, data):
    try:
      with open(filename, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)
        csv_writer.writerows(data)
    except (IOError, OSError) as csv_file_error:
        print("Unable to write the contents to csv file. Exception:{}".format(csv_file_error))
