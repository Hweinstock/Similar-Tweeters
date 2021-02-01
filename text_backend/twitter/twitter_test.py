import requests
import pandas as pd
import json
import ast
import yaml


def create_twitter_url(handle, max_results=100):
    mrf = "max_results={}".format(max_results)
    q = "query=from:{}".format(handle)
    url = "https://api.twitter.com/2/tweets/search/recent?{}&{}".format(mrf, q)

    return url


def process_configs():
    with open('twitter_config.yaml') as config_file:
        return yaml.safe_load(config_file)


def create_bearer_token(data):
    return data["search_tweets_api"]["bearer_token"]


def twitter_auth_and_connect(bearer_token, url):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    response = requests.request("GET", url, headers=headers)
    return response.json()


def tweets_from_handle(handle):
    # Create Url based on handle for endpoint
    url = create_twitter_url(handle)

    # Load in auth data from config.yaml
    auth_data = process_configs()
    bearer_token = create_bearer_token(auth_data)

    # Make request and grab text data
    response_json = twitter_auth_and_connect(bearer_token, url)
    response_data = [tweet["text"] for tweet in response_json["data"]]

    return response_data


if __name__ == "__main__":
    # Example tag
    tweets_from_handle('AOC')
