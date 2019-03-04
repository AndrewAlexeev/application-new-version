import pandas
import threading
import time
from PyQt5  import QtCore
from PyQt5.QtCore  import QSize,Qt
from PyQt5.QtCore import pyqtSignal,QThread
class Files(QThread):

	flag_exit = False
	df = pandas.DataFrame()
	colHelp = pandas.Series(['name!','col1!','col2!','col3!'])#Описание колонок - перенести в другой класс
	my_signal = pyqtSignal()
	def __init__(self):
		super().__init__()
	def run(self):
		while(not self.flag_exit):
			print("Work")
			self.my_signal.emit()
			time.sleep(5)
	pass

	def set_data(self):
		column = pandas.Series(['name', 'col1', 'col2', 'col3'])  # Колонки
		lines = pandas.Series(['Andrew', 'Nik', 'Alex'])  # Индексы
		path = pandas.Series(
			['C:\\Users\\Andrew', 'C:\\Users\\Nik', 'C:\\Users\\Alex'])  # Пути
		for index_ in lines.values:
			for col in column.values:
				self.df.loc[index_, col] = self.scan_file()
		self.df['name'] = lines.values
		pass

	def scan_file(self):
		return('path')
    
	def get_table(self):
		self.set_data()
		return self.df,self.colHelp