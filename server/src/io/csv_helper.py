"""IO functions to help with csv files."""
import csv

def readcsv(csv_file_path):
    """Reads a CSV file and returns the contents as a 2D list."""
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        csv_data_list = [row for row in reader]
    return csv_data_list

#Write a csv data list to a file.
def writecsv(csv_data_list, csv_file_path):
    """Writes a 2D csv data list to the given path."""
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_data_list)
    return
