from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TextGen(object):
    def setupUi(self, TextGen):
        TextGen.setObjectName("TextGen")
        TextGen.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(TextGen)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(43, 280, 711, 221))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 520, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 40, 491, 61))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setLineWidth(10)
        self.label.setMidLineWidth(10)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 80, 271, 71))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(40, 190, 711, 71))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 172, 221, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 262, 211, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 520, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        TextGen.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TextGen)
        self.statusbar.setObjectName("statusbar")
        TextGen.setStatusBar(self.statusbar)
        self.pushButton_2.clicked.connect(self.handleButton)

        self.retranslateUi(TextGen)
        QtCore.QMetaObject.connectSlotsByName(TextGen)

    def retranslateUi(self, TextGen):
        _translate = QtCore.QCoreApplication.translate
        TextGen.setWindowTitle(_translate("TextGen", "Text Gen"))
        self.pushButton.setText(_translate("TextGen", "Generate Text"))
        self.label.setText(_translate("TextGen", "Welcome to The Text Generator"))
        self.label_2.setText(_translate("TextGen", "Harness the Power of Machine Learning and LSTM network"))
        self.label_3.setText(_translate("TextGen", "Input a text here"))
        self.label_4.setText(_translate("TextGen", "Generated Text"))
        self.pushButton_2.setText(_translate("TextGen", "Cancel"))
   

    def handleButton(self):
        print ('hello'+self.textEdit_2.toPlainText())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TextGen = QtWidgets.QMainWindow()
    ui = Ui_TextGen()
    ui.setupUi(TextGen)
    TextGen.show()
    sys.exit(app.exec_())
