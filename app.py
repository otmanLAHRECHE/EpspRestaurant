from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtCore import QSize, QPropertyAnimation
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect


WINDOW_SIZE = 0

class AppUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(AppUi, self).__init__()
        uic.loadUi("./user_interfaces/app.ui", self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))
        # Appy shadow to central widget
        self.centralwidget.setGraphicsEffect(self.shadow)

        self.main_header = self.findChild(QtWidgets.QFrame, "main_header")
        self.left_side_menu = self.findChild(QtWidgets.QFrame, "left_side_menu")

        self.left_menu_toggle_btn = self.findChild(QtWidgets.QPushButton, "left_menu_toggle_btn")
        self.left_menu_toggle_btn.setIcon(QIcon("./icons/cil-menu.png"))
        self.left_menu_toggle_btn.setIconSize(QSize(24, 24))

        self.restoreButton = self.findChild(QtWidgets.QPushButton, "restoreButton")
        self.restoreButton.setIcon(QIcon("./icons/maximize.png"))
        self.restoreButton.setIconSize(QSize(24, 24))

        self.minimizeButton = self.findChild(QtWidgets.QPushButton, "minimizeButton")
        self.minimizeButton.setIcon(QIcon("./icons/minus.png"))
        self.minimizeButton.setIconSize(QSize(24, 24))

        self.closeButton = self.findChild(QtWidgets.QPushButton, "closeButton")
        self.closeButton.setIcon(QIcon("./icons/x.png"))
        self.closeButton.setIconSize(QSize(24, 24))

        self.pushButton_4 = self.findChild(QtWidgets.QPushButton, "pushButton_4")
        self.pushButton_4.setIcon(QIcon("./icons/home.png"))
        self.pushButton_2.setMinimumSize(QSize(100, 0))
        self.pushButton_4.setIconSize(QSize(32, 32))

        self.pushButton_3 = self.findChild(QtWidgets.QPushButton, "pushButton_3")
        self.pushButton_3.setIcon(QIcon("./icons/log-out.png"))
        self.pushButton_3.setIconSize(QSize(32, 32))

        self.pushButton = self.findChild(QtWidgets.QPushButton, "pushButton")
        self.pushButton.setIcon(QIcon("./icons/log-in.png"))
        self.pushButton.setIconSize(QSize(32, 32))

        self.pushButton_5 = self.findChild(QtWidgets.QPushButton, "pushButton_5")
        self.pushButton_5.setIcon(QIcon("./icons/bar-chart-2.png"))
        self.pushButton_5.setIconSize(QSize(32, 32))

        self.pushButton_6 = self.findChild(QtWidgets.QPushButton, "pushButton_6")
        self.pushButton_6.setIcon(QIcon("./icons/calendar.png"))
        self.pushButton_6.setIconSize(QSize(32, 32))

        self.pushButton_2 = self.findChild(QtWidgets.QPushButton, "pushButton_2")
        self.pushButton_2.setIcon(QIcon("./icons/settings.png"))
        self.pushButton_2.setIconSize(QSize(32, 32))

        self.minimizeButton.clicked.connect(lambda: self.showMinimized())
        # Close window
        self.closeButton.clicked.connect(lambda: self.close())
        # Restore/Maximize window
        self.restoreButton.clicked.connect(lambda: self.restore_or_maximize_window())

        def moveWindow(e):
            if self.isMaximized() == False:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()

        self.main_header.mouseMoveEvent = moveWindow

        self.left_menu_toggle_btn.clicked.connect(lambda: self.slideLeftMenu())

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def restore_or_maximize_window(self):
        global WINDOW_SIZE
        win_status = WINDOW_SIZE

        if win_status == 0:
            WINDOW_SIZE = 1
            self.showMaximized()
            self.restoreButton.setIcon(QtGui.QIcon("./icons/minimize.png"))  # Show minized icon
        else:
            WINDOW_SIZE = 0
            self.showNormal()
            self.restoreButton.setIcon(QtGui.QIcon("./icons/maximize.png"))  # Show maximize icon

    def slideLeftMenu(self):
        width = self.left_side_menu.width()

        # If minimized
        if width == 50:
            # Expand menu
            newWidth = 180
            self.pushButton_4.setText("معلومات عامة")
            self.pushButton_3.setText("التموين")
            self.pushButton.setText("المشتريات")
            self.pushButton_5.setText("إحصائيات")
            self.pushButton_6.setText("البرنامج اليومي")
            self.pushButton_2.setText("إعدادات  ")

        else:
            # Restore menu
            newWidth = 50
            self.pushButton_4.setText("ttttttttt")
            self.pushButton_3.setText("tttttttt")
            self.pushButton.setText("tttttttt")
            self.pushButton_5.setText("tttttttt")
            self.pushButton_6.setText("tttttttt")
            self.pushButton_2.setText(" tttttttttttttttttttttt")

        # Animate the transition
        self.animation = QPropertyAnimation(self.left_side_menu, b"minimumWidth")  # Animate minimumWidht
        self.animation.setDuration(250)
        self.animation.setStartValue(width)  # Start value is the current menu width
        self.animation.setEndValue(newWidth)  # end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
