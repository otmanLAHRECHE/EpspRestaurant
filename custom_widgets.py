from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore


class ChoseProduct(QWidget):
    def __init__(self):
        super(ChoseProduct, self).__init__()

        layout = QtWidgets.QHBoxLayout()
        self.chose_product = QtWidgets.QComboBox()
        self.chose_product.setFixedWidth(160)
        self.chose_product.setFixedHeight(30)
        layout.addStretch(1)
        layout.addWidget(self.chose_product)

        self.setLayout(layout)


class ChoseProductQte(QWidget):
    def __init__(self):
        super(ChoseProductQte, self).__init__()

        layout = QtWidgets.QHBoxLayout()
        self.chose_product_qte = QtWidgets.QDoubleSpinBox()
        self.chose_product_qte.setFixedHeight(30)
        self.chose_product_qte.setFixedWidth(130)
        self.chose_product_qte.setMaximum(1000.00)

        layout.addStretch(1)
        layout.addWidget(self.chose_product_qte)

        self.setLayout(layout)

class ProductsList(QWidget):
    def __init__(self, products):
        super(ProductsList, self).__init__()

        layout = QtWidgets.QHBoxLayout()
        self.list_products = QtWidgets.QListWidget()
        self.list_products.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.list_products.setFixedWidth(320)
        for product in products:
            cont = str(product[1]) + " :" + product[0]
            self.list_products.addItem(cont)
            print(cont)


        layout.addStretch(1)
        layout.addWidget(self.list_products)

        self.setLayout(layout)


