import pandas
import time
import json
import os
from PyQt5.QtCore import pyqtSignal, QThread


class Controller(QThread):
    df = pandas.DataFrame()

    def __init__(self, inModel):
        super().__init__()
        self.modelData = inModel
        self.configData = self.scanConfigFile()
        self.configData['colHelp'] = []  # Описание колонок
        self.configData['colName'] = []  # Название колонок
        self.configData['rowsName'] = []  # Строки
        for col in self.configData['column']:
            self.configData['colHelp'].append(col['colHelp'])
            self.configData['colName'].append(col['name'])
        for row in self.configData['rows']:
            self.configData['rowsName'].append(row['name'])
        # self.modelData.rowsName = self.configData['rowsName']
        self.modelData.colLabels = self.configData['colName']

    def run(self):
        while(1):
            self.set_data()
            time.sleep(10)

    def set_data(self):
        self.modelData.cached = []
        self.modelData.colLabels = []

        self.modelData.rowCount = len(self.configData['rows'])
        self.modelData.colCount = len(self.configData['column'])
        for col in self.configData['column']:
            self.modelData.colLabels.append(col['name'])
        for i in range(len(self.configData['rows'])):
            self.modelData.cached.append([])
            for j in range(len(self.configData['column'])):
                self.modelData.cached[i].append([])
        for index2, row in enumerate(self.configData['rows']):
            # Заполнение первой колонки именами
            self.modelData.cached[index2][0] = row['name']
            for index1, col in enumerate(self.configData['column']):
                if (col['name'] != 'name'):
                    self.modelData.cached[index2][index1] = self.scan_file(
                        row['path'] + "\\" + col['name'])
        print(self.modelData.colLabels)

    def scan_file(self, path):

        try:

            dir_list = [os.path.join(path, x) for x in os.listdir(path)]

            if dir_list:
                # Создадим список из путей к файлам и дат их создания.
                date_list = [[x, os.path.getctime(x)] for x in dir_list]

                # Отсортируем список по дате создания в обратном порядке
                sort_date_list = sorted(
                    date_list, key=lambda x: x[1], reverse=True)

                # Выведем первый элемент списка. Он и будет самым последним по дате
                return(sort_date_list[0][0])
            else:
                return "Not dir"

        except FileNotFoundError:
            return "Not dir"

    def get_table(self):
        self.set_data()
        return self.df, self.configData['colHelp']

    def scanConfigFile(self):
        with open("./config.json", "r") as read_file:
            data = json.load(read_file)
        return data
