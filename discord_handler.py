import discord
from twitter_handler import *

COMMAND_PREFIX = "!t"


def start_bot(token, api):
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith(COMMAND_PREFIX + ' tweet '):
            message_array = message.content.split()
            try:
                if len(message_array) == 3:
                    await create_tweet_message(message, message_array[-1], 0)
                else:
                    await create_tweet_message(message, message_array[2], int(message_array[-1]))
            except tweepy.TweepyException as e:
                await message.channel.send(e.api_messages[0])

        if message.content.startswith(COMMAND_PREFIX + ' like '):
            message_array = message.content.split()
            try:
                if len(message_array) == 3:
                    await create_like_message(message, message_array[-1], 0)
                else:
                    await create_like_message(message, message_array[2], int(message_array[-1]))
            except tweepy.TweepyException as e:
                await message.channel.send(e.api_messages[0])

        if message.content.startswith(COMMAND_PREFIX + ' help'):
            await message.channel.send("```\n"
                                       "!t tweet [USERNAME] [SINCE]\n"
                                       "!t like [USERNAME] [SINCE]\n"
                                       "Since is a number between 0-7\n"
                                       "A higher number will result in earlier tweets (earliest 2015)"
                                       "```\n")

    async def create_tweet_message(message, username, i):
        user = get_user(api, username)
        tweets = get_user_tweets(api, user, i)
        try:
            tweet = get_random_tweet(tweets)
            string = get_tweet_url(tweet)
            await message.channel.send(string)
        except IndexError as e:
            await message.channel.send(e)

    async def create_like_message(message, username, i):
        user = get_user(api, username)
        tweets = get_user_likes(api, user, i)
        try:
            tweet = get_random_tweet(tweets)
            string = get_tweet_url(tweet)
            await message.channel.send(string)
        except IndexError as e:
            await message.channel.send(e)

    client.run(token)