"""
Пример передачи в сигнале различных типов данных
"""
import sys
import time
import threading
import pandas
from PyQt5  import QtCore
from PyQt5.QtCore  import QSize,Qt

from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QGridLayout, QPushButton ,QTableWidget,QTableWidgetItem,QAction

flag_exit = 0#Флаг выхода из приложения
def thread(my_func):
    """
    Запускает функцию в отдельном потоке
    """
    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs)
        my_thread.start()
    return wrapper
 
@thread
def processing(signal):
	i = 0
	while(flag_exit == 0):
		i=i+1
		res = [i,i+1,i+2]
		time.sleep(5)
		#res = ex.chek()
		print("qq");
		signal.emit(res)# Посылаем сигнал в котором передаём полученные данные
    #!/usr/bin/python3
# -*- coding: utf-8 -*-




class Example(QWidget):
	my_signal = QtCore.pyqtSignal(list, name='my_signal')
	grid = QGridLayout()
	colHelp = pandas.Series(['name!','col1!','col2!','col3!'])#Описание колонок

	def chek(self):
		column = pandas.Series(['name','col1','col2','col3'])#Колонки
		lines = pandas.Series(['Andrew','Nik','Alex'])#Индексы
		path = pandas.Series(['C:\\Users\\Andrew','C:\\Users\\Nik','C:\\Users\\Alex'])#Пути
		df = pandas.DataFrame()
		for index_ in lines.values:
			for col in column.values:
				df.loc[index_,col] = self.FindActFile(1)
		df['name'] = lines.values
		return df
		#print(df)
	def __init__(self):
		super().__init__()
		self.initUI()
	def FindActFile(self,a):
		return('path')
	def tableAssembly(self,df,table):#Сборка таблицы
		
		table.setColumnCount(len(df.columns))     # Устанавливаем три колонки
		table.setRowCount(len(df.index))        # и одну строку в таблице
        # Устанавливаем заголовки таблицы
		table.setHorizontalHeaderLabels(df.columns.values)
        # Устанавливаем всплывающие подсказки на заголовки
		for index,colHelp in enumerate(self.colHelp.values):
			table.horizontalHeaderItem(index).setToolTip(colHelp)
        # Устанавливаем выравнивание на заголовки
		for index,col in enumerate(df.columns):
			if index == 0:	
				table.horizontalHeaderItem(index).setTextAlignment(Qt.AlignLeft)
			elif index == len(df.columns):	
				table.horizontalHeaderItem(index).setTextAlignment(Qt.AlignLeft)
			else:	
				table.horizontalHeaderItem(index).setTextAlignment(Qt.AlignHCenter)
        # заполняем  строки
		for index,lin in enumerate(df.index):
				for index2,col in enumerate(df.columns):
					table.setItem(index, index2, QTableWidgetItem(str(df.loc[lin,col])))
        # делаем ресайз колонок по содержимому
		table.resizeColumnsToContents()

	def initUI(self):
		quit = QAction("Quit", self)#При выходе из приложения обрабатываем сигнал, чтобы выйти из потока
		quit.triggered.connect(self.closeEvent)
		self.setLayout(self.grid)
		table = QTableWidget(self)  # Создаём таблицу
		self.tableAssembly(table = table,df = self.chek())
		self.grid.addWidget(table, 0, 0)   # Добавляем таблицу в сетку
		# запускаем обработку данных
		processing(self.my_signal)
        # Обработчик сигнала
		self.my_signal.connect(self.mySignalHandler, QtCore.Qt.QueuedConnection)
		self.move(300, 150)
		self.setWindowTitle('current version')
		self.show()
	def mySignalHandler(self, data):  # Вызывается для обработки сигнала
		#grid = QGridLayout()
		table = QTableWidget(self)  # Создаём таблицу
		self.tableAssembly(table = table,df =self.chek())
		self.grid.addWidget(table, 0, 0)   # Добавляем таблицу в сетку

	def closeEvent(self, event):
		global flag_exit 
		flag_exit = 1
		event.accept()


if __name__ == '__main__':

	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())