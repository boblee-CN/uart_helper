1,ui转python代码
pyuic6 -x test2.ui -o test2.py

2，输出exe可执行文件
 pyinstaller --paths D:\pythonprojects\pythonProject2\.venv\Lib\site-packages\PyQt6\Qt6\bin -F -w --icon=serial.ico main.py
