import sys

# from PySide2.QtWidgets import QApplication, QMessageBox, QMainWindow, QDesktopWidget
# from PySide2.QtUiTools import QUiLoader
# from PySide2.QtGui import QIcon

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



class QLabel_test(QWidget):
    def __init__(self, parent=None):
        super(QLabel_test, self).__init__(parent)
        # self.initWindow()
        self.set_label()

    def initWindow(self):
        #设置主窗口的标题
        self.setWindowTitle('first main window')

        #设置窗口尺寸
        self.resize(400, 300)

        self.status = self.statusBar()

        self.status.showMessage('只存在5秒的消息', 5000)

        #窗口居中
        self.center()

        #设置退出按钮
        # self.button_exit = QPushButton('exit')
        #将信号与槽关联

        #设置窗口图标，只在windows下可以显示
        self.setWindowIcon(QIcon('./images/Dragon.jpg'))
    
    def center(self):
        #获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        #获取窗口坐标系
        size = self.geometry()
        #计算窗口居中坐标
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        #移动窗口
        self.move(newLeft, newTop)
    
    def set_label(self):
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)

        self.label1.setText("<font color=yellow>这是一个文本标签.</font>")
        self.label1.setAutoFillBackground(True)

        #设置lable1背景色
        patette = QPalette()
        patette.setColor(QPalette.Window, Qt.blue)
        self.label1.setPalette(patette)
        self.label1.setAlignment(Qt.AlignCenter)

        self.label2.setText("<a href='#'>欢迎使用python GUI程序</a>")

        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setToolTip('这是一个图片标签')
        self.label3.setPixmap(QPixmap("./images/Dragon.jpg"))

        #label4触发时，设置打开链接，不响应槽函数
        self.label4.setOpenExternalLinks(True)
        self.label4.setText("<a href='https://github.com/jyangliu/pyqt5'> 项目地址</a>")
        self.label4.setAlignment(Qt.AlignRight)
        self.label4.setToolTip('这是一个超级链接')

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.label3)
        vbox.addWidget(self.label4)

        #绑定槽函数
        self.label2.linkHovered.connect(self.linkHovered_label2)
        self.label4.linkActivated.connect(self.linkClicked_label4)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')
    
    def linkHovered_label2(self):
        print('当鼠标滑过label2标签时，触发事件')
    
    def linkClicked_label4(self):
        print('当鼠标单击label4标签时，触发事件')


class QLabelBuddy(QDialog):
    def __init__(self, parent=None):
        super(QLabelBuddy, self).__init__(parent)
        # self.initWindow()
        self.set_label()
    
    def set_label(self):
        self.setWindowTitle('QLabel与伙伴控件')

        nameLabel = QLabel('&Name', self)
        nameLineEdit = QLineEdit(self)

        #设置伙伴控件
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel('&PassWord', self)
        passwordLineEdit = QLineEdit(self)

        #设置伙伴控件
        passwordLabel.setBuddy(passwordLineEdit)

        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)
        mainLayout.addWidget(passwordLabel, 1, 0)
        mainLayout.addWidget(passwordLineEdit, 1, 1, 1, 2)

        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)


class QLineEditEchoMode(QWidget):
    def __init__(self, parent=None):
        super(QLineEditEchoMode, self).__init__(parent)
        # self.initWindow()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')

        formLayout = QFormLayout()

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        formLayout.addRow("Normal", normalLineEdit)
        formLayout.addRow("NoEcho", noEchoLineEdit)
        formLayout.addRow("Password", passwordLineEdit)
        formLayout.addRow("PasswordEchoOnEdit", passwordEchoOnEditLineEdit)

        #placeholdertext
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/Dragon.jpg'))
    # main = QLabel_test()
    # main = QLabelBuddy()
    main = QLineEditEchoMode()


    main.show()
    sys.exit(app.exec_())