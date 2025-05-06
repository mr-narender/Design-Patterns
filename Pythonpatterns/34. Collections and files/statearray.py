"""Read file into array"""

DATAFILE="stateNames.txt"

with open(DATAFILE, "r") as f:
    statenames = [sname.rstrip() for sname in f]
print(statenames[:3])
print(len(statenames))

with open(DATAFILE, "r") as f:
    statenames = [sname.rstrip() for sname in f]

print(statenames[:4])
print(len(statenames))

f = open(DATAFILE, "r") # open the file
statenames=[]
statenames = f.readlines()
print(statenames[:3])
print(len(statenames))