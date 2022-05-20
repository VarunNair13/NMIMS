import tweepy

# Your app's bearer token can be found under the Authentication Tokens section
# of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
bearer_token = "AAAAAAAAAAAAAAAAAAAAAG20cQEAAAAAnaj3TjJPT21b337KEAMOk7nrUI8%3DZHZiZA4H23NhprGBUqDLyFR6004DWexykBYQOQHgBgmayuws2s"

# Your app's API/consumer key and secret can be found under the Consumer Keys
# section of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
consumer_key = "xvTUC9wvKZH089ZYURBBl9ZdI"
consumer_secret = "iT2olzUdVBc89l21LvGWSfKnrgZdj0prcDifOJuPEwjbrrBY0l"

# Your account's (the app owner's account's) access token and secret for your
# app can be found under the Authentication Tokens section of the
# Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
access_token = "1308836236384243712-267fBdjFAujeSae8yGl4GBTwI1VdOl"
access_token_secret = "7knjlYPd5pC1Bt0JgMMerCbSjlzA763Wv5ddgy3NE9zrR"

# You can authenticate as your app with just your bearer token
client = tweepy.Client(bearer_token=bearer_token)

# You can provide the consumer key and secret with the access token and access
# token secret to authenticate as a user
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

client = tweepy.Client(bearer_token)



response = client.search_recent_tweets("Elon",max_results= 30)



print(response.meta)



tweets = response.data



for tweet in tweets:

    print(tweet.id)

    print(tweet.text)
