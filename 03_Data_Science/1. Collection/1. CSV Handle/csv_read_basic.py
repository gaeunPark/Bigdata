import csv

with open('Demographic_Statistics_By_Zip_Code.csv', newline='') as infile:
    data = list(csv.reader(infile))

countParticipantsIndex = data[0].index("COUNT PARTICIPANTS")
print("The index of 'COUNT PARTICIPANTS': " + str(countParticipantsIndex))

countParticipantsIndex = []

for row in data[1:]:
    countParticipantsIndex.append(row[countParticipantsIndex])

print("<COUNT PARTICIPANT>")
for participant in countParticipantsIndex:
    print(participant)


