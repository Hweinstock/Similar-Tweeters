from data_cleaner.clean_discord_data import cleanup_main
import os
from analyzer.text_objects.discord_message import DiscordMessage
from analyzer.comparison import Comparison
from config_files.config import get_headers, get_features
import pandas as pd
from analyzer.model.model import load_model


def trim_uuid_from_file(file):
    return file[:36]


def by_username(author_uuid):

    print("Cleaning Discord Data...")
    data_cleaned = cleanup_main(cluster=False)

    if not data_cleaned:
        raise Exception

    path_to_data = "test_messages/cleaned_data"
    files = os.listdir(path_to_data)
    source_files = []
    target_files = []

    for file in files:
        messageObject = DiscordMessage(os.path.join(path_to_data, file), trim_uuid_from_file(file))

        if not messageObject.valid:
            continue
        if file.startswith(author_uuid):
            source_files.append(messageObject)
        else:
            target_files.append(messageObject)

    headers = get_headers()
    rows = []

    for source in source_files:
        for target in target_files:
            rows.append(Comparison(source, target).report)

    comparisons = pd.DataFrame(rows, columns=headers)
    model = load_model()

    X = comparisons.fillna(method='ffill')
    input = X[get_features()]
    predictions = model.predict(input)
    names = X["auth2"]
    names2 = X["auth1"]
    data = {"auths1": names2,'auths2': names, 'predictions': predictions}
    results = pd.DataFrame(data)
    results.to_csv("results.csv")


if __name__ == "__main__":
    uuid = "114296407816404992"

    by_username(uuid)