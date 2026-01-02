import csv

with open("../csv/employees.csv", newline="") as f:
    reader = csv.reader(f)
    rows = list(reader)


# NOTE: This assumes first_name is column 1 and last_name is column 2.
names = [row[1] + " " + row[2] for row in rows[1:]]
print(names)

names_with_e = [name for name in names if "e" in name.lower()]
print(names_with_e)
