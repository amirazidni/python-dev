from twython import Twython
import json
import pandas as pd

tKey = 'tokwkWXwVWbxD2kyMr1lBy9KZ'
tSecret = 'YHX6ruQHt3S7reeQoFy2sumkz88s4v3Ftwcwyu3ikhNP09wBAw'
tAccessToken = '1251059707965394944-P5gDjjYKdpsVZFskO8o0fFEWw3cOpw'
tAccessTokenSecret = 'uhbdvnqLVHqzX9POYQJuStOG8FUkuoqTp30epZMDul1wn'

t = Twython(app_key = tKey,
    app_secret=tSecret,
    oauth_token=tAccessToken,
    oauth_token_secret=tAccessTokenSecret)

term='CoronaBungkamSkandalKorupsi'
tweet=t.search(q=term, count=100, result_type='recent')

data_list=[]

print(tweet.keys())

# for twit in tweet['statuses']:
#     meta=dict()
#     meta['tweet']=twit['text']
#     meta['waktu']=twit['created_at']
#     meta['user']=twit['user']['screen_name']
#     data_list.append(meta)

# data=pd.DataFrame(data_list)

# writer = pd.ExcelWriter('E:\Python Project\WebCrawling\Hasil_crawling.xlsx')
# data.to_excel(writer, 'Sheet1', index=False)
# writer.save()