import time

import PyQt5
from PyQt5.QtCore import pyqtSignal, QThread

from database_operation import is_product_exist, add_new_product, get_product_id_by_name, add_new_stock, get_all_product


class ThreadLoadingApp(QThread):
    _signal = pyqtSignal(int)
    _signal_result = pyqtSignal(bool)

    def __init__(self):
        super(ThreadLoadingApp, self).__init__()

    def __del__(self):
        self.terminate()
        self.wait()

    def run(self):
        for i in range(100):
            self._signal.emit(i)
            #time.sleep(0.1)
        self._signal_result.emit(True)


class ThreadAddStock(QThread):
    _signal = pyqtSignal(int)
    _signal_result = pyqtSignal(bool)

    def __init__(self, name, type, qnt, unit):
        super(ThreadAddStock, self).__init__()
        self.name = name
        self.type = type
        self.qnt = qnt
        self.unit = unit

    def __del__(self):
        self.terminate()
        self.wait()

    def run(self):

        if is_product_exist(self.name):
            for i in range(100):
                self._signal.emit(i)
            self._signal_result.emit(False)
        else:
            add_new_product(self.name, self.type, self.unit)
            id = get_product_id_by_name(self.name)
            id = id[0]
            add_new_stock(id[0], self.qnt)
            for i in range(100):
                self._signal.emit(i)

            self._signal_result.emit(True)


class ThreadLoadStock(QThread):
    _signal = pyqtSignal(int)
    _signal_result = pyqtSignal(bool)

    def __init__(self, name, type, qnt, unit):
        super(ThreadAddStock, self).__init__()
        self.name = name
        self.type = type
        self.qnt = qnt
        self.unit = unit

    def __del__(self):
        self.terminate()
        self.wait()

    def run(self):
        meats = get_all_product("meat")
        foods = get_all_product("food")

        for i in range(100):
            self._signal.emit(i)

        self._signal_result.emit(True)

