from zip_to_dict import prepare_file
import os, csv
from tqdm import tqdm


fields = ["filepath", "author"]
rows = []

files = os.listdir("../data/pre_data/")

print("Cleaning Data...")
for file in tqdm(files[:50]):
    rows.append(prepare_file(file))

with open("../outline.csv", 'w') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(fields)
    csv_writer.writerows(rows)

#print("Output to outline.csv successful...")
