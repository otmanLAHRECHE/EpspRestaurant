from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QGraphicsDropShadowEffect

from custom_widgets import ChoseProduct


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
    def __init__(self):
        super(Add_new_commande, self).__init__()
        uic.loadUi('./user_interfaces/add_new_commande.ui', self)

        self.ttl = self.findChild(QtWidgets.QLabel, "label_4")
        self.commande_number = self.findChild(QtWidgets.QSpinBox, "spinBox")
        self.commande_date = self.findChild(QtWidgets.QDateEdit, "dateEdit")
        self.commande_date.setDate(QtCore.QDate.currentDate())
        self.commande_fournesseur = self.findChild(QtWidgets.QComboBox, "comboBox")
        self.add_product = self.findChild(QtWidgets.QPushButton, "pushButton_18")
        self.add_product.setIcon(QIcon("./icons/plus2.png"))
        self.delete_product = self.findChild(QtWidgets.QPushButton, "pushButton_23")
        self.delete_product.setIcon(QIcon("./icons/trash.png"))
        self.commande_products_table = self.findChild(QtWidgets.QTableWidget, "tableWidget")

        self.commande_products_table.setColumnWidth(0, 200)
        self.commande_products_table.setColumnWidth(1, 200)
        self.commande_products_table.setColumnWidth(2, 100)

        self.add_product.clicked.connect(self.add_p)
        self.delete_product.clicked.connect(self.delete_p)

    def add_p(self):
        index = self.commande_products_table.rowCount()
        self.commande_products_table.insertRow(index)
        chose_product = ChoseProduct()
        self.commande_products_table.setCellWidget(index, 0, chose_product)

    def delete_p(self):
        print("delete")