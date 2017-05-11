# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'findandreplace.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):

    def __init__(self):
        self.text = "I have learned a great many things from participating in varsity football. " \
                "It has changed my entire outlook on and attitude toward life. " \
                "Before my freshman year at [high-school], I was shy, had low self-esteem and turned away from seemingly impossible challenges. " \
                "Football has altered all of these qualities. " \
                "On the first day of freshman practice, the team warmed up with a game of touch football. " \
                "The players were split up and the game began. " \
                "However, during the game, I noticed that I didn't run as hard as I could, nor did I try to evade my defender and get open. " \
                "The fact of the matter is that I really did not want to be thrown the ball. " \
                "I didn't want to be the one at fault if I dropped the ball and the play didn't succeed. " \
                "I did not want the responsibility of helping the team because I was too afraid of making a mistake. " \
                "That aspect of my character led the first years of my high school life. " \
                "I refrained from asking questions in class, afraid they might be considered too stupid or dumb by my classmates. " \
                "All the while, I went to practice and everyday, I went home physically and mentally exhausted."

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(20, 130, 111, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(140, 130, 111, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(130, 60, 104, 21))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(130, 90, 104, 21))
        self.textEdit_2.setObjectName("textEdit_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(130, 170, 104, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 50, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 90, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 130, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 190, 113, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 170, 59, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(18, 90, 91, 20))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.checkBox.setText(_translate("Form", "Case sensitive"))
        self.checkBox_2.setText(_translate("Form", "Whole words"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Form", "Literal text"))
        self.pushButton.setText(_translate("Form", "Find"))
        self.pushButton_2.setText(_translate("Form", "Replace"))
        self.pushButton_3.setText(_translate("Form", "Replace All"))
        self.pushButton_4.setText(_translate("Form", "Close"))
        self.label.setText(_translate("Form", "Syntax:"))
        self.label_2.setText(_translate("Form", "Find what:"))
        self.label_3.setText(_translate("Form", "Replace with:"))


    def replace(self):
        # replace only one word
        self.text = self.text.replace(self.findWhatLineEdit.text(), self.replaceWithLineEdit.text(), 1)
