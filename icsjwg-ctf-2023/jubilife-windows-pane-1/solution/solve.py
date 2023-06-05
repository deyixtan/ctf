import csv
from operator import itemgetter

csv_file =  open('../attachments/LogonEvents.csv', 'r')
csv_reader = csv.reader(csv_file)

users = {}
for row in csv_reader:
    username = row[6]
    if username == "Username":
        continue
    if username not in users:
        users[username] = []
    users[username].append(row)
    users[username] = sorted(users[username], key=itemgetter(0))

for username, log_entries in users.items():
    loggedin = False
    for log_entry in log_entries:
        log_type = log_entry[1]
        if log_type == "4624":
            if loggedin:
                # print(log_entries)
                print(username)
                break
            else:
                loggedin = True
        elif log_type == "4634":
            if not loggedin:
                # print(log_entries)
                print(username)
                break
            else:
                loggedin = False
 