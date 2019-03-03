"""
Пример передачи в сигнале различных типов данных
"""
import sys
import time
import threading
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
		signal.emit(res)# Посылаем сигнал в котором передаём полученные данные
    #!/usr/bin/python3
# -*- coding: utf-8 -*-




class Example(QWidget):
	my_signal = QtCore.pyqtSignal(list, name='my_signal')
	grid = QGridLayout()
	
	def __init__(self):
		super().__init__()
		self.initUI()


	def initUI(self):
		quit = QAction("Quit", self)#При выходе из приложения обрабатываем сигнал, чтобы выйти из потока
		quit.triggered.connect(self.closeEvent)
		
		self.setLayout(self.grid)
		table = QTableWidget(self)  # Создаём таблицу
		table.setColumnCount(3)     # Устанавливаем три колонки
		table.setRowCount(1)        # и одну строку в таблице
        # Устанавливаем заголовки таблицы
		table.setHorizontalHeaderLabels(["Колонка 1", "Колонка 2", "Колонка 3"])
        # Устанавливаем всплывающие подсказки на заголовки
		table.horizontalHeaderItem(0).setToolTip("Column 1 ")
		table.horizontalHeaderItem(1).setToolTip("Column 2 ")
		table.horizontalHeaderItem(2).setToolTip("Column 3 ")
        # Устанавливаем выравнивание на заголовки
		table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
		table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
		table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        # заполняем первую строку
		table.setItem(0, 0, QTableWidgetItem("Text in column 1"))
		table.setItem(0, 1, QTableWidgetItem("Text in column 2"))
		table.setItem(0, 2, QTableWidgetItem("Text in column 3"))
 
        # делаем ресайз колонок по содержимому
		table.resizeColumnsToContents()
 
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
		table.setColumnCount(3)     # Устанавливаем три колонки
		table.setRowCount(1)        # и одну строку в таблице
		table.setHorizontalHeaderLabels(["Header 1", "Header 2", "Header 3"])
 
        # Устанавливаем всплывающие подсказки на заголовки
		table.horizontalHeaderItem(0).setToolTip("Column 2 ")
		table.horizontalHeaderItem(1).setToolTip("Column 2 ")
		table.horizontalHeaderItem(2).setToolTip("Column 3 ")
 
        # Устанавливаем выравнивание на заголовки
		table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
		table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
		table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
 
        # заполняем первую строку
		table.setItem(0, 0, QTableWidgetItem(str(data[0])))
		table.setItem(0, 1, QTableWidgetItem(str(data[1])))
		table.setItem(0, 2, QTableWidgetItem(str(data[2])))
 
        # делаем ресайз колонок по содержимому
		table.resizeColumnsToContents()
 
		self.grid.addWidget(table, 0, 0)   # Добавляем таблицу в сетку

	def closeEvent(self, event):
		global flag_exit 
		flag_exit = 1
		event.accept()


if __name__ == '__main__':

	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())