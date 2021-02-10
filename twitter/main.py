import requests
import yaml
import os


def read_in_top_users(n=100):
    with open('../twitter/top_users.txt') as txt_file:
        users = txt_file.read().splitlines()

    return users


def check_user_url(handle):

    url = "https://api.twitter.com/2/users/by/username/" + handle
    return url


def recent_tweets_url(handle, max_results=100):
    mrf = "max_results={}".format(max_results)
    q = "query=from:{}".format(handle)
    url = "https://api.twitter.com/2/tweets/search/recent?{}&{}".format(mrf, q)

    return url


def process_configs():
    with open('../twitter/twitter_config.yaml') as config_file:
        return yaml.safe_load(config_file)["twitter_info"]


def create_bearer_token(data):
    return data["bearer_token"]


def twitter_auth_and_connect(bearer_token, url):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    response = requests.request("GET", url, headers=headers)
    return response.json()


def tweets_from_handle(handle):
    # Create Url based on handle for endpoint
    url = recent_tweets_url(handle)

    # Load in auth data from config.yaml
    auth_data = process_configs()
    bearer_token = create_bearer_token(auth_data)

    # Make request and grab text data
    response_json = twitter_auth_and_connect(bearer_token, url)
    try:
        tweet_data = response_json["data"]

    except KeyError:
        print("Unsuccesfull call on handle", handle)
        return []
    response_data = [tweet["text"] for tweet in tweet_data]

    return response_data


def does_twitter_user_exist(handle):

    url = check_user_url(handle)

    auth_data = process_configs()
    bearer_token = create_bearer_token(auth_data)

    response_json = twitter_auth_and_connect(bearer_token, url)
    exists = True

    try:
        response_json["data"]

    except KeyError:
        exists = False

    return exists


if __name__ == "__main__":
    # Example tag
    # print(tweets_from_handle('AOC'))
    print(does_twitter_user_exist('FrostKoala0266'))
    print(does_twitter_user_exist('AOC'))
