# pyqt5

## 依赖
pip install pyside2

## 将qt designer生成的.ui文件转为.py文件
- Pyside2
```python
pyside2−uic ui\demo.ui > ui_demo.py
```

- PyQt5
```python
pyuic5 ui\demo.ui > ui_demo.py
```
转换之后的py文件需要转换成utf-8编码

## 控件
- ComboBox:下拉表
- LineEdit:单行文本输入

## 信号(signal)和槽(slot)

信号是UI界面发生的事件，如点击button，此时UI会向外部发送信号，槽就是响应这些信号的函数。一个信号可以和多个槽绑定，一个槽可以拦截多个信号。


## 窗口类型
- QWidget
不确定窗口的用途，就使用QWidget。
- QDialog
对话窗口的基类。没有菜单栏、工具栏、状态栏。
- QMainWindow
可以包含菜单栏、工具栏、状态栏和标题栏，是最常见的窗口形式。
