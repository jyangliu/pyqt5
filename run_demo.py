import sys
import ui_demo

from PySide2.QtWidgets import QApplication, QMessageBox, QMainWindow

if __name__=='__main__':
    app = QApplication(sys.argv)
    #创建主窗口
    mainWindow = QMainWindow()
    ui = ui_demo.Ui_Form()
    #向主窗口上添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())