import tweepy
import time
import json

global q_number

from os import environ

consumer_key = environ['CONSUMER_KEY']
consumer_secret_key = environ['CONSUMER_SECRET']
access_token = environ['ACCESS_KEY']
access_token_secret = environ['ACCESS_SECRET']

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)


def get_quotes():
    with open('quotes.json') as f:
        quotes_json = json.load(f)
    return quotes_json['quotes']


def get_next_quote(q_num):
    quotes = get_quotes()
    next_quote = quotes[q_num]
    return next_quote


def create_tweet(q_num):
    quote = get_next_quote(q_num)
    message = """
            {}
            ~{}
            """.format(quote['quote'], quote['character'])
    return message


def tweet():
    queue_number = 0
    interval = 60 * 15  # Every day

    # Create a tweet
    while not (queue_number == 15):
        print("Posting tweet..... Please wait")
        Tweet = create_tweet(queue_number)
        api.update_status(Tweet)
        queue_number = queue_number + 1
        time.sleep(interval)


if __name__ == "__main__":
    tweet()
