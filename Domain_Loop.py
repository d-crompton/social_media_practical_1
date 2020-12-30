# This program is used to store the domains that trackers communicate with and how many different trackers
# communicate with that domain. An sub-domains are removed, only the top-level domain is counted
import csv

input_file = "tracker_output.csv"
domains = []  # Array to store domain name and how many times it appears
with open(input_file, "r") as file:
    csv_reader = csv.reader(file, delimiter=',')
    # Loop through each row in the CSV file
    curr_row = 0
    for row in csv_reader:
        if curr_row != 0:  # Miss first line as its headers
            # Retrieving domain from address
            domain_parts = row[2].split('.')  # Split the domain into parts
            # print(domain_parts)
            # Use the minus index as there are hosts with 3 and 4 parts
            try:  # Included try state as "blank" value causes crash
                adj_domain = domain_parts[-2] + "." + domain_parts[-1]  # Adjusted domain
            except IndexError:
                adj_domain = "Not available"
            # print(adj_domain)
            # Loop through "domains" array to see if domain is already stored, if not append, if so add to count
            domain_exists = False
            # If domains is empty, add first entry
            if len(domains) == 0:
                domains.append([adj_domain, 1])
            elif len(domains) > 0:
                for domain in domains:
                    if domain[0] == adj_domain:
                        domain[1] += 1
                        domain_exists = True
                        break  # Exit loop as no longer needed to loop
                # Add domain to array after loop, if domain_exists is false
                if not domain_exists:
                    domains.append([adj_domain, 1])
        # Move to next row
        curr_row += 1
# After tracker file has been looped through, save results to another file
with open("domain_frequency.csv", "w+") as output_file:
    output_file.write("Domain,Number of Trackers\n")
    for d in domains:
        output_file.write(f"%s,%s\n" % (d[0], d[1]))
