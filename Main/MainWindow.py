import sys
from PySide import QtCore, QtGui
import FileManager

"""
    This program requires the Pyside module (Python Qt wrapper) and
    Colorama for cross platform console color formatting.  If you are
    Reading this, then you are a dev and you should use pip, or installer
    of your choice and install them on your machine. - Ernie
    
    This is the main window of the program.  As of 5/7/17, this has a few bugs.
    The qtextbox doesn't move the cursor correctly, kind of breaking the text input.
"""
MAX_LENGTH = 140
class MainWidget(QtGui.QWidget):
    def __init__(self, logger, parent=None,*args, **kwargs):
        super(MainWidget, self).__init__(parent,*args, **kwargs)
        self.length = 0
        self._logger = logger
        layout = QtGui.QVBoxLayout()
        self.setupTextBox(layout)
        self.setupButtons(layout)
        self.setLayout(layout)
        self.show()
        self._logger.info("Gui set up complete")

    def setupTextBox(self, layout):
        logger.info("Setting up gui...")
        self.box = QtGui.QPlainTextEdit(parent=self)
        self.box.setLineWidth(80)
        self.box.setLineWrapMode(QtGui.QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.box.setFocus()
        # Need text box size here
        self.box.setTabChangesFocus(True)
        self.box.textChanged.connect(self.onTextChanged)
        layout.addWidget(self.box)
        

    def setupButtons(self, layout):
        hlayout = QtGui.QHBoxLayout()
        self.sendButton = QtGui.QPushButton(parent=self)
        self.sendButton.setText("Post Question")
        self.sendButton.setFixedSize(QtCore.QSize(100,50))
        self.sendButton.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.sendButton.adjustSize()
        hlayout.addWidget(self.sendButton)
        self.charsLeftLine = QtGui.QLineEdit()
        self.charsLeftLine.setReadOnly(True)
        self.charsLeftLine.setFixedSize(QtCore.QSize(100,50))
        self.charsLeftLine.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.charsLeftLine.setText("{0} characters left".format(MAX_LENGTH))
        self.charsLeftLine.setFrame(False)
        self.charsLeftLine.setBackgroundRole(QtGui.QPalette.ColorRole.Midlight)
        hlayout.addWidget(self.charsLeftLine)
        layout.addLayout(hlayout)

    # This is a slot for the signal textChanged in the QTextBox class
    def onTextChanged(self):
        length = len(self.box.toPlainText())
        diff = MAX_LENGTH - length
        if( length > MAX_LENGTH ):
            diff = 0
            self.box.setPlainText(self.box.toPlainText()[0:MAX_LENGTH])
            # why doesn't this statement work?
            # This is supposed to leave the text cursor at the end of the text if the text fills up, however it does not
            self.box.textCursor().setPosition(139, QtGui.QTextCursor.KeepAnchor)
            self._logger.debug("cursor pos: {0}".format(self.box.textCursor().position()))
        self.charsLeftLine.setText("{0} characters left".format(diff))

    # call twitter post call
    def onButtonPress(self):
        pass

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    logManager = FileManager.LogManager()
    # started including logging
    window = QtGui.QMainWindow()
    window.setCentralWidget(MainWidget())
    window.show()
    app.exec_()