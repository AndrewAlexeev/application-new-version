from PyQt5.QtWidgets import QApplication
import sys

from Controllers.ScanFilesController import Controller
from Models.ScanFilesModel import Model
from View.ScanFilesView import ScanFilesView


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScanFilesView()
    model = Model(ex.ui.tableView)
    ex.ui.tableView.setModel(model)
    controller = Controller(model)
    controller.start()
    sys.exit(app.exec_())
