'''
Created on Feb 10, 2019

@author: blew
'''
# import pkg_resources

# import PyQt5.QtWidgets
import sys

from PyQt5 import QtWidgets 
# import MainWindow
# from accumod import *
from acomod import MainWindow

# from PyQt5.QtCore import pyqtSignal, pyqtSlot, QSettings
# import MainWindow
# import global_settings
# sys._excepthook = sys.excepthook
# def my_debug_message():
#     print("--- DEBUG MESSAGE ---")
# 
# class ExceptionHandler(QtCore.QObject):
# 
#     errorSignal = QtCore.pyqtSignal()
# 
#     def __init__(self):
#         super(ExceptionHandler, self).__init__()
# 
#     def handler(self, exctype, value, traceback):
#         self.errorSignal.emit()
#         sys._excepthook(exctype, value, traceback)
# exceptionHandler = ExceptionHandler()
# sys.excepthook = exceptionHandler.handler
sys._excepthook = sys.excepthook
def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)
sys.excepthook = exception_hook


# class Test(QtWidgets.QPushButton):
#     def __init__(self, parent=None):
#         QtWidgets.QWidget.__init__(self, parent)
#         self.setText("hello")
#         self.clicked.connect(self.buttonClicked)
# 
#     def buttonClicked(self):
#         print("clicked")
#         raise Exception("wow")
#     
# app=QtWidgets.QApplication(sys.argv)
# t=Test()
# t.show()
# try:
#     app.exec_()
# except:
#     print("exiting")

def main():
    app = QtWidgets.QApplication(sys.argv)
    progMainWindow = MainWindow.MainWindow()
#     mainWindow = MainWindow.MainWindow()
    progMainWindow.show()
    try:
        sys.exit(app.exec_())
    except:
        print("exiting")


if __name__ == '__main__':
    main()
    