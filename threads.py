import time

import PyQt5
from PyQt5.QtCore import pyqtSignal, QThread

from database_operation import is_product_exist, add_new_product, get_product_id_by_name, add_new_stock, \
    get_all_product, get_product_id_by_stock_id, update_product, update_stock


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
    _signal_list = pyqtSignal(list)
    _signal_result = pyqtSignal(bool)

    def __init__(self):
        super(ThreadLoadStock, self).__init__()
    def __del__(self):
        self.terminate()
        self.wait()

    def run(self):
        meats = get_all_product("meat")
        foods = get_all_product("food")

        for i in range(50):
            self._signal.emit(i)

        row = 0
        for meat in meats:
            list = []
            list.append("meat")
            list.append(row)
            list.append(meat[0])
            list.append(meat[1])
            list.append(meat[2])
            if meat[3] == "no_unit":
                list.append(" ")
            else:
                list.append(meat[3])

            self._signal_list.emit(list)
            row = row + 1

        row = 0
        for food in foods:
            list = []
            list.append("food")
            list.append(row)
            list.append(food[0])
            list.append(food[1])
            list.append(food[2])
            if food[3] == "no_unit":
                list.append(" ")
            else:
                list.append(food[3])

            self._signal_list.emit(list)
            row = row + 1

        for i in range(50, 100):
            self._signal.emit(i)

        self._signal_result.emit(True)


class ThreadUpdateStock(QThread):
    _signal = pyqtSignal(int)
    _signal_result = pyqtSignal(bool)

    def __init__(self, stock_id, name, type, qnt, unit):
        super(ThreadUpdateStock, self).__init__()
        self.name = name
        self.type = type
        self.qnt = qnt
        self.unit = unit
        self.stock_id = stock_id

    def __del__(self):
        self.terminate()
        self.wait()

    def run(self):

        for i in range(50):
            self._signal.emit(i)

        id = get_product_id_by_stock_id(self.stock_id)[0]
        print(id[0])
        print(self.name)
        print(self.type)
        print(self.unit)
        update_product(id[0], self.name, self.type, self.unit)
        update_stock(self.stock_id, self.qnt)

        for i in range(50, 100):
            self._signal.emit(i)

        self._signal_result.emit(True)

