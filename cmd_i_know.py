'''pandas handler
'''
import pandas as pd
cols = ['id','name','isin_code','create_day','market_type','market_type_detail','industry_type','update_time','update_user']
rows = []
rows.append(['2344', '華邦電', 'TW0002344009','19951018','上市','股票','半導體業','20180617 12:00:00','tittan'])
df1 = pd.DataFrame(rows, columns=cols)

'''while handler
'''
for x in range(10):
    if x==5:
        continue
    print x
    
'''if handler
''' 
if len(a) > 1:
    id = a[0]
    name = a[1]
else:
    a = row[0].split(' ')

'''date handler
'''
import datetime
now=datetime.datetime.now()
#'2018-06-18 09:44:43'
date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#20180618
date=datetime.datetime.now().strftime("%Y%m%d")
'''str handler
'''
a_date = '1962/2/9'.split("/")

'''array handler
'''
s = ''.join(a_date)

'''try handler
'''
try:  
    1 / 0 
except Exception as e: 
    print(e)

