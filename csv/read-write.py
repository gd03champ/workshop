import csv

with open("info.csv","w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["name","roll-num"])
    writer.writerow(["GD","7376211CS146"])
    csv_file.close()

with open("info.csv","r") as csv_file:

    reader = csv.reader(csv_file)

    next(reader) #to skip title

    for element in reader: print(element)