import tweepy
import json


def open_json(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError as e:
        print(e)
        exit()
    return data


def create_tweepy_object(data):
    auth = tweepy.OAuth1UserHandler(
        consumer_key=data["twitter"]["api_key"],
        consumer_secret=data["twitter"]["api_secret"],
        access_token=data["twitter"]["access_token"],
        access_token_secret=data["twitter"]["access_secret"])
    return tweepy.API(auth)


def get_user(twitter_api, user_name):
    return twitter_api.get_user(screen_name=user_name)

