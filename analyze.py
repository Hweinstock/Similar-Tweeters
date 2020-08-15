from text import TextObject
from comparison import Comparison
from tqdm import tqdm
import csv

with open('outline.csv') as csvfile:
    readCSV = csv.reader(csvfile)

    print("Creating TextObjects...")

    # Convert each row (except Header) to textObject
    text_objects = [TextObject(filepath=row[0], author=row[1]) for row in tqdm(readCSV) if row[0] != "filepath"]

    with open('comps.csv', 'w') as comp_csv:
        writeCSV = csv.writer(comp_csv)
        headers = ["top_n_word_comparison",
                   "average_word_length_comparison",
                   "top_n_sentence_lengths_comparison",
                   "punctuation_comparison",
                   "same_author",
                   "auth_1",
                   "auth_2"]

        rows = []
        writeCSV.writerow(headers)
        print("Creating Comparisons...")

        # Create Comparison Objects and add them to rows

        for index, text_a in enumerate(tqdm(text_objects)):
            for text_b in text_objects[index+1:]:
                rows.append(Comparison(text_a, text_b).report)

        writeCSV.writerows(rows)
