from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget


class ChoseProduct(QWidget):
    def __init__(self):
        super(ChoseProduct, self).__init__()

        layout = QtWidgets.QHBoxLayout()
        self.chose_product = QtWidgets.QComboBox()

        layout.addStretch(1)
        layout.addWidget(self.chose_product)

        self.setLayout(layout)


class ChoseProductQte(QWidget):
    def __init__(self):
        super(ChoseProductQte, self).__init__()

        layout = QtWidgets.QHBoxLayout()
        self.chose_product_qte = QtWidgets.QDoubleSpinBox

        layout.addStretch(1)
        layout.addWidget(self.chose_product_qte)

        self.setLayout(layout)


