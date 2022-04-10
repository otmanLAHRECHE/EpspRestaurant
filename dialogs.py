from PyQt5 import QtWidgets, uic


class Add_new_stock(QtWidgets.QDialog):
    def __init__(self):
        super(Add_new_stock, self).__init__()
        uic.loadUi('./user_interfaces/add_new_stock.ui' , self)

        self.setWindowTitle("إضافة مخزون جديد")
        self.stock_name = self.findChild(QtWidgets.QLabel, "lineEdit")
        self.stock_type = self.findChild(QtWidgets.QComboBox, "comboBox")
        self.stock_qnt = self.findChild(QtWidgets.QDoubleSpinBox, "doubleSpinBox")
        self.stock_unite = self.findChild(QtWidgets.QComboBox, "comboBox_2")