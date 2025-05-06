import csv
from csv import reader

nm = [
    ['Fred', 'Farkel', '1245 Bridge St', 'Bridgeport', 'CT'],
    ['Sam', "O'Kelley", '42 Secret Lane', 'Mystic', 'CT'],
    ["Sarah", 'Smythe', '205 Frazzle Rd, Apt B', 'Fairfield', 'CT'],
]

#create header text
header=['frname', 'lname', 'address', 'town', 'state']

# create csv file with header
with open ('namehlist.csv', 'w', newline='') as csvfile:
    addWriter = csv.writer(csvfile)
    addWriter.writerow(header)  #write out header row
    # write out other rows
    for row in nm:
        addWriter.writerow(row)


# now read it back in
# first look for a header row
sniffer = csv.Sniffer()
hasHead = sniffer.has_header(
    open('namehlist.csv').read(1024))

# now read in the entire file
with open ('namehlist.csv', newline='') as csvfile:
    addReader = csv.reader(csvfile)
    rows = list(addReader)
    headRow = rows.pop(0) if hasHead else []
    print(headRow)
