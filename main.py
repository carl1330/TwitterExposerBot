from json_decoder import *
from discord_handler import *
from twitter_handler import *

data = open_json("secrets.json")
api = create_tweepy_object(data)
start_bot(data["discord"]["token"], api)


