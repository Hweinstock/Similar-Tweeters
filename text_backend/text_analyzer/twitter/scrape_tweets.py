import snscrape.modules.twitter as sntwitter
import pandas as pd
import re


def clean_text(raw_text):
    text = re.sub(r'http\S+', '', raw_text)
    text = re.sub(r'RT ', '', raw_text)
    return text


def scrape_recent_tweets(username, max_tweets=10):
    df_rows = []
    query = 'from:'+username
    query_results = sntwitter.TwitterSearchScraper(query).get_items()

    for i, tweet in enumerate(query_results):
        if i > max_tweets:
            break
        text = clean_text(tweet.content)
        row = {
            "author": username,
            "source": "twitter_scraper",
            "label": "tweet",
            "text": text,
            "date": tweet.date
        }

        df_rows.append(row)

    tweets = pd.DataFrame(df_rows)

    return tweets


if __name__ == "__main__":
    tweet_df = scrape_recent_tweets("AOC")
