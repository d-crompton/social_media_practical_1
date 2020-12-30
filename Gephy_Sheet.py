# Script used to put together App names, tracker domains and the companies they go to
import os
import csv

# File Paths for Necessary Files
csv_files_dir = ".\\CSV Files"
app_name_path = "..\\App Names.csv"
dom_freq_path = "..\\domain_frequency.csv"

# Arrays of edges to be used later as Gephi Adjacency Lists
app_tracker_edges = []
unique_trackers = [] # Used to avoid repeats in the tracker_company array
tracker_company_edges = []

# Assigning App Names to found Tracker Domains (using the top 2 levels or whole IP)
for csv_file in os.scandir(csv_files_dir):  # Iterate through each App's TrackerControl File
    with open(csv_file) as app_tracker_file:
        tracker_csv = csv.reader(app_tracker_file, delimiter=',')
        # Retrieving File / Package Name
        file_name = app_tracker_file.name.split('\\')[2]  # Taking the name from the file path
        package_name = file_name[:-4]  # Removing '.csv' from the end
        # Opening App Name file to retrieve App's Name using its Package Name
        app_name = None  # Assigning now to use outside file opening below
        with open(app_name_path) as app_name_file:
            name_csv = csv.reader(app_name_file, delimiter=',')
            for row in name_csv:
                if row[0] == package_name:
                    app_name = row[1]
                    break
        # Iterate through the Game's CSV file for Trackers
        curr_row = 0
        for row in tracker_csv:
            if curr_row != 0:  # Avoid Headers
                # Getting Tracker domain
                domain_parts = row[0].split('.')  # Divide domain address into levels
                if not domain_parts[0] == "blank":  # Avoid random 'blank' addresses
                    # Check if IP is used instead of domain name - the top level will contain no letters
                    if domain_parts[0].isdigit():
                        tracker_domain = row[0]
                    elif not domain_parts[0].isdigit():
                        tracker_domain = domain_parts[-2] + "." + domain_parts[-1]
                # Add App Name and Tracker Domain to edge array
                app_tracker_edges.append([app_name, tracker_domain])
                # Checking if Tracker Domain isn't already in Unique Trackers list for use later
            curr_row += 1
    # Each CSV File closes here
# Assign Tracker Domains to Company Names for 2nd Edge Array
with open(dom_freq_path) as dom_file:
    dom_csv = csv.reader(dom_file, delimiter=',')
    # Iterate through saved Unique Trackers to find their Company
    curr_row = 0
    for row in dom_csv:
        if curr_row != 0:
            tracker_company_edges.append([row[0], row[2]])
        curr_row += 1
print(tracker_company_edges)

# Write these arrays to an Adjacency List for Gephi
with open("gephy_sheet_v2.csv", "w+") as output:
    # Writing the App -> Tracker Edges
    for edge in app_tracker_edges:
        output.write(f"%s,%s\n" % (edge[0], edge[1]))
    # Writing the Tracker -> Company Edge
    for edge in tracker_company_edges:
        output.write(f"%s,%s\n" % (edge[0], edge[1]))
