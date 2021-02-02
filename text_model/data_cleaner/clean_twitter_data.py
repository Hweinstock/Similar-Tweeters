import re
from twitter.main import read_in_top_users, tweets_from_handle
from text_model.analyzer.text_objects.tweet import Tweet
import pickle


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

    tweet_groups = [text_from_user(user) for user in users]
    full_text_groups = [" ".join(group) for group in tweet_groups]
    user_objs = [Tweet(text_cluster, raw_text=True) for text_cluster in full_text_groups]

    # Force it to pre-process all data it needs
    user_objs_reports = [obj.report() for obj in user_objs]

    with open('../twitter/top_users.pkl', 'wb') as output_file:
        pickle.dump(user_objs, output_file)


if __name__ == "__main__":
    preload_users()