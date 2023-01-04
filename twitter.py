import tweepy
import time

consumer_key = 'VJKt4ScaJzTIwVmhqXFn5zYH9'
consumer_secret = 'P07z4Anxz5LEVOydchVKnuI2lCYigpNLlmq65sS5ag6CiAQYsj'
access_token = '1334892542819627010-Z9ZJ7FNOe0zR1NwYmTSQ1QBXihKqvh'
# some unique keys which connects the code to the twitter bot/app
access_token_secret = 'ipPFWwhYxASab0PkMFba1ew5iQp6taQtOrSDCcfOqqrfd'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  # access the account
# access the bot(authentication)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)  # api becomes the bot object

user = api.me()  # Access the user info
print(user.name)  # prints your name.
print(user.screen_name)  # screen name
print(user.followers_count)  # number of followers


def limit_handle(cursor):  # Limit the number of request to twitter server
    while True:
        try:
            yield cursor.next()  # gets the next object
        except tweepy.RateLimitError:
            # if error ecountered delays the code (releives the server)
            time.sleep(1000)

# Be nice to your followers. Follow everyone! Cursor() used for various extra tasks like grabbing followers or searching
# for follower in limit_handle(tweepy.Cursor(api.followers).items()): #follower gets followers
#  if follower.name == '':#checks the condition for the follower name
#    print(follower.name)
#   follower.follow()


search = "virat kohli"
numberOfTweets = 5

# Be a narcisist and love your own tweets. or retweet anything with a keyword!
# grabs 5 items after searching 'virat kohli'
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('liked the tweet')
    except tweepy.TweepError as e:  # if error encountered
        print(e.reason)
    except StopIteration:  # to stop iteration if StopIteration encountered
        break
user1 = api.get_user('@imVkohli')
print(user1.name)
print(user1.screen_name)
