import pandas as pd

sStockId = '2344'
sFileName = 'ForeignCurrency'
sCSVFilePath = '../../Data/' + sStockId + '_Final.csv'
df1 = pd.read_csv('../../Data/' + sStockId + '.csv')
df2 = pd.read_csv('../../Data/' + sFileName + '.csv')
result = pd.merge(df1, df2, on='日期')
result.to_csv(sCSVFilePath, sep=',', encoding='utf-8-sig', index=False)

'''sql light
import pandas.io.sql as pd_sql
import sqlite3 as sql
conn = sql.connect("../data/twse.db")
df1 = pd.read_sql_query("select * from demo1;", conn)
df2 = pd.read_sql_query("select * from demo2;", conn)
存入SqLite
result.to_sql("demo3", conn, if_exists="replace")
'''

