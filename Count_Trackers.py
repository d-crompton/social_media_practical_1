# This program counts how many trackers appear in each application
# This program's output is a list of application package names and the amount of trackers found in them
import os
import csv

directory = ".\\CSV Files"  # Relative directory where files are stored
apps = []  # Storing each app and the number of trackers
# Loop through each file in the CSV directory
for csv_file in os.scandir(directory):
    # Open the file to read
    with open(csv_file) as file:
        file_name = file.name.split('\\')[2]  # Taking name from the file path
        file_name = file_name[:-4]  # Removing '.csv' from the end
        csv_reader = csv.reader(file, delimiter=',')
        row_count = 0  # Number of rows = trackers minus headers
        # Loop through rows
        for row in csv_reader:
            row_count += 1  # Add one to row count
        row_count -= 1  # Take one off for the header row, the rest are trackers
    apps.append([file_name, row_count])  # Add App Name and the Count to the array
# After looping through the files
# Writing found counts to a CSV file
with open("tracker_counts.csv", "w+") as output_file:
    output_file.write("Package Name, Tracker Count\n")
    for a in apps:
        output_file.write(f"%s,%s\n" % (a[0], a[1]))
