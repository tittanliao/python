'''select handler
'''
        
#with pandas
import pandas
import pyodbc
server = 'aholic.cc'
database = 'stock'
username = 'sa'
password = 'qweqwe1!qweqwe1!'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
sql = 'SELECT * FROM isin'
df_db = pandas.read_sql(sql, cnxn)
    
#normal way
import pyodbc
server = 'aholic.cc'
database = 'stock'
username = 'sa'
password = 'qweqwe1!qweqwe1!'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM isin")
row = cursor.fetchone()
print (str(row[0]) + " " + str(row[1]))
#rows = cursor.fetchall()
'''delete handler
'''
import pyodbc
server = 'aholic.cc'
database = 'stock'
username = 'sa'
password = 'qweqwe1!qweqwe1!'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("DELETE * FROM isin WHERE 1=1")
cnxn.commit()
#print(cursor.rowcount)

'''insert handler
'''
import pyodbc
import datetime
server = 'aholic.cc'
database = 'stock'
username = 'sa'
password = 'qweqwe1!qweqwe1!'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

id = '2344'
name = '華邦電'
isin_code = 'TW0002344009'
create_day = '19951018'
market_type = '上市'
market_type_detail = '股票'
industry_type = '半導體業'
update_time = datetime.datetime.now()
update_user = 'tittan'
    
sql='INSERT INTO isin(id,name,isin_code,create_day,market_type,market_type_detail,industry_type,update_time,update_user) VALUES (?,?,?,?,?,?,?,?,?)'
cursor.execute(sql,id,name,isin_code,create_day,market_type,market_type_detail,industry_type,update_time,update_user)
cnxn.commit()
#cursor.execute("insert into products(id, name) values ('pyodbc', 'awesome library')")