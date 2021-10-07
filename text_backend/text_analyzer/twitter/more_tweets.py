import tweepy
import csv
import pandas as pd
import yaml
import snscrape.modules.twitter as sntwitter


def process_twitter_configs():
    with open('../twitter/twitter_config.yaml') as config_file:
        return yaml.safe_load(config_file)["twitter_info"]


def create_bearer_token(data):
    return data["search_tweets_api"]["bearer_token"]


def authenticate():

    # twitter_configs = process_twitter_configs()
    # consumer_key = twitter_configs["consumer_key"]
    # consumer_secret = twitter_configs["consumer_key_secret"]
    # access_token = twitter_configs["access_token"]
    # access_secret = twitter_configs["access_token_secret"]
    #
    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_secret)

    csvFile = open('15-10-2020.csv', 'a')  # creates a file in which you want to store the data.
    csvWriter = csv.writer(csvFile)

    maxTweets = 1000  # the number of tweets you require
    # for i, tweet in enumerate(sntwitter.TwitterSearchScraper('#covid19' +
    #                                                          'since:2020-10-15 until:2020-10-16'
    #                                                          ).get_items()):
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:AOC'
                                                             ).get_items()):

        if i > maxTweets:
            break
        print(tweet.date)
        csvWriter.writerow([tweet.date, tweet.content])


if __name__ == "__main__":
    authenticate()
    # try:s
    #     redirect_url = auth.get_authorization_url()
    # except tweepy.TweepError:
    #     print("Error: failed to get request token!")