import sys
import pandas


from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QGridLayout, QPushButton, QTableWidget, QTableWidgetItem, QAction
from View.AppGUI import Ui_MainWindow


class ScanFilesView(QMainWindow):
    grid = QGridLayout()

    def __init__(self):
        super().__init__()
        self.initUI()

    def tableAssembly(self, df, colhelp):  # Сборка таблицы
        table = QTableWidget(self)  # Создаём таблицу
        table.setColumnCount(len(df.columns))     # Устанавливаем три колонки
        table.setRowCount(len(df.index))        # и одну строку в таблице
        # Устанавливаем заголовки таблицы
        table.setHorizontalHeaderLabels(df.columns.values)
        # Устанавливаем всплывающие подсказки на заголовки
        for index, colHelp in enumerate(colhelp):
            table.horizontalHeaderItem(index).setToolTip(colHelp)
        # Устанавливаем выравнивание на заголовки
        for index, col in enumerate(df.columns):
            if index == 0:
                table.horizontalHeaderItem(
                    index).setTextAlignment(Qt.AlignLeft)
            elif index == len(df.columns):
                table.horizontalHeaderItem(
                    index).setTextAlignment(Qt.AlignLeft)
            else:
                table.horizontalHeaderItem(
                    index).setTextAlignment(Qt.AlignHCenter)
        # заполняем  строки
        for index, lin in enumerate(df.index):
            for index2, col in enumerate(df.columns):
                table.setItem(index, index2, QTableWidgetItem(
                    str(df.loc[lin, col])))
        # делаем ресайз колонок по содержимому
        table.resizeColumnsToContents()
        self.grid.addWidget(table, 0, 0)   # Добавляем таблицу в сетку

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.model = model.Model(self.ui.tableView)
        # self.Fl = Files.Files(self.model)
        # self.Fl.start()
        # При выходе из приложения обрабатываем сигнал, чтобы выйти из потока
        quit = QAction("Quit", self)
        quit.triggered.connect(self.closeEvent)
        # self.ui.tableView.setModel(self.model)
        # self.setCentralWidget(self.table)
        self.move(300, 150)
        self.setWindowTitle('ScanFiles')
        self.show()

    def closeEvent(self, event):
        event.accept()
