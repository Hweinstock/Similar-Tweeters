from zip_to_dict import prepare_file
import os, csv
from tqdm import tqdm


fields = ["filepath", "author"]
rows = []

files = os.listdir("../book_data/zip_files/")
print("Cleaning Data...")
for file in tqdm(files[:100]):
    next_file = prepare_file(file)
    if next_file is not None:
        rows.append(prepare_file(file))
    else:
        print("WARNING", file, "Could not prepare file, Possibly of wrong form. ")

with open("../outline.csv", 'w') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(fields)
    csv_writer.writerows(rows)

