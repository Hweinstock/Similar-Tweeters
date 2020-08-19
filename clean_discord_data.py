import os
from uuid import uuid4
import re
import csv
from config import return_configs

discord_data_path = "test_messages/"

CONFIGS = return_configs()
def generate_author_identifier():
    return str(uuid4())


def cluster_messages(messages, n=CONFIGS['cluster_size']):
    return [messages[i:i + n] for i in range(0, len(messages), n)]


def remove_refs(message):
    no_refs = re.sub('<[^>]*>', '', message)
    no_mentions = re.sub('>', '', no_refs)
    return no_mentions


def cleanup_message_file(file):
    messages = []

    with open(file, 'r',  encoding='ISO-8859-1') as discord_file:
        for message in discord_file:
            stripped_message = message.strip()
            cleaned_message = remove_refs(stripped_message)
            messages.append(cleaned_message)

    return messages


def generate_csv(rows):
    fields = ["filepath", "author"]

    with open("outline.csv", 'w') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(fields)
        csv_writer.writerows(rows)


def cleanup_main():
    raw_files = os.listdir(discord_data_path+"raw_data")
    rows_for_csv = []

    for file in raw_files:

        # Generate filepath for file in raw_data
        filepath = discord_data_path + "raw_data/" + file

        # Remove tags and references
        messages = cleanup_message_file(filepath)

        # Generate uuid for author
        author_uuid = generate_author_identifier()

        # Break file into message clusters of size n
        clusters = cluster_messages(messages)

        # Write each cluster out to file
        for index, cluster in enumerate(clusters):
            file_name = author_uuid + "(" + str(index) + ")"
            new_filepath = discord_data_path + "cleaned_data/" + file_name + '.txt'

            with open(new_filepath, 'w') as text_file:
                for line in cluster:
                    text_file.write(line)
                    text_file.write("\n")
            # Trim to .. to make it accessible to analyze.py
            relative_path = new_filepath[3:]
            rows_for_csv.append([relative_path, author_uuid])

        # Generate csv outlining authors and filepaths
        generate_csv(rows_for_csv)


if __name__ == "__main__":
    cleanup_main()

