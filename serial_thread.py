import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt6.QtCore import QThread, pyqtSignal, QObject, QIODeviceBase, QIODevice, QTimer
from time import sleep
import threading
# from PyQt6.QtSerialPort import QSerialPort
import serial


class Serial_Qthread_function(QObject):
    signal_start_function = pyqtSignal()
    signal_Button_open = pyqtSignal(object)
    signal_Button_close = pyqtSignal()
    # signal_serial_receive = pyqtSignal()
    signal_update_textbrowser = pyqtSignal(object)

    def __init__(self, parent=None):
        super(Serial_Qthread_function, self).__init__(parent)
        print("初始化进程:", threading.current_thread().ident)
        self.state = 0  # 0：未打开，1：打开，2：占用/错误
        self.is_running = False
        self.serial1 = None
        # 开始调用网络的信号

    def slot_Button_open(self, parameter):
        print("串口线程id:", threading.current_thread().ident)
        # 为了后面的串口操作，先保存一下参数
        self.parameter_temple = parameter
        # 设置校验位
        setparity = {'无': 'N', '奇校验': 'O', '偶校验': 'E'}.get(parameter['comboBox_Check'])
        try:
            self.serial1 = serial.Serial(port=parameter['comboBox_Portname'],
                                         baudrate=int(parameter['comboBox_Baud']),
                                         bytesize=int(parameter['comboBox_Data']),
                                         parity=str(setparity),
                                         stopbits=int(parameter['comboBox_Stop']),
                                         timeout=1)
            if self.serial1.is_open:
                self.state = 1
                # self.signal_Button_open.emit(self.serial1)
                print("串口信息：", self.serial1)
                print("串口打开成功")
                self.is_running = True
                self.Serial_receive_data()
            else:
                self.state = 2
                print("串口打开失败")
        except serial.SerialException as e:
            print(f"{e}")  # 打印异常
            self.state = 2

    def slot_Button_close(self):
        if self.serial1 != None:
            self.state = 0
            self.serial1.close()
        # self.serial1 = None
        self.is_running = False
        print("串口关闭成功")

    def send_SerialStatus(self):
        return self.state

    # def SerialInit_function(self):
    #     print("串口线程id:", threading.current_thread().ident)

    def Serial_receive_data(self):
        self.read_timer = QTimer()
        self.read_timer.timeout.connect(self.start_reading)
        self.read_timer.start(100)

    def start_reading(self):
        if self.serial1 and self.is_running:
            if self.parameter_temple['comboBox_fontset'] == 1:  # ascii
                data = self.serial1.readline().decode('utf-8', errors='ignore').rstrip()
            # data = self.serial1.readline().decode('gbk', errors='ignore').rstrip()
            else:  # hex
                self.recieve_data_temple = self.serial1.readline().rstrip()  # recieve_data_temple 为bytes类型的str类型
                data = ' '.join([hex(byte)[2:].zfill(2) for byte in self.recieve_data_temple])  # bytes转16进制
            if data:
                self.signal_update_textbrowser.emit(data)

    def Serial_send_data(self, data):
        if self.state == 1:
            # if fontset == 0:  # hex发送
            send_data_temple = [int(x, 16) for x in data.split()]
            # data = data.encode('hex')
            self.serial1.write(send_data_temple)  # 接受list
            print(send_data_temple)
            # elif fontset == 1:  # ascii发送
            #     send_data_temple = [int(x, 16) for x in data.split()]
            #     self.serial1.write(send_data_temple)  # 接受list
            #     print(send_data_temple)
