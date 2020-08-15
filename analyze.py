from text import TextObject
from comparison import Comparison
from tqdm import tqdm
import csv


def get_headers():
    headers = ["top_n_word_comparison",
               "average_word_length_comparison",
               "top_n_sentence_lengths_comparison",
               "punctuation_comparison",
               "same_author",
               "auth_1",
               "auth_2"]

    return headers


def create_comparison_objects(text_objects):
    objects = []
    for index, text_a in enumerate(tqdm(text_objects)):
        for text_b in text_objects[index + 1:]:
            objects.append(Comparison(text_a, text_b).report)

    return objects


def generate_data(file_name="comps"):
    file_name = file_name+'.csv'
    with open('outline.csv') as csvfile:
        readCSV = csv.reader(csvfile)

        print("Creating TextObjects...")

        # Convert each row (except Header) to textObject
        text_objects = [TextObject(filepath=row[0], author=row[1]) for row in tqdm(readCSV) if row[0] != "filepath"]

        with open(file_name, 'w') as comp_csv:
            writeCSV = csv.writer(comp_csv)
            print("Creating Comparisons...")

            headers = get_headers()
            rows = create_comparison_objects(text_objects)

            writeCSV.writerow(headers)
            writeCSV.writerows(rows)

    return file_name

