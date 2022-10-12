import sys
import random
from twitter_handler import *


def get_random_tweet(tweets):
    tweet = random.choice(tweets)
    print(get_tweet_url(tweet))


api = create_tweepy_object(open_json("secrets.json"))
user = get_user(api, sys.argv[1])

tweets = get_user_likes(api, user)
get_random_tweet(tweets)



