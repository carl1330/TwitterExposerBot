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
                user = get_user(api, message_array[-1])
                tweets = get_user_tweets(api, user)
                string = get_tweet_url(get_random_tweet(tweets))
                await message.channel.send(string)
            except tweepy.TweepyException as e:
                await message.channel.send(e.api_messages[0])
        if message.content.startswith(COMMAND_PREFIX + ' like '):
            message_array = message.content.split()
            try:
                user = get_user(api, message_array[-1])
                tweets = get_user_likes(api, user)
                string = get_tweet_url(get_random_tweet(tweets))
                await message.channel.send(string)
            except tweepy.TweepyException as e:
                await message.channel.send(e.api_messages[0])

        if message.content.startswith(COMMAND_PREFIX + ' help'):
            await message.channel.send("```\n"
                                       "!t tweet [USERNAME]\n"
                                       "!t like [USERNAME]"
                                       "```\n")

    client.run(token)