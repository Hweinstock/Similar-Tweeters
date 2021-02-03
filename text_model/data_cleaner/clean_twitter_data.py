import re
from twitter.main import read_in_top_users, tweets_from_handle
from text_model.analyzer.text_objects.tweet import Tweet
import json
import requests


def clean_tweet(tweet):
    tweet = re.sub(r'http\S+', '', tweet)
    tweet = re.sub(r'RT ', '', tweet)
    return tweet


def text_from_user(handle):
    tweets = tweets_from_handle(handle)
    cleaned_tweets = [clean_tweet(tw) for tw in tweets]

    return cleaned_tweets


def preload_users(users=None):
    if users is None:
        users = read_in_top_users()

    tweet_groups = {}

    for user in users:
        tweet_groups[user] = " ".join(text_from_user(user))

    user_vectors = [Tweet(text, raw_text=True, author=user).to_vector for (user, text) in tweet_groups.items()]

    # Remove the vectors that were unable to get any text
    user_vectors = [vector for vector in user_vectors if vector['top_n_words'] != []]

    for vector in user_vectors:

        # First check if data already exists in db.
        get_data = {"author": vector["author"]}

        first_response = requests.get('http://127.0.0.1:8000/api/textObjects/doesExist/', params=get_data)
        query_result = json.loads(first_response.content)
        already_posted = query_result['status']

        if not already_posted:

            # If it can't find that author, add them to the db
            post_data = {}

            for key in vector:
                value = vector[key]
                post_data[key] = json.dumps(value)

            post_data["label"] = "top100"

            response = requests.post('http://127.0.0.1:8000/api/textObjects/', data=post_data)


if __name__ == "__main__":
    preload_users()