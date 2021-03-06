from peewee import *
import datetime
class OSDate(Field):
	db_field = 'date'
	def db_value(self, value):
		if value == None:
			return None
		ret = datetime.date(value['year'], value['month'], value['day'])
		return ret
	def python_value(self, value):
		if value == None:
			return None
		ret = {'day': value.day, 'month': value.month, 'year': value.year}
		return ret