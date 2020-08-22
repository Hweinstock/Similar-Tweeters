from comparison import Comparison
from tqdm import tqdm
import csv
from config import get_headers, get_text_object
import pickle
from config import return_configs


PIK = 'text_objects.dat'
CONFIGS = return_configs()


def create_comparison_objects_conservative(text_objects):

    objects = []
    for index, text_a in enumerate(tqdm(text_objects)):
        diff_author_added = False
        same_author_added = False
        for text_b in text_objects[index + 1:]:
            if same_author_added and diff_author_added:
                break

            if not same_author_added and text_b.author == text_a.author:
                objects.append(Comparison(text_a, text_b).report)
                same_author_added = True

            elif not diff_author_added and text_b.author != text_a.author:
                objects.append(Comparison(text_a, text_b).report)
                diff_author_added = True

    return objects


def create_comparison_objects_exponential(text_objects):
    objects = []
    for index, text_a in enumerate(tqdm(text_objects)):
        for text_b in text_objects[index + 1:]:
            objects.append(Comparison(text_a, text_b).report)

    return objects


def generate_data(args, file_name="comps"):
    file_name = file_name+'.csv'
    if args is not None:
        TextObject = get_text_object(args.text_object_type)
    else:
        TextObject = CONFIGS['default_object']

    with open('outline.csv', encoding='ISO-8859-1') as csvfile:
        readCSV = csv.reader(csvfile)

        # Convert each row (except Header) to textObject
        if args is None or args.text_objects is None:
            print("Creating TextObjects...")
            text_objects = []
            for row in tqdm(readCSV):
                if row[0] != 'filepath':
                    try:
                        new_text = TextObject(filepath=row[0], author=row[1])
                        if new_text.valid:
                            text_objects.append(TextObject(filepath=row[0], author=row[1]))
                    except UnicodeDecodeError:
                        pass

            print("Dumping TextObjects to pickle, "+PIK+"...")
            with open(PIK, 'wb') as pf:
                pickle.dump(text_objects, pf)
        else:
            print("Loading in TextObjects from "+args.text_objects)
            with open(args.text_objects, 'rb') as pf:
                text_objects = pickle.load(pf)

        with open(file_name, 'w') as comp_csv:
            writeCSV = csv.writer(comp_csv)
            print("Creating Comparisons...")

            headers = get_headers()
            if CONFIGS["exponential_comparison"]:
                rows = create_comparison_objects_exponential(text_objects)
            else:
                rows = create_comparison_objects_conservative(text_objects)

            writeCSV.writerow(headers)
            writeCSV.writerows(rows)

    return file_name


if __name__ == "__main__":
    generate_data(None)
