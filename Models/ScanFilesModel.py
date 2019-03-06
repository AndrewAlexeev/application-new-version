from PyQt5 import QtGui, QtCore
import sys


class Model(QtCore.QAbstractTableModel):
    def __init__(self, parent):
        QtCore.QAbstractTableModel.__init__(self)
        self.gui = parent
        self.rowsName = []  # Название строк
        self.colLabels = [
            '1', '2', '3', '4', '5'
        ]  # Название колонок
        self.cached = [
            ['11', '12', '13', '14'],
            ['11', '12', '13', '14'],
            ['11', '12', '13', '14'],
            ['11', '12', '13', '14'],
            ['11', '12', '13', '14']
        ]  # Таблица
        self._mObservers = []  # Список наблюдателей

    def rowCount(self, parent):
        return len(self.cached)

    def columnCount(self, parent):
        return len(self.colLabels)

    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()
        elif role != QtCore.Qt.DisplayRole and role != QtCore.Qt.EditRole:
            return QtCore.QVariant()
        value = ''
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            value = self.cached[row][col]
        return QtCore.QVariant(value)

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self.colLabels[section])
        return QtCore.QVariant()
