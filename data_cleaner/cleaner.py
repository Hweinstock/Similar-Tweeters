from zip_to_dict import prepare_file
import os, csv
from tqdm import tqdm


fields = ["filepath", "author"]
rows = []

files = os.listdir("../data/pre_data/")
print("Cleaning Data...")
for file in tqdm(files[:25]):
    next_file = prepare_file(file)
    if next_file is not None:
        rows.append(prepare_file(file))

with open("../outline.csv", 'w') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(fields)
    csv_writer.writerows(rows)

