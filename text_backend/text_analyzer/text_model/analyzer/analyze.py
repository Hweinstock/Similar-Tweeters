from tqdm import tqdm
import csv
import os
import pickle
import pandas as pd
from ..config_files.config import get_headers, get_text_object
from ..config_files.config import return_configs
from ..utility.utility import author_from_filename
from ..analyzer.comparison import Comparison


PIK = 'text_objects_books.dat'
CONFIGS = return_configs()
DATA_PATH = 'book_data/raw_text/'


def create_comparison_objects_conservative(text_objects):

    objects = []
    for index, text_a in enumerate(tqdm(text_objects)):
        diff_author_added = False
        same_author_added = False
        for text_b in text_objects[index + 1:]:
            if same_author_added and diff_author_added:
                break

            if not same_author_added and text_b["author"] == text_a["author"]:
                objects.append(Comparison(text_a, text_b).report)
                same_author_added = True

            elif not diff_author_added and text_b["author"] != text_a["author"]:
                objects.append(Comparison(text_a, text_b).report)
                diff_author_added = True

    return objects


def create_comparison_objects_exponential(text_objects):
    objects = []
    for index, text_a in enumerate(tqdm(text_objects)):
        for text_b in text_objects[index + 1:]:
            next_line = Comparison(text_a, text_b).report
            objects.append(next_line)

    return objects


def generate_data(args, file_name='comps'):
    text_files = os.listdir(DATA_PATH)

    if args is not None:
        TextObject = get_text_object(args.text_object_type)
    else:
        TextObject = CONFIGS['default_object']

    text_objects = []
    if args is None or args.text_objects is None:
        print("Creating TextObjects...")

        for file in tqdm(text_files):
            author = author_from_filename(file)
            full_path = os.path.join(DATA_PATH + file)
            new_obj = TextObject(filepath_or_text=full_path, author=author)

            # Check if object meets minimums to work with model
            if new_obj.valid:
                text_objects.append(new_obj.to_vector)
            else:
                print("Found Invalid TextObject:", full_path)

        if args is not None and args.save_text:
            print("\nDumping TextObjects to pickle, " + PIK + "...")
            with open(PIK, 'wb') as pf:
                pickle.dump(text_objects, pf)

    else:
        print("Loading in TextObjects from " + args.text_objects)
        with open(args.text_objects, 'rb') as pf:
            text_objects = pickle.load(pf)

    print("\nCreating Comparisons...")

    headers = get_headers()
    if CONFIGS["exponential_comparison"]:
        rows = create_comparison_objects_exponential(text_objects)
    else:
        rows = create_comparison_objects_conservative(text_objects)

    comparisons = pd.DataFrame(data=rows, columns=headers)

    if args is not None and args.save_comps:
        comparisons.to_csv('comps.csv')

    return comparisons


if __name__ == "__main__":
    df = generate_data(None)
