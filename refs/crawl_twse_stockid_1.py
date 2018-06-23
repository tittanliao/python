import datetime
import requests
import pyodbc
import pandas as pd
from bs4 import BeautifulSoup

#本國上市證券國際證券辨識號碼一覽表
response = requests.get('http://isin.twse.com.tw/isin/C_public.jsp?strMode=2')
soup = BeautifulSoup(response.text, 'html.parser')
list = pd.read_html(str(soup.prettify))
df = list[0] #change to pandas dataframe
#df.to_csv('./crawl_twse_stockid_1', sep=',', encoding='utf-8-sig', index=False)

#generate db records
cols = ['id','name','isin_code','create_day','market_type','market_type_detail','industry_type','update_time','update_user']
rows = []
s_detail = ''
dt_now = datetime.datetime.now()
dt_day = dt_now.strftime("%Y%m%d")
for i,row in df.iterrows():
    if str(row[2]) == '上市日':
        continue
    if str(row[2]) == 'nan':
        s_detail = row[0]
        continue
    if str(row[4]) == 'nan':
        row[4] = ''
    #default
    id = row[0]
    name = row[0]
    isin_code = row[1]
    create_day = '19910101'
    market_type = row[3]
    market_type_detail = s_detail
    industry_type = row[4]
    update_time = dt_now
    update_user = 'tittan'
    #change format
    a = row[0].split('\u3000')
    if len(a) == 2:
        id = a[0]
        name = a[1]
    else:
        #4148 全宇生技-KY
        a = row[0].split(' ')
        if len(a) == 2:
            id = a[0]
            name = a[1]
    a_date = row[2].split('/')
    if len(a_date) == 3: 
        a_date[0] = str(a_date[0])
        a_date[1] = str(a_date[1]).zfill(2)
        a_date[2] = str(a_date[2]).zfill(2)
        create_day = ''.join(a_date)
    rows.append([id,name,isin_code,create_day,market_type,market_type_detail,industry_type,update_time,update_user])
df_final = pd.DataFrame(rows,columns=cols)
df_final.to_csv('./csv/' + dt_day + '_crawl_twse_stockid_1.csv', sep=',', encoding='utf-8-sig', index=False)

#db handler
server = 'aholic.cc'
database = 'stock'
username = 'sa'
password = 'qweqwe1!qweqwe1!'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("DELETE FROM isin WHERE 1=1")
cnxn.commit()
for i,row in df_final.iterrows():
    try:
        sql='INSERT INTO isin(id,name,isin_code,create_day,market_type,market_type_detail,industry_type,update_time,update_user) VALUES (?,?,?,?,?,?,?,?,?)'
        cursor.execute(sql,row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
        cnxn.commit()
    except Exception as e:
        print(str(e)+'@@'+row[0])
        break

cnxn.close()
'''dataframe after bf 
[0] 有價證券代號及名稱
[1] 國際證券辨識號碼(ISIN Code)
[2] 上市日
[3] 市場別
[4] 產業別
[5] CFICode
[6] 備註
'''