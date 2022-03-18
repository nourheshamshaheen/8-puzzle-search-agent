import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
import resources
from collections import deque
from Game import Game

class App:
    def __init__(self):
        self.ui = self.loadUiWidget('mainwindow.ui')
        self.ui.show()

    def loadUiWidget(self, uifilename, parent=None):
        loader = QUiLoader()
        uifile = QFile(uifilename)
        uifile.open(QFile.ReadOnly)
        ui = loader.load(uifile, parent)
        uifile.close()
        return ui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = App()
    g = Game(a.ui)
    app.exec_()


