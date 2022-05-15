from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtCore import QSize, QPropertyAnimation, QDate
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QMessageBox, QTableWidgetItem, qApp, QCompleter

from dialogs import Add_new_stock, Threading_loading, Add_new_fb, Add_new_commande
from threads import ThreadAddStock, ThreadLoadStock, ThreadUpdateStock, ThreadSearchStock, ThreadAddFourBen, \
    ThreadUpdateFourBen, ThreadLoadFourBen, ThreadDeleteFourBen, ThreadCommandDialog, ThreadAddBonCommande, ThreadLoadCommande, \
    ThreadCommandDialogToUpdate, ThreadUpdateBonCommande
from custom_widgets import ProductsList, Check


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
        self.pushButton_4.setIcon(QIcon("./icons/users.png"))
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

        ##################### home page initialisation :

        self.home_table_fourn = self.findChild(QtWidgets.QTableWidget, "tableWidget_3")
        self.home_table_ben = self.findChild(QtWidgets.QTableWidget, "tableWidget_4")
        self.home_four_add_button = self.findChild(QtWidgets.QPushButton, "pushButton_12")
        self.home_four_edit_button = self.findChild(QtWidgets.QPushButton, "pushButton_13")
        self.home_four_delete_button = self.findChild(QtWidgets.QPushButton, "pushButton_14")
        self.home_ben_add_button = self.findChild(QtWidgets.QPushButton, "pushButton_15")
        self.home_ben_edit_button = self.findChild(QtWidgets.QPushButton, "pushButton_16")
        self.home_ben_delete_button = self.findChild(QtWidgets.QPushButton, "pushButton_17")

        self.home_four_add_button.setIcon(QIcon("./icons/plus2.png"))
        self.home_four_edit_button.setIcon(QIcon("./icons/edit2.png"))
        self.home_four_delete_button.setIcon(QIcon("./icons/user-x.png"))
        self.home_ben_add_button.setIcon(QIcon("./icons/plus2.png"))
        self.home_ben_edit_button.setIcon(QIcon("./icons/edit2.png"))
        self.home_ben_delete_button.setIcon(QIcon("./icons/user-x.png"))

        self.home_table_fourn.hideColumn(0)
        self.home_table_fourn.setColumnWidth(1, 40)
        self.home_table_fourn.setColumnWidth(2, 300)

        self.home_table_ben.hideColumn(0)
        self.home_table_ben.setColumnWidth(1, 40)
        self.home_table_ben.setColumnWidth(2, 300)

        self.home_four_add_button.clicked.connect(self.home_four_add)
        self.home_four_edit_button.clicked.connect(self.home_four_edit)
        self.home_four_delete_button.clicked.connect(self.home_four_delete)

        self.home_ben_add_button.clicked.connect(self.home_ben_add)
        self.home_ben_edit_button.clicked.connect(self.home_ben_edit)
        self.home_ben_delete_button.clicked.connect(self.home_ben_delete)


        ##################### End home page initialisation



        ##################### commandes page initialisation :

        self.commandes_table = self.findChild(QtWidgets.QTableWidget, "tableWidget_5")
        self.add_commande_button = self.findChild(QtWidgets.QPushButton, "pushButton_18")
        self.add_commande_button.setIcon(QIcon("icons/plus2.png"))
        self.edit_commmande_button = self.findChild(QtWidgets.QPushButton, "pushButton_22")
        self.edit_commmande_button.setIcon(QIcon("icons/edit2.png"))
        self.delete_commande_button = self.findChild(QtWidgets.QPushButton, "pushButton_23")
        self.delete_commande_button.setIcon(QIcon("icons/trash.png"))
        self.filter_commande_button = self.findChild(QtWidgets.QPushButton, "pushButton_19")
        self.filter_commande_button.setIcon(QIcon("icons/filter.png"))
        self.reset_commande_buton = self.findChild(QtWidgets.QPushButton, "pushButton_21")
        self.reset_commande_buton.setIcon(QIcon("icons/refresh.png"))
        self.report_commande_button = self.findChild(QtWidgets.QPushButton, "pushButton_20")
        self.report_commande_button.setIcon(QIcon("icons/file-text.png"))

        self.commandes_table.setColumnWidth(0, 40)
        self.commandes_table.setColumnWidth(1, 200)
        self.commandes_table.setColumnWidth(2, 100)
        self.commandes_table.setColumnWidth(3, 100)
        self.commandes_table.setColumnWidth(4, 340)

        self.add_commande_button.clicked.connect(self.add_commande)
        self.edit_commmande_button.clicked.connect(self.edit_commande)
        self.delete_commande_button.clicked.connect(self.delete_commande)


        ##################### End commandes page initialisation



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
        self.stock_table_food.setColumnWidth(1, 40)
        self.stock_table_food.setColumnWidth(2, 200)
        self.stock_table_food.setColumnWidth(3, 150)
        self.stock_table_food.setColumnWidth(4, 150)

        self.stock_table_meat.hideColumn(0)
        self.stock_table_meat.setColumnWidth(1, 40)
        self.stock_table_meat.setColumnWidth(2, 160)
        self.stock_table_meat.setColumnWidth(3, 100)
        self.stock_table_meat.setColumnWidth(4, 100)

        self.stock_add_button.clicked.connect(self.add_stock)
        self.stock_edit_button.clicked.connect(self.edit_stock)
        self.stock_search_button.clicked.connect(self.search_stock)
        self.stock_reset_button.clicked.connect(self.reset_stock)

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

        self.load_fb()


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
            self.pushButton_4.setText("الممونين و المستفيدين")
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


        self.stock_search_field.setText("")

        self.dialog = Threading_loading()
        self.dialog.ttl.setText("إنتظر من فضلك")
        self.dialog.progress.setValue(0)
        self.dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.dialog.show()

        self.stock_table_food.setRowCount(0)
        self.stock_table_meat.setRowCount(0)



        self.thr = ThreadLoadStock()
        self.thr._signal.connect(self.signal_stock_load_accepted)
        self.thr._signal_list.connect(self.signal_stock_load_accepted)
        self.thr._signal_result.connect(self.signal_stock_load_accepted)
        self.thr._signal_auto_food.connect(self.stock_auto_complete)
        self.thr.start()

    def signal_stock_load_accepted(self, progress):
        if type(progress) == int:
            self.dialog.progress.setValue(progress)
        elif type(progress) == list:
            if progress[0] == "meat":
                self.stock_table_meat.insertRow(progress[1])
                self.stock_table_meat.setItem(progress[1], 0, QTableWidgetItem(str(progress[2])))
                check = Check()
                self.stock_table_meat.setCellWidget(progress[1], 1, check)
                self.stock_table_meat.setItem(progress[1], 2, QTableWidgetItem(str(progress[3])))
                self.stock_table_meat.setItem(progress[1], 3, QTableWidgetItem(str(progress[4])))
                self.stock_table_meat.setItem(progress[1], 4, QTableWidgetItem(str(progress[5])))
            else:
                self.stock_table_food.insertRow(progress[1])

                self.stock_table_food.setItem(progress[1], 0, QTableWidgetItem(str(progress[2])))
                check = Check()
                self.stock_table_food.setCellWidget(progress[1], 1, check)
                self.stock_table_food.setItem(progress[1], 2, QTableWidgetItem(str(progress[3])))
                self.stock_table_food.setItem(progress[1], 3, QTableWidgetItem(str(progress[4])))
                self.stock_table_food.setItem(progress[1], 4, QTableWidgetItem(str(progress[5])))
        else:
            self.dialog.progress.setValue(100)
            self.dialog.ttl.setText("إنتها بنجاح")
            self.dialog.close()

    def edit_stock(self):
        ch1 = 0
        ch2 = 0
        for row in range(self.stock_table_food.rowCount()):
            if self.stock_table_food.cellWidget(row, 1).check.isChecked():
                row_selected = row
                ch1 = ch1 + 1
        for row in range(self.stock_table_meat.rowCount()):
            if self.stock_table_meat.cellWidget(row, 1).check.isChecked():
                row_selected = row
                ch2 = ch2 + 1
        if (ch1 > 1 or ch1 == 0) and (ch2 > 1 or ch2 == 0):
            self.alert_("خطأ في الإختيار")
            for row in range(self.stock_table_food.rowCount()):
                self.stock_table_food.cellWidget(row, 1).check.setChecked(False)
            for row in range(self.stock_table_meat.rowCount()):
                self.stock_table_meat.cellWidget(row, 1).check.setChecked(False)
        elif ch1 ==1 and ch2 == 1:
            self.alert_("خطأ في الإختيار")
            for row in range(self.stock_table_food.rowCount()):
                self.stock_table_food.cellWidget(row, 1).check.setChecked(False)
            for row in range(self.stock_table_meat.rowCount()):
                self.stock_table_meat.cellWidget(row, 1).check.setChecked(False)

        else:
            if ch1 ==1 and ch2 == 0:
                id = self.stock_table_food.item(row_selected, 0).text()
                product_name = self.stock_table_food.item(row_selected, 2).text()
                qne = self.stock_table_food.item(row_selected, 3).text()
                unit = self.stock_table_food.item(row_selected, 4).text()
                i = 0
            elif ch1 ==0 and ch2 == 1:
                id = self.stock_table_meat.item(row_selected, 0).text()
                product_name = self.stock_table_meat.item(row_selected, 2).text()
                qne = self.stock_table_meat.item(row_selected, 3).text()
                unit = self.stock_table_meat.item(row_selected, 4).text()
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

                    if dialog.stock_type.currentIndex() == 0:
                        t = "food"
                    else:
                        t = "meat"

                    self.thr = ThreadUpdateStock(int(id), dialog.stock_name.text(), t, dialog.stock_qnt.value(), u)
                    self.thr._signal.connect(self.signal_stock_update_accepted)
                    self.thr._signal_result.connect(self.signal_stock_update_accepted)
                    self.thr.start()
                    dialog.close()
            else:
                for row in range(self.stock_table_food.rowCount()):
                    self.stock_table_food.cellWidget(row, 1).check.setChecked(False)
                for row in range(self.stock_table_meat.rowCount()):
                    self.stock_table_meat.cellWidget(row, 1).check.setChecked(False)



    def signal_stock_update_accepted(self, progress):
        if type(progress) == int:
            self.dialog.progress.setValue(progress)
        else:
            self.dialog.progress.setValue(100)
            self.dialog.ttl.setText("إنتها بنجاح")
            self.dialog.close()
            self.load_stock()


    def stock_auto_complete(self, progress):
        completer = QCompleter(progress)
        self.stock_search_field.setCompleter(completer)

    def search_stock(self):
        if self.stock_search_field.text() == "":
            message = "خطأ في الإدخال"
            self.alert_(message)
        else:
            self.dialog = Threading_loading()
            self.dialog.ttl.setText("إنتظر من فضلك")
            self.dialog.progress.setValue(0)
            self.dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            self.dialog.show()

            self.stock_table_food.setRowCount(0)

            self.thr = ThreadSearchStock(self.stock_search_field.text())
            self.thr._signal.connect(self.signal_stock_search_accepted)
            self.thr._signal_list.connect(self.signal_stock_search_accepted)
            self.thr._signal_result.connect(self.signal_stock_search_accepted)
            self.thr.start()

    def reset_stock(self):
        self.load_stock()

    def signal_stock_search_accepted(self, progress):
        if type(progress) == int:
            self.dialog.progress.setValue(progress)
        elif type(progress) == list:

            self.stock_table_food.insertRow(progress[1])

            self.stock_table_food.setItem(progress[1], 0, QTableWidgetItem(str(progress[2])))
            check = Check()
            self.stock_table_food.setCellWidget(progress[1], 1, check)
            self.stock_table_food.setItem(progress[1], 2, QTableWidgetItem(str(progress[3])))
            self.stock_table_food.setItem(progress[1], 3, QTableWidgetItem(str(progress[4])))
            self.stock_table_food.setItem(progress[1], 4, QTableWidgetItem(str(progress[5])))

        else:
            self.dialog.progress.setValue(100)
            self.dialog.ttl.setText("إنتها بنجاح")
            self.dialog.close()



    def home_four_add(self):
        dial = Add_new_fb()
        dial.setWindowTitle("إضافة ممون جديد")
        dial.ttl.setText("إضافة ممون جديد")
        dial.label.setText("إسم الممون")
        if dial.exec() == QtWidgets.QDialog.Accepted:
            if dial.fb_name.text() == "":
                message = "خطأ في إسم الممون"
                self.alert_(message)
            else:
                self.dialog = Threading_loading()
                self.dialog.ttl.setText("إنتظر من فضلك")
                self.dialog.progress.setValue(0)
                self.dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
                self.dialog.show()

                self.thr = ThreadAddFourBen(dial.fb_name.text(), "four")
                self.thr._signal.connect(self.signal_f_accepted)
                self.thr._signal_result.connect(self.signal_f_accepted)
                self.thr.start()

    def signal_f_accepted(self, progress):
        if type(progress) == int:
            self.dialog.progress.setValue(progress)
        else:
            if progress:
                self.dialog.ttl.setText("اضيف بنجاح")
                self.dialog.progress.setValue(100)
                self.dialog.close()
                self.load_fb()
            else:
                self.dialog.ttl.setText("خطأ")
                self.dialog.progress.setValue(100)
                self.dialog.close()
                message = "المخزون موجود سابقا"
                self.alert_(message)

    def home_four_edit(self):
        ch = 0
        for row in range(self.home_table_fourn.rowCount()):
            if self.home_table_fourn.cellWidget(row, 1).check.isChecked():
                row_selected = row
                ch = ch + 1
        if ch > 1 or ch == 0:
            self.alert_("إختر خانة من الخانات")
            for row in range(self.home_table_fourn.rowCount()):
                self.home_table_fourn.cellWidget(row, 1).check.setChecked(False)
        else:
            id = self.home_table_fourn.item(row_selected, 0).text()
            name = self.home_table_fourn.item(row_selected, 2).text()


            dialog = Add_new_fb()
            dialog.setWindowTitle("تغيير الممون")
            dialog.ttl.setText("تغيير الممون")
            dialog.label.setText("الإسم الجديد للممون")
            dialog.fb_name.setText(name)

            if dialog.exec() == QtWidgets.QDialog.Accepted:
                if dialog.fb_name.text() == "":
                    message = "خطأ في إسم الممون"
                    self.alert_(message)
                    dialog.close()
                else:
                    self.dialog = Threading_loading()
                    self.dialog.ttl.setText("إنتظر من فضلك")
                    self.dialog.progress.setValue(0)
                    self.dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
                    self.dialog.show()

                    self.thr = ThreadUpdateFourBen(int(id), dialog.fb_name.text())
                    self.thr._signal.connect(self.signal_fb_update_accepted)
                    self.thr._signal_result.connect(self.signal_fb_update_accepted)
                    self.thr.start()
                    dialog.close()
            else:
                for row in range(self.home_table_fourn.rowCount()):
                    self.home_table_fourn.cellWidget(row, 1).check.setChecked(False)


    def signal_fb_update_accepted(self, progress):
        if type(progress) == int:
            self.dialog.progress.setValue(progress)
        else:
            self.dialog.progress.setValue(100)
            self.dialog.ttl.setText("إنتها بنجاح")
            self.dialog.close()
            self.load_fb()


    def home_four_delete(self):
        ch = 0
        for row in range(self.home_table_fourn.rowCount()):
            if self.home_table_fourn.cellWidget(row, 1).check.isChecked():
                row_selected = row
                ch = ch + 1
        if ch > 1 or ch == 0:
            self.alert_("إختر خانة من الخانات")
            for row in range(self.home_table_fourn.rowCount()):
                self.home_table_fourn.cellWidget(row, 1).check.setChecked(False)
        else:
            id = self.home_table_fourn.item(row_selected, 0).text()
            self.stock_table_food.removeRow(row_selected)

            self.dialog = Threading_loading()
            self.dialog.ttl.setText("إنتظر من فضلك")
            self.dialog.progress.setValue(0)
            self.dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            self.dialog.show()

            self.thr = ThreadDeleteFourBen(int(id))
            self.thr._signal.connect(self.signal_fb_update_accepted)
            self.thr._signal_result.connect(self.signal_fb_update_accepted)
            self.thr.start()

    def home_ben_add(self):
        dial = Add_new_fb()
        dial.setWindowTitle("إضافة مستفيد جديد")
        dial.ttl.setText("إضافة مستفيد جديد")
        dial.label.setText("إسم المستفيد او المصلحة")
        if dial.exec() == QtWidgets.QDialog.Accepted:
            if dial.fb_name.text() == "":
                message = "خطأ في الإسم"
                self.alert_(message)
            else:
                self.dialog = Threading_loading()
                self.dialog.ttl.setText("إنتظر من فضلك")
                self.dialog.progress.setValue(0)
                self.dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
                self.dialog.show()

                self.thr = ThreadAddFourBen(dial.fb_name.text(), "ben")
                self.thr._signal.connect(self.signal_b_accepted)
                self.thr._signal_result.connect(self.signal_b_accepted)
                self.thr.start()

    def signal_b_accepted(self, progress):
        if type(progress) == int:
            self.dialog.progress.setValue(progress)
        else:
            if progress:
                self.dialog.ttl.setText("اضيف بنجاح")
                self.dialog.progress.setValue(100)
                self.dialog.close()
                self.load_fb()
            else:
                self.dialog.ttl.setText("خطأ")
                self.dialog.progress.setValue(100)
                self.dialog.close()
                message = "المستفيد موجود سابقا"
                self.alert_(message)

    def home_ben_edit(self):
        ch = 0
        for row in range(self.home_table_ben.rowCount()):
            if self.home_table_ben.cellWidget(row, 1).check.isChecked():
                row_selected = row
                ch = ch + 1
        if ch > 1 or ch == 0:
            self.alert_("selectioner just une travailleur")
            for row in range(self.home_table_ben.rowCount()):
                self.home_table_ben.cellWidget(row, 1).check.setChecked(False)
        else:
            id = self.home_table_ben.item(row_selected, 0).text()
            name = self.home_table_ben.item(row_selected, 2).text()


            dialog = Add_new_fb()
            dialog.setWindowTitle("تغيير المستفيد")
            dialog.ttl.setText("تغيير المستفيد")
            dialog.label.setText("الإسم الجديد للمستفيد")
            dialog.fb_name.setText(name)

            if dialog.exec() == QtWidgets.QDialog.Accepted:
                if dialog.fb_name.text() == "":
                    message = "خطأ في إسم المستفيد"
                    self.alert_(message)
                    dialog.close()
                else:
                    self.dialog = Threading_loading()
                    self.dialog.ttl.setText("إنتظر من فضلك")
                    self.dialog.progress.setValue(0)
                    self.dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
                    self.dialog.show()

                    self.thr = ThreadUpdateFourBen(int(id), dialog.fb_name.text())
                    self.thr._signal.connect(self.signal_fb_update_accepted)
                    self.thr._signal_result.connect(self.signal_fb_update_accepted)
                    self.thr.start()
                    dialog.close()
            else:
                for row in range(self.home_table_ben.rowCount()):
                    self.home_table_ben.cellWidget(row, 1).check.setChecked(False)


    def home_ben_delete(self):
        ch = 0
        for row in range(self.home_table_ben.rowCount()):
            if self.home_table_ben.cellWidget(row, 1).check.isChecked():
                row_selected = row
                ch = ch + 1
        if ch > 1 or ch == 0:
            self.alert_("selectioner just une travailleur")
            for row in range(self.home_table_ben.rowCount()):
                self.home_table_ben.cellWidget(row, 1).check.setChecked(False)
        else:
            id = self.home_table_ben.item(row_selected, 0).text()
            self.home_table_ben.removeRow(row_selected)

            self.dialog = Threading_loading()
            self.dialog.ttl.setText("إنتظر من فضلك")
            self.dialog.progress.setValue(0)
            self.dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            self.dialog.show()

            self.thr = ThreadDeleteFourBen(int(id))
            self.thr._signal.connect(self.signal_fb_update_accepted)
            self.thr._signal_result.connect(self.signal_fb_update_accepted)
            self.thr.start()


    def load_fb(self):
        self.dialog = Threading_loading()
        self.dialog.ttl.setText("إنتظر من فضلك")
        self.dialog.progress.setValue(0)
        self.dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.dialog.show()

        self.home_table_fourn.setRowCount(0)
        self.home_table_ben.setRowCount(0)

        self.thr = ThreadLoadFourBen()
        self.thr._signal.connect(self.signal_fb_load_accepted)
        self.thr._signal_list.connect(self.signal_fb_load_accepted)
        self.thr._signal_result.connect(self.signal_fb_load_accepted)
        self.thr.start()

    def signal_fb_load_accepted(self, progress):
        if type(progress) == int:
            self.dialog.progress.setValue(progress)
        elif type(progress) == list:
            if progress[0] == "four":
                self.home_table_fourn.insertRow(progress[1])
                self.home_table_fourn.setItem(progress[1], 0, QTableWidgetItem(str(progress[2])))
                chose = Check()
                self.home_table_fourn.setCellWidget(progress[1], 1, chose)
                self.home_table_fourn.setItem(progress[1], 2, QTableWidgetItem(str(progress[3])))
            else:
                self.home_table_ben.insertRow(progress[1])
                self.home_table_ben.setItem(progress[1], 0, QTableWidgetItem(str(progress[2])))
                chose = Check()
                self.home_table_ben.setCellWidget(progress[1], 1, chose)
                self.home_table_ben.setItem(progress[1], 2, QTableWidgetItem(str(progress[3])))

        else:
            self.dialog.progress.setValue(100)
            self.dialog.ttl.setText("إنتها بنجاح")
            self.dialog.close()


    def add_commande(self):

        self.dialog = Threading_loading()
        self.dialog.ttl.setText("إنتظر من فضلك")
        self.dialog.progress.setValue(0)
        self.dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.dialog.show()


        self.thr = ThreadCommandDialog()
        self.thr._signal.connect(self.signal_commande_dialog_load_accepted)
        self.thr._signal_list.connect(self.signal_commande_dialog_load_accepted)
        self.thr._signal_result.connect(self.signal_commande_dialog_load_accepted)
        self.thr.start()


    def signal_commande_dialog_load_accepted(self, progress):
        l = []

        if type(progress) == int:
            self.dialog.progress.setValue(progress)

        elif type(progress) == type(l) :
            if progress[0] == "four":
                progress.remove("four")
                self.f = progress
            elif progress[0] == "products":
                progress.remove("products")
                self.p = progress
            else:
                self.com_nbr = progress[1]
                self.com_nbr = self.com_nbr + 1
        elif type(progress) == bool:
            self.dialog.ttl.setText("إنتها بنجاح")
            self.dialog.progress.setValue(100)
            self.dialog.close()
            dialog = Add_new_commande(self.p, self.f, self.com_nbr)


            if dialog.exec() == QtWidgets.QDialog.Accepted:
                if dialog.commande_products_table.rowCount() == 0:
                    self.alert_("لا يوجد طلبات")
                elif dialog.commande_number.text() == "00":
                    self.alert_("خطأ في رقم الطلب")
                else:
                    error = False
                    product_list = []
                    for i in range(dialog.commande_products_table.rowCount()):
                        if dialog.commande_products_table.cellWidget(i, 1).chose_product.currentIndex() == 0 or dialog.commande_products_table.cellWidget(i, 2).chose_product_qte.value() == 0:
                            error = True
                        else:
                            list = [dialog.commande_products_table.cellWidget(i, 1).chose_product.currentText(), dialog.commande_products_table.cellWidget(i, 2).chose_product_qte.value()]
                            product_list.append(list)

                    if error:
                        self.alert_("خطأ في المطلوبات")
                    else:
                        self.dialog = Threading_loading()
                        self.dialog.ttl.setText("إنتظر من فضلك")
                        self.dialog.progress.setValue(0)
                        self.dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
                        self.dialog.show()

                        self.thr = ThreadAddBonCommande(dialog.commande_number.text(), dialog.commande_date.text(), dialog.commande_fournesseur.currentText(), product_list)
                        self.thr._signal.connect(self.signal_commande_add_accepted)
                        self.thr._signal_result.connect(self.signal_commande_add_accepted)
                        self.thr.start()

    def signal_commande_add_accepted(self, progress):
        if type(progress) == int:
            self.dialog.progress.setValue(progress)
        else:
            if progress == True:
                self.dialog.progress.setValue(100)
                self.dialog.ttl.setText("إنتها بنجاح")
                self.dialog.close()
                self.load_commandes()
            else:
                self.dialog.progress.setValue(100)
                self.dialog.ttl.setText("إنتها بنجاح")
                self.dialog.close()
                self.alert_("خطأ في الرقم")




    def load_commandes(self):

        self.dialog = Threading_loading()
        self.dialog.ttl.setText("إنتظر من فضلك")
        self.dialog.progress.setValue(0)
        self.dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.dialog.show()

        self.commandes_table.setRowCount(0)

        self.thr = ThreadLoadCommande()
        self.thr._signal.connect(self.commande_load_accepted)
        self.thr._signal_list.connect(self.commande_load_accepted)
        self.thr._signal_result.connect(self.commande_load_accepted)
        self.thr.start()


    def commande_load_accepted(self, progress):
        if type(progress) == int:
            self.dialog.progress.setValue(progress)
        elif type(progress) == list:
            self.commandes_table.insertRow(progress[0])
            if len(progress[4]) == 1 or len(progress[4]) == 2 or len(progress[4]) == 3:
                self.commandes_table.setRowHeight(progress[0], len(progress[4]) * 30)
            else:
                self.commandes_table.setRowHeight(progress[0], len(progress[4])*24)

            check = Check()

            self.commandes_table.setCellWidget(progress[0], 0, check)
            self.commandes_table.setItem(progress[0], 1, QTableWidgetItem(str(progress[1])))
            self.commandes_table.setItem(progress[0], 2, QTableWidgetItem(str(progress[2])))
            self.commandes_table.setItem(progress[0], 3, QTableWidgetItem(str(progress[3])))
            p_list = ProductsList(progress[4])
            self.commandes_table.setCellWidget(progress[0], 4, p_list)

        else:
            self.dialog.progress.setValue(100)
            self.dialog.ttl.setText("إنتها بنجاح")
            self.dialog.close()



    def edit_commande(self):
        ch = 0
        for row in range(self.commandes_table.rowCount()):
            if self.commandes_table.cellWidget(row, 0).check.isChecked():
                row_selected = row
                ch = ch + 1
        if ch > 1 or ch == 0:
            self.alert_("إختار طلب")
            for row in range(self.commandes_table.rowCount()):
                self.commandes_table.cellWidget(row, 0).check.setChecked(False)
        else:
            self.dialog = Threading_loading()
            self.dialog.ttl.setText("إنتظر من فضلك")
            self.dialog.progress.setValue(0)
            self.dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            self.dialog.show()

            self.thr = ThreadCommandDialogToUpdate(self.commandes_table.item(row_selected, 1).text())
            self.to_update_row = row_selected
            self.thr._signal.connect(self.signal_commande_dialog_load_to_update_accepted)
            self.thr._signal_list.connect(self.signal_commande_dialog_load_to_update_accepted)
            self.thr._signal_result.connect(self.signal_commande_dialog_load_to_update_accepted)
            self.thr.start()


    def signal_commande_dialog_load_to_update_accepted(self, progress):
        l = []
        if not type(progress) == int:
            print("progress", progress)

        if type(progress) == int:
            self.dialog.progress.setValue(progress)

        elif type(progress) == type(l):
            if progress[0] == "four":
                progress.remove("four")
                self.f = progress
            elif progress[0] == "products":
                progress.remove("products")
                self.p = progress
            else:
                self.oper = progress

        elif type(progress) == bool:
            self.dialog.ttl.setText("إنتها بنجاح")
            self.dialog.progress.setValue(100)
            self.dialog.close()
            dialog = Add_new_commande(self.p, self.f, self.commandes_table.item(self.to_update_row, 1).text())
            dialog.setWindowTitle("تعديل على طلب")
            dialog.commande_fournesseur.setCurrentText(self.commandes_table.item(self.to_update_row, 3).text())
            dt = self.commandes_table.item(self.to_update_row, 2).text()
            dt = dt.split("/")
            d = QDate(int(dt[2]), int(dt[1]), int(dt[0]))
            dialog.commande_date.setDate(d)
            for operation in self.oper:
                dialog.add_p_to_update(operation)

            if dialog.exec() == QtWidgets.QDialog.Accepted:
                if dialog.commande_products_table.rowCount() == 0:
                    self.alert_("لا يوجد طلبات")
                elif dialog.commande_number.text() == "00":
                    self.alert_("خطأ في رقم الطلب")
                else:
                    error = False
                    product_list = []
                    for i in range(dialog.commande_products_table.rowCount()):
                        if dialog.commande_products_table.cellWidget(i,1).chose_product.currentIndex() == 0 or dialog.commande_products_table.cellWidget(i, 2).chose_product_qte.value() == 0:
                            error = True
                        else:
                            list = [dialog.commande_products_table.cellWidget(i, 1).chose_product.currentText(),
                                    dialog.commande_products_table.cellWidget(i, 2).chose_product_qte.value()]
                            product_list.append(list)

                    if error:
                        self.alert_("خطأ في المطلوبات")
                    else:
                        self.dialog = Threading_loading()
                        self.dialog.ttl.setText("إنتظر من فضلك")
                        self.dialog.progress.setValue(0)
                        self.dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
                        self.dialog.show()

                        self.thr = ThreadUpdateBonCommande(dialog.commande_number.text(), dialog.commande_date.text(),
                                                        dialog.commande_fournesseur.currentText(), product_list)
                        self.thr._signal.connect(self.signal_commande_update_accepted)
                        self.thr._signal_result.connect(self.signal_commande_update_accepted)
                        self.thr.start()
            else:
                for row in range(self.commandes_table.rowCount()):
                    self.commandes_table.cellWidget(row, 0).check.setChecked(False)

    def signal_commande_update_accepted(self, progress):
        if type(progress) == int:
            self.dialog.progress.setValue(progress)
        elif type(progress) == bool:
            if progress:
                self.dialog.progress.setValue(100)
                self.dialog.ttl.setText("إنتها بنجاح")
                self.dialog.close()
                self.load_commandes()
            else:
                self.dialog.progress.setValue(100)
                self.dialog.ttl.setText("إنتها بنجاح")
                self.dialog.close()
                self.alert_("خطأ في رقم الطلب (الرقم موجود سابقا)")



    def delete_commande(self):
        print("ok")
        """
        if self.to_update_table == "commande":

        else:
            self.alert_("إختار طلب")
        """


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

        self.to_update_table = "non"
        self.load_fb()

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
        self.to_update_table = "non"

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
        self.to_update_table = "non"


        self.load_commandes()

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
        self.to_update_table = "non"

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
        self.to_update_table = "non"

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
        self.to_update_table = "non"

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
        self.to_update_table = "non"
