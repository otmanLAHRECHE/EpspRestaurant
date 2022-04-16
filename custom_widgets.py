from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget


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


