# Form implementation generated from reading ui file 'mserialport.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Mserialport(object):
    def setupUi(self, Mserialport):
        Mserialport.setObjectName("Mserialport")
        Mserialport.resize(812, 779)
        self.gridLayout_6 = QtWidgets.QGridLayout(Mserialport)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.widget_3 = QtWidgets.QWidget(parent=Mserialport)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.widget_3)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Button_send = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.Button_send.setObjectName("Button_send")
        self.gridLayout_4.addWidget(self.Button_send, 2, 0, 1, 1)
        self.ptesend = QtWidgets.QPlainTextEdit(parent=self.groupBox_2)
        self.ptesend.setObjectName("ptesend")
        self.gridLayout_4.addWidget(self.ptesend, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 2, 0, 1, 2)
        self.le = QtWidgets.QLabel(parent=self.widget_3)
        self.le.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.le.setObjectName("le")
        self.gridLayout_5.addWidget(self.le, 3, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(parent=self.widget_3)
        self.groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ptereceive = QtWidgets.QPlainTextEdit(parent=self.groupBox)
        self.ptereceive.setObjectName("ptereceive")
        self.gridLayout_3.addWidget(self.ptereceive, 0, 0, 2, 1)
        self.widget_2 = QtWidgets.QWidget(parent=self.groupBox)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_Check = QtWidgets.QComboBox(parent=self.widget_2)
        self.comboBox_Check.setObjectName("comboBox_Check")
        self.comboBox_Check.addItem("")
        self.comboBox_Check.addItem("")
        self.comboBox_Check.addItem("")
        self.gridLayout.addWidget(self.comboBox_Check, 5, 3, 1, 1)
        self.comboBox_Portname = QtWidgets.QComboBox(parent=self.widget_2)
        self.comboBox_Portname.setObjectName("comboBox_Portname")
        self.comboBox_Portname.addItem("")
        self.comboBox_Portname.addItem("")
        self.comboBox_Portname.addItem("")
        self.comboBox_Portname.addItem("")
        self.comboBox_Portname.addItem("")
        self.gridLayout.addWidget(self.comboBox_Portname, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.comboBox_Numberset = QtWidgets.QLineEdit(parent=self.widget_2)
        self.comboBox_Numberset.setObjectName("comboBox_Numberset")
        self.gridLayout.addWidget(self.comboBox_Numberset, 14, 3, 1, 1)
        self.comboBox_Data = QtWidgets.QComboBox(parent=self.widget_2)
        self.comboBox_Data.setObjectName("comboBox_Data")
        self.comboBox_Data.addItem("")
        self.comboBox_Data.addItem("")
        self.comboBox_Data.addItem("")
        self.comboBox_Data.addItem("")
        self.gridLayout.addWidget(self.comboBox_Data, 4, 3, 1, 1)
        self.comboBox_Stop = QtWidgets.QComboBox(parent=self.widget_2)
        self.comboBox_Stop.setObjectName("comboBox_Stop")
        self.comboBox_Stop.addItem("")
        self.comboBox_Stop.addItem("")
        self.comboBox_Stop.addItem("")
        self.gridLayout.addWidget(self.comboBox_Stop, 6, 3, 1, 1)
        self.comboBox_Baud = QtWidgets.QComboBox(parent=self.widget_2)
        self.comboBox_Baud.setObjectName("comboBox_Baud")
        self.comboBox_Baud.addItem("")
        self.comboBox_Baud.addItem("")
        self.comboBox_Baud.addItem("")
        self.comboBox_Baud.addItem("")
        self.comboBox_Baud.addItem("")
        self.gridLayout.addWidget(self.comboBox_Baud, 3, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.widget_2)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.comboBox_Lengthset = QtWidgets.QLineEdit(parent=self.widget_2)
        self.comboBox_Lengthset.setObjectName("comboBox_Lengthset")
        self.gridLayout.addWidget(self.comboBox_Lengthset, 12, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 12, 0, 1, 1)
        self.Button_open = QtWidgets.QPushButton(parent=self.widget_2)
        self.Button_open.setCheckable(False)
        self.Button_open.setChecked(False)
        self.Button_open.setAutoDefault(False)
        self.Button_open.setFlat(False)
        self.Button_open.setObjectName("Button_open")
        self.gridLayout.addWidget(self.Button_open, 8, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.Button_close = QtWidgets.QPushButton(parent=self.widget_2)
        self.Button_close.setObjectName("Button_close")
        self.gridLayout.addWidget(self.Button_close, 8, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 14, 0, 1, 1)
        self.Button_colorselect = QtWidgets.QPushButton(parent=self.widget_2)
        self.Button_colorselect.setObjectName("Button_colorselect")
        self.gridLayout.addWidget(self.Button_colorselect, 15, 0, 1, 1)
        self.comboBox_Fontset = QtWidgets.QComboBox(parent=self.widget_2)
        self.comboBox_Fontset.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.comboBox_Fontset.setEditable(False)
        self.comboBox_Fontset.setObjectName("comboBox_Fontset")
        self.comboBox_Fontset.addItem("")
        self.comboBox_Fontset.addItem("")
        self.gridLayout.addWidget(self.comboBox_Fontset, 7, 3, 1, 1)
        self.comboBox_Modelselect = QtWidgets.QComboBox(parent=self.widget_2)
        self.comboBox_Modelselect.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.comboBox_Modelselect.setObjectName("comboBox_Modelselect")
        self.comboBox_Modelselect.addItem("")
        self.comboBox_Modelselect.addItem("")
        self.comboBox_Modelselect.addItem("")
        self.comboBox_Modelselect.addItem("")
        self.gridLayout.addWidget(self.comboBox_Modelselect, 15, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget_2)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 16, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 16, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout_3.addWidget(self.widget_2, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)
        self.Button_clear = QtWidgets.QPushButton(parent=self.groupBox)
        self.Button_clear.setObjectName("Button_clear")
        self.gridLayout_3.addWidget(self.Button_clear, 2, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 3)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setRowStretch(0, 3)
        self.gridLayout_5.addWidget(self.groupBox, 1, 1, 1, 1)
        self.gridLayout_5.setRowStretch(1, 3)
        self.gridLayout_5.setRowStretch(2, 1)
        self.gridLayout_6.addWidget(self.widget_3, 2, 0, 1, 1)

        self.retranslateUi(Mserialport)
        QtCore.QMetaObject.connectSlotsByName(Mserialport)

    def retranslateUi(self, Mserialport):
        _translate = QtCore.QCoreApplication.translate
        Mserialport.setWindowTitle(_translate("Mserialport", "Mserialport"))
        self.groupBox_2.setTitle(_translate("Mserialport", "发送"))
        self.Button_send.setText(_translate("Mserialport", "点击发送"))
        self.le.setText(_translate("Mserialport", "   version: llx v0.0   1,设置串口参数    2,打开串口     3,设置灯带长度与每米个数    4灯带模式选择   5选择颜色   6,点击发送"))
        self.groupBox.setTitle(_translate("Mserialport", "接收"))
        self.comboBox_Check.setItemText(0, _translate("Mserialport", "无"))
        self.comboBox_Check.setItemText(1, _translate("Mserialport", "奇校验"))
        self.comboBox_Check.setItemText(2, _translate("Mserialport", "偶校验"))
        self.comboBox_Portname.setItemText(0, _translate("Mserialport", "COM1"))
        self.comboBox_Portname.setItemText(1, _translate("Mserialport", "COM2"))
        self.comboBox_Portname.setItemText(2, _translate("Mserialport", "COM3"))
        self.comboBox_Portname.setItemText(3, _translate("Mserialport", "COM4"))
        self.comboBox_Portname.setItemText(4, _translate("Mserialport", "COM5"))
        self.label_4.setText(_translate("Mserialport", "校验位"))
        self.comboBox_Data.setItemText(0, _translate("Mserialport", "8"))
        self.comboBox_Data.setItemText(1, _translate("Mserialport", "7"))
        self.comboBox_Data.setItemText(2, _translate("Mserialport", "6"))
        self.comboBox_Data.setItemText(3, _translate("Mserialport", "5"))
        self.comboBox_Stop.setItemText(0, _translate("Mserialport", "1"))
        self.comboBox_Stop.setItemText(1, _translate("Mserialport", "1.5"))
        self.comboBox_Stop.setItemText(2, _translate("Mserialport", "2"))
        self.comboBox_Baud.setItemText(0, _translate("Mserialport", "9600"))
        self.comboBox_Baud.setItemText(1, _translate("Mserialport", "19200"))
        self.comboBox_Baud.setItemText(2, _translate("Mserialport", "38400"))
        self.comboBox_Baud.setItemText(3, _translate("Mserialport", "57600"))
        self.comboBox_Baud.setItemText(4, _translate("Mserialport", "115200"))
        self.label_3.setText(_translate("Mserialport", "数据位"))
        self.label.setText(_translate("Mserialport", "串口名"))
        self.label_5.setText(_translate("Mserialport", "停止位"))
        self.label_2.setText(_translate("Mserialport", "波特率"))
        self.label_6.setText(_translate("Mserialport", "灯带总长度/m"))
        self.Button_open.setText(_translate("Mserialport", "打开串口"))
        self.label_8.setText(_translate("Mserialport", "16进制/ASCII"))
        self.Button_close.setText(_translate("Mserialport", "关闭串口"))
        self.label_7.setText(_translate("Mserialport", "每米灯个数"))
        self.Button_colorselect.setText(_translate("Mserialport", "选择颜色"))
        self.comboBox_Fontset.setItemText(0, _translate("Mserialport", "Hex"))
        self.comboBox_Fontset.setItemText(1, _translate("Mserialport", "ASCII"))
        self.comboBox_Modelselect.setItemText(0, _translate("Mserialport", "颜色控制"))
        self.comboBox_Modelselect.setItemText(1, _translate("Mserialport", "呼吸灯"))
        self.comboBox_Modelselect.setItemText(2, _translate("Mserialport", "流水灯"))
        self.comboBox_Modelselect.setItemText(3, _translate("Mserialport", "跑马灯"))
        self.label_10.setText(_translate("Mserialport", "CRC校验结果(0x)"))
        self.label_9.setText(_translate("Mserialport", "格式:帧头:0x48,命令码:0x06,数据长度:0x000C(12),数据域(模式选择,亮度,色温,R,G,B,长度,个数),CRC"))
        self.Button_clear.setText(_translate("Mserialport", "清除接收"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mserialport = QtWidgets.QWidget()
    ui = Ui_Mserialport()
    ui.setupUi(Mserialport)
    Mserialport.show()
    sys.exit(app.exec())