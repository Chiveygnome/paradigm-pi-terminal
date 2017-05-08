import sys
from PySide import QtCore, QtGui

"""
    This is the main window of the program.  As of 5/7/17, this is broken.
    None of the widgets are showing.  May be due to incorrect sizing, however
    I am unsure - Ernie
"""

class MainWidget(QtGui.QWidget):
    def __init__(self, *args):
        super(MainWidget, self).__init__(*args)
        self.layout = QtGui.QVBoxLayout()
        self.setupTextBox()
        self.setupButtons()
        self.show()

    def setupTextBox(self):
        self.box = QtGui.QPlainTextEdit()
        self.box.setLineWidth(80)
        self.box.setLineWrapMode(QtGui.QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.box.setTabChangesFocus(True)
        self.layout.addWidget(self.box)
        

    def setupButtons(self):
        self.sendButton = QtGui.QPushButton()
        self.sendButton.setText("Post Question")
        self.sendButton.setFixedSize(QtCore.QSize(100,50))
        self.sendButton.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.sendButton.adjustSize()
        self.layout.addWidget(self.sendButton)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()
    window.setCentralWidget(MainWidget())
    window.show()
    app.exec_()