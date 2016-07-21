#coding=utf-8
import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets
import win32clipboard
import win32con
import re

qtCreatorFile = "ClipboardFormater.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

def get_clipboard():
	win32clipboard.OpenClipboard()
	data = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()
	return data

def set_clipboard(text):
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardText(text)
	win32clipboard.CloseClipboard()

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.apply1_button.clicked.connect(self.Button1)
		self.apply2_button.clicked.connect(self.Button2)


	def focusInEvent(self, event):
		self.cbtext.setText('Got focus')

	def focusOutEvent(self, event):
		self.cbtext.setText('Lost focus')

	def Button1(self):
		string=get_clipboard()
		self.cbtext.setText(string)
		pattern=self.regex1.toPlainText()
		rep=self.replace1.toPlainText()
		pattern=re.compile(pattern)
		res = pattern.sub(rep,string)
		self.replaced_text.setText(res)
		set_clipboard(res)
	def Button2(self):
		string=get_clipboard()
		self.cbtext.setText(string)
		pattern=self.regex2.toPlainText()
		rep=self.replace2.toPlainText()
		pattern=re.compile(pattern)
		res = pattern.sub(rep,string)
		self.replaced_text.setText(res)


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())
