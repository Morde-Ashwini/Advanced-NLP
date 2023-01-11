
import tweepy
import pandas as pd
import configparser


#Read all credentials from config file

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authenticate twitter account
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


#get tweets for particular user:

#user = 'deepikapadukone'    
#limit = 1000

#tweets = tweepy.Cursor(api.user_timeline,screen_name = user, count = 200, tweet_mode= 'extended').items(limit)
#columns = ['user','tweets']

#data = []

#for tweet in tweets:
 #   data.append([tweet.user.screen_name, tweet.full_text])

#df = pd.DataFrame(data, columns=columns)

#print(df)


#Search Tweets for hashtag:

keyword = input("Enter hashtag to search tweets: ")
limit = 300


tweets = tweepy.Cursor(api.search_tweets, q=keyword,lang="en",count = 100, tweet_mode= 'extended').items(limit)
columns = ['Created_at','Username','Tweet']

data = []

for tweet in tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)

print (df)

#Save data to CSV file:

df.to_csv('test.csv')

