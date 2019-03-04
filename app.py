import sys
import time
import threading
import pandas
import Files
from PyQt5  import QtCore
from PyQt5.QtCore  import QSize,Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QGridLayout, QPushButton ,QTableWidget,QTableWidgetItem,QAction


class App(QWidget):
	grid = QGridLayout()

	Fl = Files.Files();
	def __init__(self):
		super().__init__()
		self.initUI()
	
	def tableAssembly(self,df,colhelp):#Сборка таблицы
		print(df)
		table = QTableWidget(self)  # Создаём таблицу
		table.setColumnCount(len(df.columns))     # Устанавливаем три колонки
		table.setRowCount(len(df.index))        # и одну строку в таблице
        # Устанавливаем заголовки таблицы
		table.setHorizontalHeaderLabels(df.columns.values)
        # Устанавливаем всплывающие подсказки на заголовки
		for index,colHelp in enumerate(colhelp.values):
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
		self.grid.addWidget(table, 0, 0)   # Добавляем таблицу в сетку

	def initUI(self):
		# запускаем обработку данных
		self.Fl.start()
		# Обработчик сигнала
		self.Fl.my_signal.connect(self.mySignalHandler)
		quit = QAction("Quit", self)#При выходе из приложения обрабатываем сигнал, чтобы выйти из потока
		quit.triggered.connect(self.closeEvent)
		self.setLayout(self.grid)
		a,b=self.Fl.get_table()
		self.tableAssembly(df=a,colhelp=b)
		self.move(300, 150)
		self.setWindowTitle('current version')
		self.show()
	def mySignalHandler(self):  # Вызывается для обработки сигнала
		a,b=self.Fl.get_table()
		self.tableAssembly(df=a,colhelp=b)

	def closeEvent(self, event):
		# global flag_exit 
		# flag_exit = 1
		event.accept()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())