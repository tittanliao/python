import requests as req
import pandas as pd
import pandas.io.sql as pd_sql
import sqlite3 as sql
from time import sleep

sFileName = "ForeignCurrency"
sCSVFilePath = '../../Data/' + sFileName + '.csv'
payload = {
    'download':'',
    'hdn_gostartdate':'2017/01/1',
    'hdn_goenddate':'2017/12/31',
    'syear':'2017',
    'smonth':'01',
    'sday':'1',
    'eyear':'2017',
    'emonth':'12',
    'eday':'31',
    'datestart':'2017/01/1',
    'dateend':'2017/12/31'
}

err_count = 0
while err_count <3:
    try:
        html = req.post('http://www.taifex.com.tw/chinese/3/3_5.asp', data=payload)
        break
    except:
        sleep(5)
        err_count += 1
        continue
if err_count == 3:
    print('connect fail')
    
html.encoding = 'utf-8'
df = pd.read_html(html.text)
df = df[2]  #skip 0,1
df.columns = df.iloc[0] #first row is column name
df = df.drop(0).reset_index(drop=True)  #delet first row
df.sort_index(ascending=False).head()   #sort index
df.to_csv(sCSVFilePath, sep=',', encoding='utf-8-sig', index=False)

'''
#連線至sqlite檔案，若無該檔案sql，則會建立一個新的
conn = sql.connect("../data/twse.db")
#將Dataframe資料寫入sql檔中的'demo2'表中，無該資料表則會自動建立
df.to_sql("demo2", conn, if_exists="replace", index=False)
pd.read_sql_query("select * from demo2;", conn).sort_index(ascending=False).head() #以index排序(由新到舊)
'''