from tittan_py import pybase as pyb
import pandas as pd
#get db
cnxn = pyb.dbo
sql = "SELECT id FROM isin WHERE market_type_detail IN ('股票','ETF')"
df_db = pd.read_sql(sql, cnxn)

for i, r in df_db.iterrows():
	print(r[0])
	pyb.log.warning(str(r[0]))
	break
