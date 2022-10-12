import datetime
import tweepy
import random
import calendar
import time

TID_TIME_ARRAY = [1477429324181561344, 1345157610928893952, 1212523617327689729,
                  1080250801816252416, 947980639315271681, 815707920109215744,
                  683074647655608320, 550802614255112193]

def create_tweepy_object(data):
    auth = tweepy.OAuth1UserHandler(
        consumer_key=data["twitter"]["api_key"],
        consumer_secret=data["twitter"]["api_secret"],
        access_token=data["twitter"]["access_token"],
        access_token_secret=data["twitter"]["access_secret"])
    return tweepy.API(auth)


def get_user(api, user_name):
    return api.get_user(screen_name=user_name)


def get_user_tweets(api, user, tid=0, count=200):
    if tid > len(TID_TIME_ARRAY):
        tid = len(TID_TIME_ARRAY)

    if tid == 0:
        return api.user_timeline(user_id=user.id, count=count)
    else:
        return api.user_timeline(user_id=user.id, count=count, max_id=TID_TIME_ARRAY[tid])


def get_user_likes(api, user, tid=0, count=200):
    if tid > len(TID_TIME_ARRAY):
        tid = len(TID_TIME_ARRAY)

    if tid == 0:
        return api.get_favorites(user_id=user.id, count=count)
    else:
        return api.get_favorites(user_id=user.id, count=count, max_id=TID_TIME_ARRAY[tid])


def get_tweet_url(tweet):
    return "https://twitter.com/" + tweet.user.screen_name + "/status/" + str(tweet.id)


def print_tweets(api, tweets):
    for tweet in tweets:
        print(tweet.text)


def get_random_tweet(tweets):
    try:
        return random.choice(tweets)
    except IndexError:
        raise IndexError("Since set too high, user doesn't have tweets from before that period")

