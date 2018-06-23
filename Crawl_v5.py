import requests
import datetime
import pandas as pd

sStockId = '2344'
sCSVFilePath = '../../Data/' + sStockId + '_Final.csv'
sModelFilePath = '../../Data/lin_r_model.pickle'
sHtmlFilePath = '../../Data/' + sStockId + '_Predict.html'

today = datetime.date.today().strftime("%Y%m%d")
today2 = datetime.date.today().strftime("%Y/%m/%d")
today_y = today2.split('/')[0]
today_m = today2.split('/')[1]
today_d = today2.split('/')[2]
today3 = '/'.join([today_y, today_m.lstrip('0'), today_d.lstrip('0')])

url1 = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=%s&stockNo='% today + sStockId 
url2 = 'http://www.taifex.com.tw/chinese/3/3_5.asp'
payload = {
    'download':'',
    'hdn_gostartdate':today3,
    'hdn_goenddate':today3,
    'syear':today_y,
    'smonth':today_m,
    'sday':today_d,
    'eyear':today_y,
    'emonth':today_m,
    'eday':today_d,
    'datestart':today2,
    'dateend':today2
}


err_count = 0
while err_count < 3:
    try:
        res1 = requests.get(url1)
        res2 = requests.post(url2, data=payload)
        res2.encoding = 'utf-8'
        break
    except:
        sleep(5)
        err_count += 1
        continue
if err_count == 3:
    print('connect fail')

json = res1.json()
header = json['fields']
data = json['data']
df1 = pd.DataFrame.from_records(data, columns=header).sort_index(ascending=False).head(1).reset_index(drop=True)
df1.iloc[0]['日期'] = today3
df2 = pd.read_html(res2.text)
df2 = df2[2]
df2.columns = df2.iloc[0]
df2 = df2.drop(0).reset_index(drop=True).sort_index(ascending=False).head(1)
df3 = pd.merge(df1, df2, on='日期')
df4 = pd.read_csv(sCSVFilePath)

if not ((df4['日期'] == today3)).any():
    df4 = df4.append(df3, ignore_index=True)
    df4.to_csv(sCSVFilePath, sep=',', encoding='utf-8-sig', index=False)
df4.sort_index(ascending=False).head()

def regData(x):
    for i, row in x.iterrows():
        x.loc[i, '成交股數'] = row['成交股數'].replace(',', '')
        x.loc[i, '成交筆數'] = row['成交筆數'].replace(',', '')
    for i, row in X.iterrows():
        if i <= len(X)-2:
            x.loc[i, '成交股數'] = int(x.loc[i+1, '成交股數'])/int(x.loc[i, '成交股數'])
            x.loc[i, '成交筆數'] = int(x.loc[i+1, '成交筆數'])/int(x.loc[i, '成交筆數'])
            x.loc[i, '美元／新台幣'] = float(x.loc[i+1, '美元／新台幣'])/float(x.loc[i, '美元／新台幣'])
    return x

X = df4[['成交股數', '成交筆數', '美元／新台幣']]
X = regData(X.sort_index(ascending=False))
X = X.sort_index(ascending=True)
X.columns = ['成交股數[Normalize]', '成交筆數[Normalize]', '美元／新台幣[Normalize]']
df4 = pd.concat([df4, X.shift()], axis=1)

df5 = df4.sort_index(ascending=False).head(2).reset_index(drop=True)
pred1 = float(df5.loc[0, '成交股數[Normalize]'])
pred2 = float(df5.loc[0, '成交筆數[Normalize]'])
pred3 = float(df5.loc[0, '美元／新台幣[Normalize]'])

import pickle
with open(sModelFilePath, 'rb') as f:
    regression_model = pickle.load(f)
    pred_result = regression_model.predict([[pred1, pred2, pred3]])
    print('預測結果: %f' % pred_result)

from datetime import timedelta
tomorrow = (datetime.date.today() + timedelta(days=1)).strftime("%Y/%m/%d")
tomorrow_y = tomorrow.split('/')[0]
tomorrow_m = tomorrow.split('/')[1]
tomorrow_d = tomorrow.split('/')[2]
today5 = '/'.join([tomorrow_y, tomorrow_m.lstrip('0'), tomorrow_d.lstrip('0')])

pred_col = [today5, '', '', '', '', '', float(pred_result), '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
pred_col = pd.DataFrame(pred_col).T
pred_col.columns = list(df5.columns)

df6 = df4.append(pred_col, ignore_index=True)
df6.sort_index(ascending=False).to_html(sHtmlFilePath, index=False)
