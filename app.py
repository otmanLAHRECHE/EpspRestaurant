from PyQt5 import QtWidgets, uic, Qt
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QCursor, QIcon


class AppUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(AppUi, self).__init__()
        uic.loadUi("./user_interfaces/app.ui", self)

        self.left_menu_toggle_btn = self.findChild(QtWidgets.QPushButton, "left_menu_toggle_btn")
        self.left_menu_toggle_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.left_menu_toggle_btn.setIcon(icon)
        self.left_menu_toggle_btn.setIconSize(QSize(24, 24))

        self.restoreButton = self.findChild(QtWidgets.QPushButton, "restoreButton")
        self.restoreButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.restoreButton.setIcon(QIcon("./icons/maximize.png"))
        self.restoreButton.setIconSize(QSize(24, 24))

        self.minimizeButton = self.findChild(QtWidgets.QPushButton, "minimizeButton")
        self.minimizeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimizeButton.setIcon(QIcon("./icons/minus.png"))
        self.minimizeButton.setIconSize(QSize(24, 24))

        self.closeButton = self.findChild(QtWidgets.QPushButton, "closeButton")
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.setIcon(QIcon("./icons/x.png"))
        self.closeButton.setIconSize(QSize(24, 24))


