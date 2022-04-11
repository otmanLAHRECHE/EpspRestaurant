from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtCore import QSize, QPropertyAnimation
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QMessageBox, QTableWidgetItem, qApp

from dialogs import Add_new_stock, Threading_loading
from threads import ThreadAddStock, ThreadLoadStock, ThreadUpdateStock

WINDOW_SIZE = 0

class AppUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(AppUi, self).__init__()
        uic.loadUi("./user_interfaces/app.ui", self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.move(115, 20)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))
        self.to_update_table = "non"
        self.to_update_row = "non"

        # Appy shadow to central widget
        self.centralwidget.setGraphicsEffect(self.shadow)
        self.main_header = self.findChild(QtWidgets.QFrame, "main_header")
        self.left_side_menu = self.findChild(QtWidgets.QFrame, "left_side_menu")
        self.left_menu_toggle_btn = self.findChild(QtWidgets.QPushButton, "left_menu_toggle_btn")
        self.left_menu_toggle_btn.setIcon(QIcon("./icons/cil-menu.png"))
        self.left_menu_toggle_btn.setIconSize(QSize(24, 24))
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
        self.pushButton_7 = self.findChild(QtWidgets.QPushButton, "pushButton_7")
        self.pushButton_7.setIcon(QIcon("./icons/clipboard.png"))
        self.pushButton_7.setIconSize(QSize(32, 32))
        self.pushButton_6 = self.findChild(QtWidgets.QPushButton, "pushButton_6")
        self.pushButton_6.setIcon(QIcon("./icons/calendar.png"))
        self.pushButton_6.setIconSize(QSize(32, 32))
        self.pushButton_2 = self.findChild(QtWidgets.QPushButton, "pushButton_2")
        self.pushButton_2.setIcon(QIcon("./icons/settings.png"))
        self.pushButton_2.setIconSize(QSize(32, 32))
        self.fragment = self.findChild(QtWidgets.QStackedWidget, "stackedWidget")
        self.pushButton_4.setStyleSheet("""
                background-color: rgb(0, 92, 157);
                background-repeat: none;
                padding-left: 50px;
                background-position: center left;
                """)
        self.fragment.setCurrentIndex(0)

        self.minimizeButton.clicked.connect(self.showMinimized)
        self.closeButton.clicked.connect(self.close)

        ##################### Stock page initialisation :

        self.stock_table_food = self.findChild(QtWidgets.QTableWidget, "tableWidget")
        self.stock_table_meat = self.findChild(QtWidgets.QTableWidget, "tableWidget_2")
        self.stock_search_field = self.findChild(QtWidgets.QLineEdit, "lineEdit")
        self.stock_search_button = self.findChild(QtWidgets.QPushButton, "pushButton_8")
        self.stock_reset_button = self.findChild(QtWidgets.QPushButton, "pushButton_9")
        self.stock_add_button = self.findChild(QtWidgets.QPushButton, "pushButton_10")
        self.stock_edit_button = self.findChild(QtWidgets.QPushButton, "pushButton_11")
        self.stock_search_button.setIcon(QIcon("./icons/search.png"))
        self.stock_reset_button.setIcon(QIcon("./icons/refresh.png"))
        self.stock_add_button.setIcon(QIcon("./icons/plus.png"))
        self.stock_edit_button.setIcon(QIcon("./icons/edit.png"))

        self.stock_table_food.hideColumn(0)
        self.stock_table_food.setColumnWidth(1, 200)
        self.stock_table_food.setColumnWidth(2, 150)
        self.stock_table_food.setColumnWidth(3, 150)

        self.stock_table_meat.hideColumn(0)
        self.stock_table_meat.setColumnWidth(1, 160)
        self.stock_table_meat.setColumnWidth(2, 100)
        self.stock_table_meat.setColumnWidth(3, 100)

        self.stock_add_button.clicked.connect(self.add_stock)
        self.stock_edit_button.clicked.connect(self.edit_stock)

        ##################### End stock page initialisation

        
        self.pushButton_4.clicked.connect(self.h)
        self.pushButton_3.clicked.connect(self.sort)
        self.pushButton.clicked.connect(self.ent)
        self.pushButton_7.clicked.connect(self.sto)
        self.pushButton_5.clicked.connect(self.stat)
        self.pushButton_6.clicked.connect(self.prog)
        self.pushButton_2.clicked.connect(self.sett)

        def moveWindow(e):
            if self.isMaximized() == False:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()

        self.main_header.mouseMoveEvent = moveWindow

        self.left_menu_toggle_btn.clicked.connect(lambda: self.slideLeftMenu())


    def alert_(self, message):
        alert = QMessageBox()
        alert.setWindowTitle("alert")
        alert.setText(message)
        alert.exec_()

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
            self.pushButton_7.setText("المخزون")
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
            self.pushButton_7.setText("tttttttt")
            self.pushButton_2.setText(" tttttttttttttttttttttt")

        # Animate the transition
        self.animation = QPropertyAnimation(self.left_side_menu, b"minimumWidth")  # Animate minimumWidht
        self.animation.setDuration(250)
        self.animation.setStartValue(width)  # Start value is the current menu width
        self.animation.setEndValue(newWidth)  # end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


    def add_stock(self):
        dialog_add_stock = Add_new_stock()
        if dialog_add_stock.exec() == QtWidgets.QDialog.Accepted:
            if dialog_add_stock.stock_name.text() == "":
                message = "خطأ في إسم المخزون"
                self.alert_(message)
            else:
                self.dialog  = Threading_loading()
                self.dialog.ttl.setText("إنتظر من فضلك")
                self.dialog.progress.setValue(0)
                self.dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
                self.dialog.show()

                if dialog_add_stock.stock_type.currentIndex() == 0:
                    t = "food"
                else:
                    t = "meat"

                if dialog_add_stock.stock_unite.currentIndex() == 0:
                    u = "no_unit"
                else:
                    u = dialog_add_stock.stock_unite.currentText()

                self.thr = ThreadAddStock(dialog_add_stock.stock_name.text(), t, dialog_add_stock.stock_qnt.value(), u)
                self.thr._signal.connect(self.signal_stock_accepted)
                self.thr._signal_result.connect(self.signal_stock_accepted)
                self.thr.start()




    def edit_stock(self):
        self.dialog = Add_new_stock()
        self.dialog.show()


    def signal_stock_accepted(self, progress):
        if type(progress) == int:
            self.dialog.progress.setValue(progress)
        else:
            if progress:
                self.dialog.ttl.setText("اضيف بنجاح")
                self.dialog.progress.setValue(100)
                self.dialog.close()
                self.load_stock()
            else:
                self.dialog.ttl.setText("خطأ")
                self.dialog.progress.setValue(100)
                self.dialog.close()
                message = "المخزون موجود سابقا"
                self.alert_(message)

    def load_stock(self):

        self.stock_table_food.selectionModel().selectionChanged.connect(self.food_selected)
        self.stock_table_meat.selectionModel().selectionChanged.connect(self.meat_selected)

        self.dialog = Threading_loading()
        self.dialog.ttl.setText("إنتظر من فضلك")
        self.dialog.progress.setValue(0)
        self.dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.dialog.show()

        self.thr = ThreadLoadStock()
        self.thr._signal.connect(self.signal_stock_load_accepted)
        self.thr._signal_list.connect(self.signal_stock_load_accepted)
        self.thr._signal_result.connect(self.signal_stock_load_accepted)
        self.thr.start()

    def signal_stock_load_accepted(self, progress):
        if type(progress) == int:
            self.dialog.progress.setValue(progress)
        elif type(progress) == list:
            if progress[0] == "meat":
                self.stock_table_meat.setItem(progress[1], 0, QTableWidgetItem(str(progress[2])))
                self.stock_table_meat.setItem(progress[1], 1, QTableWidgetItem(str(progress[3])))
                self.stock_table_meat.setItem(progress[1], 2, QTableWidgetItem(str(progress[4])))
                self.stock_table_meat.setItem(progress[1], 3, QTableWidgetItem(str(progress[5])))
            else:
                self.stock_table_food.setItem(progress[1], 0, QTableWidgetItem(str(progress[2])))
                self.stock_table_food.setItem(progress[1], 1, QTableWidgetItem(str(progress[3])))
                self.stock_table_food.setItem(progress[1], 2, QTableWidgetItem(str(progress[4])))
                self.stock_table_food.setItem(progress[1], 3, QTableWidgetItem(str(progress[5])))
        else:
            self.dialog.progress.setValue(100)
            self.dialog.ttl.setText("إنتها بنجاح")
            self.dialog.close()

    def edit_stock(self):
        if self.to_update_table == "non":
            message = "إختار مخزون"
            self.alert_(message)
        else:
            if self.to_update_table == "food":
                id = self.stock_table_food.item(self.to_update_row, 0).text()
                product_name = self.stock_table_food.item(self.to_update_row, 1).text()
                qne = self.stock_table_food.item(self.to_update_row, 2).text()
                unit = self.stock_table_food.item(self.to_update_row, 3).text()
                i = 0
            else:
                id = self.stock_table_food.item(self.to_update_row, 0).text()
                product_name = self.stock_table_meat.item(self.to_update_row, 1).text()
                qne = self.stock_table_meat.item(self.to_update_row, 2).text()
                unit = self.stock_table_meat.item(self.to_update_row, 3).text()
                i = 1


            dialog = Add_new_stock()
            dialog.setWindowTitle("تغيير مخزون")
            dialog.ttl.setText("تغيير مخزون")
            dialog.stock_name.setText(product_name)
            dialog.stock_type.setCurrentIndex(i)
            if unit == "kg":
                dialog.stock_unite.setCurrentIndex(1)
            elif unit == "litre":
                dialog.stock_unite.setCurrentIndex(2)
            else:
                dialog.stock_unite.setCurrentIndex(0)

            dialog.stock_qnt.setValue(float(str(qne)))




            if dialog.exec() == QtWidgets.QDialog.Accepted:
                if dialog.stock_name.text() == "":
                    message = "خطأ في إسم المخزون"
                    self.alert_(message)
                    dialog.close()
                else:
                    self.dialog = Threading_loading()
                    self.dialog.ttl.setText("إنتظر من فضلك")
                    self.dialog.progress.setValue(0)
                    self.dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
                    self.dialog.show()

                    if dialog.stock_unite.currentIndex() == 0:
                        u = "no_unit"
                    else:
                        u = dialog.stock_unite.currentText()

                    self.thr = ThreadUpdateStock(int(id), dialog.stock_name.text(), self.to_update_table, dialog.stock_qnt.value(), u)
                    self.thr._signal.connect(self.signal_stock_update_accepted)
                    self.thr._signal_result.connect(self.signal_stock_update_accepted)
                    self.thr.start()
                    dialog.close()

    def signal_stock_update_accepted(self, progress):
        if type(progress) == int:
            self.dialog.progress.setValue(progress)
        else:
            self.dialog.progress.setValue(100)
            self.dialog.ttl.setText("إنتها بنجاح")
            self.dialog.close()
            self.load_stock()


    def food_selected(self, selected, deselected):
        self.to_update_table = "food"
        self.to_update_row = selected.indexes()[0].row()

    def meat_selected(self, selected, deselected):
        self.to_update_table = "meat"
        self.to_update_row = selected.indexes()[0].row()

    def h(self):
        self.pushButton_4.setStyleSheet("""
        background-color: rgb(0, 92, 157);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;
        """)
        self.pushButton.setStyleSheet("""
        background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;
        """)
        self.pushButton_2.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;
        """)
        self.pushButton_3.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;
        """)
        self.pushButton_5.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;
        """)
        self.pushButton_6.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_7.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.fragment.setCurrentIndex(0)

    def sort(self):
        self.pushButton_3.setStyleSheet("""background-color: rgb(0, 92, 157);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_4.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_2.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_5.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_6.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_7.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.fragment.setCurrentIndex(1)

    def ent(self):
        self.pushButton.setStyleSheet("""background-color: rgb(0, 92, 157);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_2.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_5.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_6.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_7.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_3.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_4.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.fragment.setCurrentIndex(2)

    def sto(self):
        self.pushButton_7.setStyleSheet("""background-color: rgb(0, 92, 157);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_3.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_4.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_2.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_5.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_6.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.fragment.setCurrentIndex(3)

        self.load_stock()

    def stat(self):
        self.pushButton_5.setStyleSheet("""background-color: rgb(0, 92, 157);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_6.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_7.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_3.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_4.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_2.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.fragment.setCurrentIndex(4)

    def prog(self):
        self.pushButton_6.setStyleSheet("""background-color: rgb(0, 92, 157);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_7.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_3.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_4.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_2.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_5.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.fragment.setCurrentIndex(5)

    def sett(self):
        self.pushButton_2.setStyleSheet("""background-color: rgb(0, 92, 157);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_5.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_6.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_7.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_3.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton_4.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.pushButton.setStyleSheet("""background-color: rgb(0, 0, 0);
        background-repeat: none;
        padding-left: 50px;
        background-position: center left;""")
        self.fragment.setCurrentIndex(6)
