from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(881, 772)
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 20, 69, 31))
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(110, 20, 581, 31))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(740, 20, 75, 31))
        self.toolButton = QToolButton(Form)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(270, 150, 37, 31))
        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(90, 150, 161, 31))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 101, 81, 31))
        self.calendarWidget = QCalendarWidget(Form)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(140, 260, 248, 197))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"HTTP\u63a5\u53e3\u6d4b\u8bd5", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"GET", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"POST", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"PUT", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"DELETE", None))

        self.textEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5730\u5740", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u53d1\u9001", None))
        self.toolButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

