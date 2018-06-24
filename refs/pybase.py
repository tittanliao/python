import pyodbc
import logging
import os

#private
def __get_dbo():
	list = []
	list.append('DRIVER='+__driver)
	list.append('PORT='+__port)
	list.append('SERVER='+__server)
	list.append('DATABASE='+__database)
	list.append('UID='+__username)
	list.append('PWD='+__password)
	cnxn = pyodbc.connect(';'.join(list))
	return cnxn

#dbo settings
__driver = '{ODBC Driver 13 for SQL Server}'
__port = '1433'
__server = 'aholic.cc'
__database = 'stock'
__username = 'sa'
__password = 'qweqwe1!qweqwe1!'
#logging settings
'''
logging.DEBUG,logging.INFO,logging.WARNING,logging.ERROR,logging.CRITICAL
'''
logpath = '/var/log/tittan/'
if not os.path.exists(logpath):
    os.makedirs(logpath)

logging.basicConfig(
	level=logging.INFO,
	format='[%(levelname)s] %(asctime)s - %(message)s',
	datefmt='%H:%M:%S',
	filename=logpath + 'trace.log',
	)

#public
dbo = __get_dbo()

class log:
	@classmethod
	def debug(self,s):
		logging.debug(s)
	@classmethod
	def info(self,s):
		logging.info(s)
	@classmethod
	def warning(self,s):
		logging.warning(s)
	@classmethod
	def error(self,s):
		logging.error(s)
	@classmethod
	def critical(self,s):
		logging.critical(s)
