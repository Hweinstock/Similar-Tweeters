from zip_to_dict import prepare_file
import os, csv


fields = ["filepath", "author"]
rows = []

files = os.listdir("../data/pre_data/")

for file in files[:100]:
    rows.append(prepare_file(file))

with open("data.csv", 'w') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(fields)
    csv_writer.writerows(rows)

