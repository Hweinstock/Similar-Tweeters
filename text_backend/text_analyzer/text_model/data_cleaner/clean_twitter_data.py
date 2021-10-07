import re
from ...twitter.scrape_tweets import scrape_recent_tweets


def clean_text(raw_text):
    text = re.sub(r'http\S+', '', raw_text)
    text = re.sub(r'RT ', '', raw_text)
    return text


def text_from_user(handle):
    tweets = scrape_recent_tweets(handle)
    cleaned_tweets = list(tweets)
    # cleaned_tweets = [clean_scraped_tweet(tw) for tw in tweets["text"].tolist()]
