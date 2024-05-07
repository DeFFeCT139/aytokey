
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import win32gui, win32con, win32api
from pykeyboard import PyKeyboard
from string import ascii_letters
import ctypes, time
import keyboard


state = True

k = PyKeyboard()

listWindow = []
id = 1
def winEnumHandler( hwnd, ctx ):
    global id
    if win32gui.IsWindowVisible( hwnd ):
        if win32gui.GetWindowText( hwnd ) != '':
            listWindow.append( [ id,win32gui.GetWindowText( hwnd )])
            id = id + 1

def mas():
    global id, listWindow
    listWindow = []
    id = 1
    win32gui.EnumWindows( winEnumHandler, None )
    return listWindow

mas()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout.addWidget(self.doubleSpinBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        for item in listWindow:
            self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_8.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(self.tab)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_10.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_9.addWidget(self.textEdit)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_7.addWidget(self.tabWidget)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.get_function()
        self.setRu()
        self.setleng()
        self.get_layout()
        keyboard.add_hotkey('ctrl+alt+x', lambda: self.on_ctrl_alt_x_press())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Автовводер 3008 или лучшее приложение созданое худшим кодером в мире"))
        self.label_2.setText(_translate("MainWindow", "Настройки"))
        self.label.setText(_translate("MainWindow", "Скорость печати"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Выбор окна для ввода текста"))
        for item in listWindow:
            self.comboBox.setItemText(item[0], _translate("MainWindow", item[1]))
        self.checkBox.setText(_translate("MainWindow", "Паузы и ошибки"))
        self.pushButton.setText(_translate("MainWindow", "Начать"))
        self.label_6.setText(_translate("MainWindow", "Для того что бы остановить печать нажмите комбинацию ctrl+alt+x"))
        self.label_3.setText(_translate("MainWindow", "Ввод"))
        self.pushButton_3.setText(_translate("MainWindow", "Обновить"))
        self.label_4.setText(_translate("MainWindow", "Ваедите путь к файлу с текстом или найдите его на пк"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Выбор файла"))
        self.label_5.setText(_translate("MainWindow", "Введите текст"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Ввод текста"))

    
    def get_function(self):
        self.toolButton.clicked.connect(lambda: self.openFile())
        self.pushButton.clicked.connect(lambda: self.gowWrite())
        self.pushButton_3.clicked.connect(lambda: self.newList())


    def openFile(self):
        res = QFileDialog.getOpenFileName( caption="Open txt file",directory= "/", filter="Text files (*.txt)")
        self.lineEdit.setText(res[0])

    def newList(self):
        _translate = QtCore.QCoreApplication.translate
        self.comboBox.clear()
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, _translate("MainWindow", "Выбор окна для ввода текста"))
        for index in mas():
            self.comboBox.addItem("")
            self.comboBox.setItemText(index[0], _translate("MainWindow", index[1]))

    def setRu(self):
        win32api.LoadKeyboardLayout("00000419",1)
        k.press_key(k.control_l_key)
        k.tap_key(k.shift_l_key)
        k.release_key(k.control_l_key)

    def setleng(self):
        win32api.LoadKeyboardLayout("00000409",1)
        k.press_key(k.control_l_key)
        k.tap_key(k.shift_l_key)
        k.release_key(k.control_l_key)
    
    def get_layout(self):
        u = ctypes.windll.LoadLibrary("user32.dll")
        pf = getattr(u, "GetKeyboardLayout")
        if hex(pf(0)) == '0x4190419':
            return 'ru'
        if hex(pf(0)) == '0x4090409':
            return 'en'
    
    def on_ctrl_alt_x_press(self):
        global state
        print('Программа завершена')
        state = False


    def gowWrite(self):
        global state
        if (self.tabWidget.currentIndex() == 0):
            self.textEdit.setText('')
        else:
            self.lineEdit.setText('')
        if ((self.comboBox.currentText() != "Выбор окна для ввода текста") & (self.doubleSpinBox.value() != 0.00) & ((self.textEdit.toPlainText() != "") | (self.lineEdit.text() != ""))):
            state = True
            inter = self.doubleSpinBox.value()
            hwnd = win32gui.FindWindow(None, self.comboBox.currentText())
            win32gui.ShowWindow(hwnd,win32con.SW_MAXIMIZE)
            win32gui.SetForegroundWindow(hwnd)
            text = ''
            if (self.tabWidget.currentIndex() == 0):
                text = ''
                file = open(self.lineEdit.text(), 'r')
                text = file.read()
                file.close()
                for i in text:
                    if state:
                        if (i.isalpha() == True):
                            if ((all(map(lambda c: c in ascii_letters, i)) == True)):
                                if (self.get_layout() != 'en'):
                                    self.setleng()
                                    time.sleep(0.1)
                                    k.tap_key(i,n=1,interval=inter)
                                else:
                                    k.tap_key(i,n=1,interval=inter)
                            else:
                                if (self.get_layout() != 'ru'):
                                    self.setRu()
                                    time.sleep(0.1)
                                    k.tap_key(i,n=1,interval=inter)
                                else:
                                    k.tap_key(i,n=1,interval=inter)
                        else:
                            k.tap_key(i,n=1,interval=inter)
                    else:
                        break

            else:
                text = self.textEdit.toPlainText()
                for i in text:
                    if state:
                        if (i.isalpha() == True):
                            if ((all(map(lambda c: c in ascii_letters, i)) == True)):
                                if (self.get_layout() != 'en'):
                                    self.setleng()
                                    time.sleep(0.1)
                                    k.tap_key(i,n=1,interval=inter)
                                else:
                                    k.tap_key(i,n=1,interval=inter)
                            else:
                                if (self.get_layout() != 'ru'):
                                    self.setRu()
                                    time.sleep(0.1)
                                    k.tap_key(i,n=1,interval=inter)
                                else:
                                    k.tap_key(i,n=1,interval=inter)
                        else:
                            k.tap_key(i,n=1,interval=inter)
                    else:
                        break
                        
                        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
