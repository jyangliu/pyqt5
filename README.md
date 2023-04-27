# pyqt5

# 依赖
pip install pyside2

## 将qt designer生成的.ui文件转为.py文件
- Pyside2
```python
pyside2−uic main.ui > ui_main.py
```

- PyQt5
```python
pyuic5 main.ui > ui_main.py
```
转换之后的py文件需要转换成utf-8编码
