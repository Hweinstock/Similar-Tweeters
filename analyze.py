from text import TextObject
import os
from comparison import Comparison
from tqdm import tqdm
import csv

with open('outline.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    # Convert each row (except Header) to textObject
    print("Creating TextObjects...")
    text_objects = [TextObject(filepath=row[0], author=row[1]) for row in tqdm(readCSV) if row[0] != "filepath"]

    with open('comps.csv', 'w') as comp_csv:
        writeCSV = csv.writer(comp_csv)
        headers = ["top_n_word_comparison",
                   "average_word_length_comparison",
                   "top_n_sentence_lengths_comparison",
                   "punctuation_comparison",
                   "same_author?",
                   "auth_1",
                   "auth_2"]

        rows = []
        writeCSV.writerow(headers)
        print("Creating Comparisons...")
        for index, text_a in enumerate(text_objects):
            for text_b in text_objects[index+1:]:
                rows.append(Comparison(text_a, text_b).report)

        writeCSV.writerows(rows)


# if __name__ == "__main__":
#
#     """
#     Examples/Testing
#     1-3, 2-4 same authors
#     """
#
#     Dracula = TextObject('test_data/dracula_bstoker.txt')
#     MobyDick = TextObject('test_data/moby_dick_hmelville.txt')
#     Worm = TextObject('test_data/worm_bstoker.txt')
#     Bartleby = TextObject('test_data/bartleby_hmelville.txt')
#
#     textObjects = []
#     for file in os.listdir('test_data'):
#         textObjects.append(TextObject('test_data/'+file))
#
#     source = textObjects[1]
#     for to in textObjects:
#         print(source.filepath, to.filepath, Comparison(source, to).report)

    # print(Comparison(Dracula, MobyDick).punctuation_comparison())
    # print(Comparison(Dracula, Worm).punctuation_comparison())
    # print(Comparison(MobyDick, Bartleby).punctuation_comparison())
    # print(str(MobyDick))

    # Old code for debugging average setence length.
    # s = sorted(MobyDick.list_of_sentences(), key=words_in_sentence, reverse=True)
    # for st in s:
    #     print(st)
    #print("List of Sentences: ", MobyDick.top_n_sentence_lengths(10))
