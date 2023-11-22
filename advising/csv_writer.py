import csv
def write_csv(filename, header, data):
   try:
    with open(filename, 'w') as csv_file:
      csv_writer = csv.writer(csv_file)
      csv_writer.writerow(header)
      csv_writer.writerows(data)
   except (IOError, OSError) as csv_file_error:
    print("Unable to write the contents to csv file. Exception:{}".format(csv_file_error))
