from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, qApp

from custom_widgets import ChoseProduct, ChoseProductQte, Check
from database_operation import get_product_type_by_name


class Add_new_stock(QtWidgets.QDialog):
    def __init__(self):
        super(Add_new_stock, self).__init__()
        uic.loadUi('./user_interfaces/add_new_stock.ui', self)

        self.setWindowTitle("إضافة مخزون جديد")
        self.ttl = self.findChild(QtWidgets.QLabel, "label_4")
        self.stock_name = self.findChild(QtWidgets.QLineEdit, "lineEdit")
        self.stock_type = self.findChild(QtWidgets.QComboBox, "comboBox")
        self.stock_qnt = self.findChild(QtWidgets.QDoubleSpinBox, "doubleSpinBox")
        self.stock_unite = self.findChild(QtWidgets.QComboBox, "comboBox_2")

class Threading_loading(QtWidgets.QMainWindow):
    def __init__(self):
        super(Threading_loading, self).__init__()
        uic.loadUi('./user_interfaces/threading.ui', self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))
        # Appy shadow to central widget
        self.centralwidget.setGraphicsEffect(self.shadow)

        self.ttl = self.findChild(QtWidgets.QLabel, "loading_progress_status")
        self.progress = self.findChild(QtWidgets.QProgressBar, "my_progressBar")

class Add_new_fb(QtWidgets.QDialog):
    def __init__(self):
        super(Add_new_fb, self).__init__()
        uic.loadUi('./user_interfaces/add_new_fb.ui', self)

        self.ttl = self.findChild(QtWidgets.QLabel, "label_4")
        self.label = self.findChild(QtWidgets.QLabel, "label")
        self.fb_name = self.findChild(QtWidgets.QLineEdit, "lineEdit")

class Add_new_commande(QtWidgets.QDialog):
    def __init__(self, products, fourn, commande_number):
        super(Add_new_commande, self).__init__()
        uic.loadUi('./user_interfaces/add_new_commande.ui', self)


        self.pd = products
        self.fr = fourn
        self.ttl = self.findChild(QtWidgets.QLabel, "label_4")
        self.ttl_nbr = self.findChild(QtWidgets.QLabel, "label_3")
        self.ttl_fb = self.findChild(QtWidgets.QLabel, "label_2")
        self.commande_number = self.findChild(QtWidgets.QSpinBox, "spinBox")
        self.commande_number.setValue(int(commande_number))
        self.commande_date = self.findChild(QtWidgets.QDateEdit, "dateEdit")
        self.commande_date.setDate(QtCore.QDate.currentDate())
        self.commande_fournesseur = self.findChild(QtWidgets.QComboBox, "comboBox")
        self.add_product = self.findChild(QtWidgets.QPushButton, "pushButton_18")
        self.add_product.setIcon(QIcon("./icons/plus2.png"))
        self.delete_product = self.findChild(QtWidgets.QPushButton, "pushButton_23")
        self.delete_product.setIcon(QIcon("./icons/trash.png"))
        self.commande_products_table = self.findChild(QtWidgets.QTableWidget, "tableWidget")

        self.commande_products_table.setColumnWidth(0, 40)
        self.commande_products_table.setColumnWidth(1, 200)
        self.commande_products_table.setColumnWidth(2, 200)
        self.commande_products_table.setColumnWidth(3, 100)

        self.add_product.clicked.connect(self.add_p)
        self.delete_product.clicked.connect(self.delete_p)

        for f in self.fr:
            self.commande_fournesseur.addItem(f[0])

    def add_p(self):
        index = self.commande_products_table.rowCount()
        self.commande_products_table.insertRow(index)

        check = Check()
        self.commande_products_table.setCellWidget(index, 0, check)

        chose_product = ChoseProduct()
        chose_product.chose_product.currentTextChanged.connect(self.text_changed)
        chose_product.chose_product.addItem(" ")
        for p in self.pd:
            chose_product.chose_product.addItem(p[0])
        self.commande_products_table.setCellWidget(index, 1, chose_product)
        chose_product_qte = ChoseProductQte()
        self.commande_products_table.setCellWidget(index, 2, chose_product_qte)
        self.commande_products_table.setRowHeight(index, 50)

    def add_p_to_update(self, operations):
        index = self.commande_products_table.rowCount()
        self.commande_products_table.insertRow(index)

        check = Check()
        self.commande_products_table.setCellWidget(index, 0, check)

        chose_product = ChoseProduct()
        chose_product.chose_product.addItem(" ")
        for p in self.pd:
            chose_product.chose_product.addItem(p[0])
        chose_product.chose_product.setCurrentText(operations[0])
        chose_product.chose_product.currentTextChanged.connect(self.text_changed)
        self.commande_products_table.setCellWidget(index, 1, chose_product)
        chose_product_qte = ChoseProductQte()
        chose_product_qte.chose_product_qte.setValue(operations[1])
        self.commande_products_table.setCellWidget(index, 2, chose_product_qte)
        self.commande_products_table.setRowHeight(index, 50)
        if operations[2] == "no_unit":
            self.commande_products_table.setItem(index, 3, QtWidgets.QTableWidgetItem(""))
        else:
            self.commande_products_table.setItem(index, 3, QtWidgets.QTableWidgetItem(str(operations[2])))

    def text_changed(self, value):
        clickme = qApp.focusWidget()
        index = self.commande_products_table.indexAt(clickme.parent().pos())
        row = index.row()
        print(row)
        if not value == " ":
            unit = get_product_type_by_name(value)[0]
            if unit [0] == "kg":
                self.commande_products_table.setItem(row, 3, QtWidgets.QTableWidgetItem("kg"))
            elif unit [0] == "litres":
                self.commande_products_table.setItem(row, 3, QtWidgets.QTableWidgetItem("litres"))
            else:
                self.commande_products_table.setItem(row, 3, QtWidgets.QTableWidgetItem(""))

    def delete_p(self):
        ch = 0
        for row in range(self.commande_products_table.rowCount()):
            if self.commande_products_table.cellWidget(row, 0).check.isChecked():
                row_selected = row
                ch = ch + 1
        if ch > 1 or ch == 0:
            for row in range(self.commande_products_table.rowCount()):
                self.commande_products_table.cellWidget(row, 0).check.setChecked(False)
        else:
            self.commande_products_table.removeRow(row_selected)


class Filter_commande(QtWidgets.QDialog):
    def __init__(self, products, fourn, filter):
        super(Filter_commande, self).__init__()
        uic.loadUi('./user_interfaces/filter_commandes.ui', self)

        self.pd = products
        self.fr = fourn
        self.ttl = self.findChild(QtWidgets.QLabel, "label_4")
        self.ttl_2 = self.findChild(QtWidgets.QLabel, "label_7")
        self.ttl_3 = self.findChild(QtWidgets.QLabel, "label_3")
        self.ttl_ben = self.findChild(QtWidgets.QLabel, "label_8")
        self.date_type = self.findChild(QtWidgets.QComboBox, "comboBox")
        self.frm = self.findChild(QtWidgets.QLabel, "label")
        self.to = self.findChild(QtWidgets.QLabel, "label_2")
        self.fourn_label = self.findChild(QtWidgets.QLabel, "label_8")
        self.products_label = self.findChild(QtWidgets.QLabel, "label_9")
        self.commande_number_label = self.findChild(QtWidgets.QLabel, "label_3")
        self.date_before = self.findChild(QtWidgets.QDateEdit, "dateEdit")
        self.date_before.setDate(QtCore.QDate.currentDate())
        self.date_after = self.findChild(QtWidgets.QDateEdit, "dateEdit_2")
        self.date_after.setDate(QtCore.QDate.currentDate())
        self.order = self.findChild(QtWidgets.QComboBox, "comboBox_2")
        self.filter_type = self.findChild(QtWidgets.QComboBox, "comboBox_3")
        self.commande_number = self.findChild(QtWidgets.QSpinBox, "spinBox")
        self.fourn = self.findChild(QtWidgets.QComboBox, "comboBox_4")
        self.products = self.findChild(QtWidgets.QComboBox, "comboBox_5")
        self.add = self.findChild(QtWidgets.QPushButton, "pushButton")
        self.add.setIcon(QIcon("./icons/plus2.png"))
        self.empty = self.findChild(QtWidgets.QPushButton, "pushButton_2")
        self.empty.setIcon(QIcon("./icons/trash.png"))
        self.products_list = self.findChild(QtWidgets.QListWidget, "listWidget")

        self.date_type.currentIndexChanged.connect(self.date_type_changed)
        self.filter_type.currentIndexChanged.connect(self.filter_type_changed)

        self.add.clicked.connect(self.add_event)
        self.empty.clicked.connect(self.empty_event)

        self.frm.setText("قبل التاريخ:")

        self.frm.setEnabled(False)
        self.date_before.setEnabled(False)
        self.to.setEnabled(False)
        self.date_after.setEnabled(False)

        self.commande_number.setEnabled(False)
        self.commande_number_label.setEnabled(False)


        self.fourn.addItem("الكل")
        for f in self.fr:
            self.fourn.addItem(f[0])

        for p in self.pd:
            self.products.addItem(p[0])

    def date_type_changed(self, value):
        if value == 0:
            self.frm.setEnabled(False)
            self.date_before.setEnabled(False)
            self.to.setEnabled(False)
            self.date_after.setEnabled(False)
        elif value == 1:
            self.frm.setEnabled(True)
            self.date_before.setEnabled(True)
            self.frm.setText("قبل التاريخ:")
            self.to.setEnabled(False)
            self.date_after.setEnabled(False)
        elif value == 2:
            self.frm.setEnabled(True)
            self.date_before.setEnabled(True)
            self.frm.setText("بعد التاريخ:")
            self.to.setEnabled(False)
            self.date_after.setEnabled(False)
        elif value == 3:
            self.frm.setEnabled(True)
            self.date_before.setEnabled(True)
            self.frm.setText("بين التاريخ:")
            self.to.setEnabled(True)
            self.to.setText("و التاريخ")
            self.date_after.setEnabled(True)

    def filter_type_changed(self, value):
        if value == 0:
            self.commande_number.setEnabled(False)
            self.commande_number_label.setEnabled(False)

            self.fourn_label.setEnabled(True)
            self.products_label.setEnabled(True)
            self.fourn.setEnabled(True)
            self.products.setEnabled(True)
            self.products_list.setEnabled(True)
            self.add.setEnabled(True)
            self.empty.setEnabled(True)
        elif value == 1:
            self.commande_number.setEnabled(True)
            self.commande_number_label.setEnabled(True)

            self.fourn_label.setEnabled(False)
            self.products_label.setEnabled(False)
            self.fourn.setEnabled(False)
            self.products.setEnabled(False)
            self.products_list.setEnabled(False)
            self.add.setEnabled(False)
            self.empty.setEnabled(False)


    def add_event(self):
        self.products_list.addItem(self.products.currentText())

    def empty_event(self):
        self.products_list.clear()




