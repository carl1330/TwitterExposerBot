import sys
from twitter_handler import *

api = create_tweepy_object(open_json("secrets.json"))
user = get_user(api, sys.argv[1])

tweets = get_user_tweets(api, user)

print(get_tweet_url(tweets[1]))