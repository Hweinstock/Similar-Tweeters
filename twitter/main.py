import requests
import yaml
import os


def create_twitter_url(handle, max_results=100):
    mrf = "max_results={}".format(max_results)
    q = "query=from:{}".format(handle)
    url = "https://api.twitter.com/2/tweets/search/recent?{}&{}".format(mrf, q)

    return url


def process_configs():
    with open('../twitter/twitter_config.yaml') as config_file:
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
    print(type(handle), handle)
    print(response_json)
    tweet_data = response_json["data"]
    response_data = [tweet["text"] for tweet in tweet_data]

    return response_data


if __name__ == "__main__":
    # Example tag
    print(tweets_from_handle('AOC'))
