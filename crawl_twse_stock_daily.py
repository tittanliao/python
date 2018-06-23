import datetime
import requests
import json
import pyodbc
import pandas as pd
from time import sleep

'''function
'''
def get_dbo():
	server = 'aholic.cc'
	database = 'stock'
	username = 'sa'
	password = 'qweqwe1!qweqwe1!'
	driver= '{ODBC Driver 13 for SQL Server}'
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	return cnxn
	
'''main
'''
#local var
dt_now = datetime.datetime.now()
dt_day = dt_now.strftime("%Y%m%d")
s_filename = './csv/' + dt_day + '_crawl_twse_stock_daily.csv'
i_sleep = 5
i_year_start = 2017
i_year_end = 2018
#format:'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20170901&stockNo=2330'
sURL = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json'

#get db
cnxn = get_dbo()
sql = "SELECT id FROM isin WHERE market_type_detail IN ('股票','ETF')"
df_db = pd.read_sql(sql, cnxn)

months = []
for x in range(i_year_start,i_year_end):
        for y in range(1,13):
                months.append(str(x).zfill(4) + str(y).zfill(2) + "01")

months.sort(reverse=True)

'''test code
cols = [id]
rows = []
rows.append('2344')
rows.append('2330')
df_db = pd.DataFrame(rows,columns=cols)
months = ['20171201','20171101']
'''

for i, r in df_db.iterrows():
	stockid = r[0]
	dResult = {}
	for x in months:
		sGet = sURL + '&date=' + x + '&stockNo=' + stockid
		err_count = 0
		while err_count < 3:
			try:
				res = requests.get(sGet)
				dResult[x] = res.json()
				#sleep 5 secs
				sleep(5)
				break
			except:
				sleep(5)
				err_count += 1
				continue
		if err_count == 3:
			print('connect fail')
	
	header = dResult[list(dResult)[0]]['fields']
	data = dResult[list(dResult)[0]]['data']
	iIndex = 0
	for x in dResult:
		if iIndex != 0:
			data.extend(dResult[x]['data'])
		iIndex += 1
	
	df = pd.DataFrame.from_records(data, columns=header)
	df.sort_index(ascending=False).head()
	
	#generate db records
	cols = ['id','day','vol','turnover','price_open','price_high','price_low','price_close','spread','count']
	rows = []
	for i, row in df.iterrows():
		try:
			#default
			id = stockid
			day = '19110101'
			vol = int(str(row[1]).replace(",", ""))
			turnover = int(str(row[2]).replace(",", ""))
			price_open = 0
			price_high = 0
			price_low = 0
			price_close = 0
			#0052 富邦科技,106/11/01,price --
			if vol > 0:
				price_open = float(str(row[3]))
				price_high = float(str(row[4]))
				price_low = float(str(row[5]))
				price_close = float(str(row[6]))
			#0050 元大台灣50,106/02/08,漲跌價差,X0.00
			spread = float(str(row[7]).replace("X", ""))
			count = float(str(row[8]).replace(",", ""))
			a_date = row[0].split('/')
			if len(a_date) == 3: 
				a_date[0] = str(int(a_date[0])+1911)
				a_date[1] = str(a_date[1]).zfill(2)
				a_date[2] = str(a_date[2]).zfill(2)
				day = ''.join(a_date)
			rows.append([id,day,vol,turnover,price_open,price_high,price_low,price_close,spread,count])
		except Exception as e:
			print(id+'@@'+row[0]+'@@'+str(e))
			continue
	
	df_final = pd.DataFrame(rows,columns=cols)
	#df_final.to_csv(s_filename, sep=',', encoding='utf-8-sig', index=False)
	#db handler
	cnxn = get_dbo()
	cursor = cnxn.cursor()
	for i,row in df_final.iterrows():
		try:
			sql='INSERT INTO daily(id,day,vol,turnover,price_open,price_high,price_low,price_close,spread,count) VALUES (?,?,?,?,?,?,?,?,?,?)'
			cursor.execute(sql,row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
			cnxn.commit()
		except Exception as e:
			print(str(e)+'@@'+row[0])
			break
	
	cnxn.close()
	#break

'''comment
[0] 日期
[1] 成交股數
[2] 成交金額
[3] 開盤價
[4] 最高價
[5] 最低價
[6] 收盤價
[7] 漲跌價差
[8] 成交筆數
'''