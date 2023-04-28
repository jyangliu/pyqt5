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
### 控件通用方法
- setToolTip:为控件设置提示消息

### 基本控件使用
#### QLabel
- setAlignment():设置文本对齐方式
- setIndent():设置文本缩进
- text():获取文本内容
- setBuddy():设置伙伴关系
- setText(): 设置文本内容
- selectedText(): 返回所选择的字符
- setWordWarp():设置是否允许换行
##### QLabel常用信号
- 鼠标滑过QLabel控件触发：linkHovered()
- 鼠标单击QLabel控件触发：linkActivated()

#### QLineEdit
- 基本功能：输入单行文本
- EchoMode(回显模式)：四种回显模式，QLineEdit.Normal(正常显示)，QLineEdit.NoEcho(不显示到屏幕)，QLineEdit.Password(屏幕上显示点)，QLineEdit.PasswordEchoOnEdit(先正常显示，之后变成点)
- QLineEdit().setEchoMode 设置不同模式
##### 限制QLineEdit控件的输入（校验器）
- 整数校验器：QIntValidator
- 浮点校验器：QDoubleValidator
- 正则表达式校验器：QRegExpValidator
##### 通过掩码限制QLineEdit控件输入
- 限制输入IP地址样例：QLineEdit().setInputMask('000.000.000.000;_')

#### ComboBox:下拉表
#### LineEdit:单行文本输入

## 信号(signal)和槽(slot)

信号是UI界面发生的事件，如点击button，此时UI会向外部发送信号，槽就是响应这些信号的函数。一个信号可以和多个槽绑定，一个槽可以拦截多个信号。


## 窗口类型
- QWidget：
不确定窗口的用途，就使用QWidget。
- QDialog：
对话窗口的基类。没有菜单栏、工具栏、状态栏。
- QMainWindow：
可以包含菜单栏、工具栏、状态栏和标题栏，是最常见的窗口形式。
