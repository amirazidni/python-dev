import csv
import json
import pandas as pd
import os


basePath = os.path.dirname(os.path.abspath('E:\Python Project\WebCrawling'))
df = pd.read_json (r'E:\Python Project\WebCrawling\Hasil_crawling3.json', lines=True)
print(df['full_text'])

data_list=[]

for df in df:
    meta=dict()
    meta['Tweet'] = df['full_text']
    meta['Tanggal'] = df['created_at']
    meta['Nama']=df['name']
    data_list.append(meta)

data=pd.DataFrame(data_list)

writer = pd.ExcelWriter('E:\Python Project\WebCrawling\ZidniCrawling.xlsx')
data.to_excel(writer, 'Sheet1', index=False)
writer.save()


# data=pd.DataFrame(data_list)
# writer = pd.ExcelWriter('E:\Python Project\WebCrawling\Hasil_crawling3.xlsx')
# data.to_excel(writer, 'Sheet1', index=False)
# writer.save()

# df.to_csv(r'E:\Python Project\WebCrawling\TugasCrawling_Zidni_0224.csv', index = None)