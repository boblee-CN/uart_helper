import sys
import time

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QInputDialog, QFontDialog, \
    QColorDialog
from PyQt6.QtSerialPort import QSerialPortInfo
from PyQt6 import uic, QtGui
from PyQt6.QtCore import QThread, QTimer
import threading
from serial_thread import Serial_Qthread_function
import serialport  # ui界面代码
import serial.tools.list_ports


class SerialInit(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()
        self.Init_ComScan()
        # self.interface_face()
        print("主线程id:", threading.current_thread().ident)

        # 创建子线程
        self.Serial_QThread = QThread()
        self.Serial_QThread_Function = Serial_Qthread_function()
        self.Serial_QThread_Function.moveToThread(self.Serial_QThread)
        self.Serial_QThread.start()

        # connect连接槽函数
        self.SlotConnect_Init()

        # self.Serial_QThread_Function.signal_start_function.emit()

        # 串口定时扫描1秒1次
        self.time_scan = QTimer()
        self.time_scan.timeout.connect(self.Init_ComScan)
        self.time_scan.start(1000)

    def ui_init(self):
        self.ui = serialport.Ui_Mserialport()
        self.ui.setupUi(self)
        self.myPlainTextEdit = self.ui.ptesend
        self.myLineEdit = self.ui.lineEdit
        self.modelset = self.ui.comboBox_Modelselect.currentIndex()
        # hex还是字符串
        self.fontset = self.ui.comboBox_Fontset.currentIndex()
        self.port_name = []

    # 槽函数连接
    def SlotConnect_Init(self):
        # click连接
        self.ui.Button_send.clicked.connect(self.buttonsend)
        self.ui.Button_open.clicked.connect(self.buttonopen)
        self.ui.Button_close.clicked.connect(self.buttonclose)
        self.pushButton: QPushButton = self.ui.Button_colorselect
        self.pushButton.clicked.connect(self.selectColor)
        self.ui.Button_clear.clicked.connect(self.reiceve_clear)
        # signal信号槽函数连接
        self.Serial_QThread_Function.signal_Button_open.connect(self.Serial_QThread_Function.slot_Button_open)
        self.Serial_QThread_Function.signal_Button_close.connect(self.Serial_QThread_Function.slot_Button_close)
        # self.Serial_QThread_Function.signal_serial_receive.connect(self.Serial_QThread_Function.Serial_receive_data)
        self.Serial_QThread_Function.signal_update_textbrowser.connect(self.update_textbrowser)

    def Init_ComScan(self):
        # print(self.port_name)
        available_ports = QSerialPortInfo.availablePorts()
        new_ports = []
        for port in available_ports:
            new_ports.append(port.portName())
        # print(new_ports)
        if len(self.port_name) != len(new_ports):
            self.port_name = new_ports
            self.ui.comboBox_Portname.clear()
            self.ui.comboBox_Portname.addItems(self.port_name)
            print(self.port_name)

    def update_textbrowser(self, data):
        if data != '':
            self.ui.ptereceive.appendPlainText(data)

    def selectColor(self):  # 颜色选择
        self.color = QColorDialog.getColor()
        if self.color.isValid():
            # 刷新数据
            self.rgb = self.color.getRgb()
            self.length_set = self.ui.comboBox_Lengthset.text()
            if self.length_set == '':
                self.length_set = 0
            self.number_set = self.ui.comboBox_Numberset.text()
            if self.number_set == '':
                self.number_set = 0
            self.modelset = self.ui.comboBox_Modelselect.currentIndex()
            self.fontset = self.ui.comboBox_Fontset.currentIndex()
            self.sendstr = (
                f"0x48 0x06 0x00 0x0c  0x{format(self.modelset, 'x').zfill(2).upper()} 0x00 0x00 0x00 0x00 0x{format(self.rgb[0], 'x').zfill(2).upper()} 0x{format(self.rgb[1], 'x').zfill(2).upper()} 0x{format(self.rgb[2], 'x').zfill(2).upper()} 0x{format(int(self.length_set), 'x').zfill(4)[0:2].upper()} 0x{format(int(self.length_set), 'x').zfill(4)[2:4].upper()} 0x{format(int(self.number_set), 'x').zfill(4)[0:2].upper()} 0x{format(int(self.number_set), 'x').zfill(4)[2:4].upper()} ")
            # 模式选择显示   帧头 命令码 数据长度 数据（模式选择 亮度 色温 rgb 长度 数量） crc
            # if self.fontset == 1:
            #     self.myPlainTextEdit.setPlainText(self.sendstr)
            # else:
            #     self.myPlainTextEdit.setPlainText(self.sendstr)
            self.myPlainTextEdit.setStyleSheet(
                f"background-color: rgb({self.rgb[0]}, {self.rgb[1]}, {self.rgb[2]});")
            # CRC处理与显示
            # self.data_for_crc = self.ui.ptesend.toPlainText()
            # print(type(self.data_for_crc))
            self.crc16_ccitt_reverse(self.sendstr)
            # 数据帧显示在发送窗口
            self.myPlainTextEdit.setPlainText(
                f"{self.sendstr} 0x{self.crc_str[:2].upper()} 0x{self.crc_str[2:4].upper()}")

    def reiceve_clear(self):
        self.ui.ptereceive.clear()

    def buttonopen(self):
        self.set_parameter = {}
        self.set_parameter['comboBox_Portname'] = self.ui.comboBox_Portname.currentText()
        self.set_parameter['comboBox_Baud'] = self.ui.comboBox_Baud.currentText()
        self.set_parameter['comboBox_Stop'] = self.ui.comboBox_Stop.currentText()
        self.set_parameter['comboBox_Data'] = self.ui.comboBox_Data.currentText()
        self.set_parameter['comboBox_Check'] = self.ui.comboBox_Check.currentText()
        self.set_parameter['comboBox_fontset'] = self.ui.comboBox_Fontset.currentIndex()
        self.Serial_QThread_Function.signal_Button_open.emit(self.set_parameter)
        self.ui.Button_open.setEnabled(False)
        time.sleep(0.001)
        self.debug()

    def buttonclose(self):
        self.Serial_QThread_Function.signal_Button_close.emit()
        self.ui.Button_open.setEnabled(True)

    def buttonsend(self):
        # print(self.data)
        self.data_for_show = self.ui.ptesend.toPlainText()
        # print(self.data_for_show)
        self.Serial_QThread_Function.Serial_send_data(self.data_for_show)

    def crc16_ccitt_reverse(self, data):
        # CRC16-CCITT parameters
        POLY = 0x1021
        INIT = 0x0000
        XOROUT = 0x0000

        # Reverse bits in a byte
        def reverse_8bits(byte):
            # print(bin(byte))
            bits = bin(byte)[2:].zfill(8)
            reversed_8bits = bits[::-1]
            reversed_1byte = int(reversed_8bits, 2)
            return reversed_1byte

        def reverse_16bits(byte):
            bits = bin(byte)[2:].zfill(16)
            reversed_16bits = bits[::-1]
            reversed_2byte = int(reversed_16bits, 2)
            return reversed_2byte

        # Initialize CRC
        crc = INIT
        # 一整个str 到 变量为str的list
        bytes_data = data.split()
        for byte_str in bytes_data:
            byte = int(byte_str, 16)  # Convert hex string to integer
            byte = reverse_8bits(byte)  # Reverse bits in byte
            # print("byte:", hex(byte))
            crc ^= (byte << 8)
            # print("crc:", hex(crc))
            for _ in range(8):
                if crc & 0x8000:
                    crc = (crc << 1) ^ POLY
                else:
                    crc = (crc << 1)

            crc &= 0xFFFF

        # Reverse CRC before final XOR
        crc = reverse_16bits(crc)
        crc ^= XOROUT
        print("CRC16-CCITT:", hex(crc))
        self.crc_str = hex(crc)[2:].zfill(4).upper()
        print(self.crc_str)
        self.myLineEdit.setText(self.crc_str)

    def debug(self):
        if self.Serial_QThread_Function.send_SerialStatus() == 2:
            QMessageBox.warning(self, '串口状态', '串口打开失败/占用！', QMessageBox.StandardButton.Ok)
            self.ui.Button_open.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ui = uic.loadUi("./mserialport.ui")
    w = SerialInit()
    # selectColor()
    # print(a)
    w.show()
    sys.exit(app.exec())
