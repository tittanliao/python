import pyodbc
import logging
from logging.handlers import RotatingFileHandler
import datetime
import os

#private
def __get_dbo_mssql():
	list = []
	list.append('DRIVER='+__driver)
	list.append('PORT='+__port)
	list.append('SERVER='+__server)
	list.append('DATABASE='+__database)
	list.append('UID='+__username)
	list.append('PWD='+__password)
	cnxn = pyodbc.connect(';'.join(list))
	return cnxn

#var settings
__driver = '{ODBC Driver 13 for SQL Server}'
__port = '1433'
__server = 'aholic.cc'
__database = 'stock'
__username = 'sa'
__password = 'qweqwe1!qweqwe1!'

__log_type = logging.INFO
__log_path = '/var/log/tittan/'
__date8 = datetime.datetime.now().strftime("%Y%m%d")
#logging settings
'''
#logging.DEBUG,logging.INFO,logging.WARNING,logging.ERROR,logging.CRITICAL
logging.basicConfig(
	level=logging.INFO,
	format='[%(levelname)s] %(asctime)s - %(message)s',
	datefmt='%H:%M:%S',
	filename=logpath + 'trace.log',
	)
'''
if not os.path.exists(__log_path):
    os.makedirs(__log_path)

__log_formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')
__log_handler = RotatingFileHandler(__log_path+__date8+'_trace.log', mode='a', maxBytes=5*1024*1024, 
                                 backupCount=2, encoding=None, delay=0)
__log_handler.setFormatter(__log_formatter)
__log_handler.setLevel(__log_type)
logger = logging.getLogger('root')
logger.setLevel(__log_type)
logger.addHandler(__log_handler)

#public
dbo = __get_dbo_mssql()
date8 = __date8
caller = ''
class log:
	@classmethod
	def debug(self,s):
		logger.debug('['+caller+'] '+s)
	@classmethod
	def info(self,s):
		logger.info('['+caller+'] '+s)
	@classmethod
	def warning(self,s):
		logger.warning('['+caller+'] '+s)
	@classmethod
	def error(self,s):
		logger.error('['+caller+'] '+s)
	@classmethod
	def critical(self,s):
		logger.critical('['+caller+'] '+s)
