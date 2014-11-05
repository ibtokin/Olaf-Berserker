from twitter import *
import os

OAUTH_TOKEN = ("************")
OAUTH_SECRET =("************")
CONSUMER_KEY = ("************")
CONSUMER_SECRET = ("**********")


t = Twitter(
            auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
                       CONSUMER_KEY, CONSUMER_SECRET)
)

# Get the status of a particular friend:
Morton201 = t.statuses.user_timeline(screen_name="Morton201")

author = (Morton201[0]['user']['screen_name'])
tweet = (Morton201[0]['text'])
tweet_url = (Morton201[0]['extended_entities']['media'][1]['url'])

print("\n\n")
print(author)
print("\n")
print(tweet)
print("\n")
print(tweet_url)

print("\n\nFuck Yeah!\n\n")