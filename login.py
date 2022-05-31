from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QGraphicsDropShadowEffect, QMessageBox

import app
from database_operation import check_user


class LoginUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginUi, self).__init__()
        uic.loadUi("./user_interfaces/login.ui", self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))
        # Appy shadow to central widget
        self.centralwidget.setGraphicsEffect(self.shadow)


        self.username = self.findChild(QtWidgets.QLineEdit, "lineEdit")
        self.password = self.findChild(QtWidgets.QLineEdit, "lineEdit_2")

        self.login = self.findChild(QtWidgets.QPushButton, "pushButton")

        self.login.clicked.connect(self.login_event)


    def login_event(self):
        if self.username.text() == "" or self.password.text() == "":
            self.alert_("خطأ في إسم المستخدم أو كلمة المرور")
        else:
            check = check_user(self.username.text(), self.password.text())

            if check:
                self.next_page = app.AppUi()
                self.next_page.show()
                self.close()
            else:
                self.alert_("خطأ في إسم المستخدم أو كلمة المرور")
                self.username.setText("")
                self.password.setText("")



    def alert_(self, message):
        alert = QMessageBox()
        alert.setWindowTitle("alert")
        alert.setText(message)
        alert.exec_()





