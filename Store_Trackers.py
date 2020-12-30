# This program is used to store each tracker individually that appears in each of the apps
# The output stores the tracker name and category provided by TC Lite and the domain is contacts
import os
import csv

directory = ".\\CSV Files"  # Relative directory where files are stored
trackers = []  # Used for storing found trackers
# Loop through each file in the CSV directory
for csv_file in os.scandir(directory):
    # Open the file to read
    with open(csv_file) as file:
        csv_reader = csv.reader(file, delimiter=',')
        curr_line = 0
        # Loop through rows
        for row in csv_reader:
            if curr_line != 0:  # Ignore first line as that has column headers
                host_address = row[0]
                # Check if host address is already added to existing trackers list, if so do not add again
                tracker_present = False
                for t in trackers:
                    if host_address in t:
                        tracker_present = True
                        break  # Exit loop as no more iteration needed
                if not tracker_present:  # If tracker_present exits the loop as true, skip this
                    # row[2] = tracker name, row[3] = tracker category
                    trackers.append([row[2], row[3], host_address])
            curr_line += 1
# After looping through files
# Writing found trackers to an output file for later use
with open("tracker_output.csv", "w+") as output_file:  # opening a new output file in write mode
    output_file.write("Tracker Name,Tracker Category,Host Address\n")
    for t in trackers:
        output_file.write(f"%s,%s,%s\n" % (t[0], t[1], t[2]))  # Writes the tracker name, category and host
