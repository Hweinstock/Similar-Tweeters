import os
from uuid import uuid4
import re
import csv
from text_model.config_files.config import return_configs
from tqdm import tqdm

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


def cleanup_main(cluster=True):
    raw_files = os.listdir(discord_data_path+"raw_data")
    rows_for_csv = []

    for file in raw_files:

        if not file[0].isnumeric():
            continue
        # Generate filepath for file in raw_data
        filepath = discord_data_path + "raw_data/" + file

        # Remove tags and references
        messages = cleanup_message_file(filepath)

        # Generate uuid for author
        author_uuid = os.path.basename(file)[:18]

        # Break file into message clusters of size n
        if cluster:
            messages = cluster_messages(messages)

            # Write each cluster out to file
            for index, cluster in enumerate(tqdm(messages)):
                file_name = author_uuid + "(" + str(index) + ")"
                new_filepath = discord_data_path + "cleaned_data/" + file_name + '.txt'

                with open(new_filepath, 'w') as text_file:
                    for line in cluster:
                        text_file.write(line)
                        text_file.write("\n")
                rows_for_csv.append([new_filepath, author_uuid])
        else:
            file_name = author_uuid
            new_filepath = discord_data_path + "cleaned_data/" + file_name + '.txt'

            with open(new_filepath, 'w') as text_file:
                for message in messages:
                    text_file.write(message)
                    text_file.write("\n")

            rows_for_csv.append([new_filepath, author_uuid])

        # Generate csv outlining authors and filepaths
        generate_csv(rows_for_csv)

    return True


if __name__ == "__main__":
    cleanup_main()

