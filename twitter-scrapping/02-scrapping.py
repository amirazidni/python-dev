from twython import Twython
import tweepy
import pandas as pd
import json

consumer_key = 'tokwkWXwVWbxD2kyMr1lBy9KZ'
consumer_secret = 'YHX6ruQHt3S7reeQoFy2sumkz88s4v3Ftwcwyu3ikhNP09wBAw'
access_token = '1251059707965394944-P5gDjjYKdpsVZFskO8o0fFEWw3cOpw'
access_secret = 'uhbdvnqLVHqzX9POYQJuStOG8FUkuoqTp30epZMDul1wn'
tweetsPerQry = 100
maxTweets = 500
hashtag = "boleh lewat jogja"

authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
authentication.set_access_token(access_token, access_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
twython = Twython(app_key = consumer_key, app_secret=consumer_secret, oauth_token=access_token, oauth_token_secret=access_secret)
maxId = -1
tweetCount = 0
data_list=[]

while tweetCount < maxTweets:
	if(maxId <= 0):
		newTweets = api.search(q=hashtag, count=tweetsPerQry, result_type="recent")
		newTweets2 = twython.search(q=hashtag, count=tweetsPerQry, result_type="recent")
	else:
		newTweets = api.search(q=hashtag, count=tweetsPerQry, max_id=str(maxId - 1), result_type="recent")
		newTweets2 = twython.search(q=hashtag, count=tweetsPerQry, max_id=str(maxId - 1), result_type="recent")

	if not newTweets:
		print("Tweet Habis")
		break
	
	# with open("E:\Python Project\WebCrawling\Hasil_crawling.json", 'a') as f:
	# 	for tweeti in newTweets:
	# 		json.dump(tweeti._json, f)
	# 		f.write('\n')

	for twit in newTweets2['statuses']:
		meta=dict()
		meta['tweet']=twit['text']
		meta['waktu']=twit['created_at']
		meta['user']=twit['user']['screen_name']
		data_list.append(meta)

	tweetCount += len(newTweets)	
	maxId = newTweets[-1].id
	

data=pd.DataFrame(data_list)
writer = pd.ExcelWriter('E:\Python Project\WebCrawling\Hasil_crawling.xlsx')
data.to_excel(writer, 'Sheet1', index=False)
writer.save()
