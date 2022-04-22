import time

import PyQt5
from PyQt5.QtCore import pyqtSignal, QThread

from database_operation import is_product_exist, add_new_product, get_product_id_by_name, add_new_stock, \
    get_all_product, get_product_id_by_stock_id, update_product, update_stock, search_food, add_new_four_ben, \
    is_four_ben_exist, get_all_four_ben, update_four_ben, delete_four_ben, get_all_product_names_no_type, \
    get_all_four_ben_names, get_last_bon_commande_number, is_commande_number_exist, add_bon, get_fourn_ben_id_from_name, \
    add_operation, get_stock_qte_by_product_id, update_stock_by_commande, get_all_commande, get_operations_by_commande_id

from tools import forming_date, un_forming_date


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
    _signal_auto_food = pyqtSignal(list)
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


        list_auto_food = []

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
            list_auto_food.append(food[1])

            self._signal_list.emit(list)
            row = row + 1

        for i in range(50, 100):
            self._signal.emit(i)

        self._signal_auto_food.emit(list_auto_food)

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


class ThreadSearchStock(QThread):
    _signal = pyqtSignal(int)
    _signal_list = pyqtSignal(list)
    _signal_result = pyqtSignal(bool)

    def __init__(self, search_text):
        super(ThreadSearchStock, self).__init__()
        self.search_text = search_text

    def __del__(self):
        self.terminate()
        self.wait()

    def run(self):

        foods = search_food(self.search_text)

        for i in range(50):
            self._signal.emit(i)

        if foods:
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
        else:
            for i in range(50, 100):
                self._signal.emit(i)


            self._signal_result.emit(False)


class ThreadAddFourBen(QThread):
    _signal = pyqtSignal(int)
    _signal_result = pyqtSignal(bool)

    def __init__(self, name, type):
        super(ThreadAddFourBen, self).__init__()
        self.name = name
        self.type = type

    def __del__(self):
        self.terminate()
        self.wait()

    def run(self):

        if is_four_ben_exist(self.name):
            for i in range(100):
                self._signal.emit(i)
            self._signal_result.emit(False)
        else:
            add_new_four_ben(self.name, self.type)
            for i in range(100):
                self._signal.emit(i)

            self._signal_result.emit(True)


class ThreadLoadFourBen(QThread):
    _signal = pyqtSignal(int)
    _signal_list = pyqtSignal(list)
    _signal_result = pyqtSignal(bool)

    def __init__(self):
        super(ThreadLoadFourBen, self).__init__()
    def __del__(self):
        self.terminate()
        self.wait()

    def run(self):
        fours = get_all_four_ben("four")
        bens = get_all_four_ben("ben")

        for i in range(50):
            self._signal.emit(i)


        row = 0
        for four in fours:
            list = []
            list.append("four")
            list.append(row)
            list.append(four[0])
            list.append(four[1])

            self._signal_list.emit(list)
            row = row + 1

        row = 0
        for ben in bens:
            list = []
            list.append("ben")
            list.append(row)
            list.append(ben[0])
            list.append(ben[1])

            self._signal_list.emit(list)
            row = row + 1

        for i in range(50, 100):
            self._signal.emit(i)


        self._signal_result.emit(True)


class ThreadUpdateFourBen(QThread):
    _signal = pyqtSignal(int)
    _signal_result = pyqtSignal(bool)

    def __init__(self, id, name):
        super(ThreadUpdateFourBen, self).__init__()
        self.name = name
        self.id = id

    def __del__(self):
        self.terminate()
        self.wait()

    def run(self):

        for i in range(50):
            self._signal.emit(i)

        update_four_ben(self.id, self.name)

        for i in range(50, 100):
            self._signal.emit(i)

        self._signal_result.emit(True)


class ThreadDeleteFourBen(QThread):
    _signal = pyqtSignal(int)
    _signal_result = pyqtSignal(bool)

    def __init__(self, id):
        super(ThreadDeleteFourBen, self).__init__()
        self.id = id

    def __del__(self):
        self.terminate()
        self.wait()

    def run(self):

        for i in range(50):
            self._signal.emit(i)

        delete_four_ben(self.id)

        for i in range(50, 100):
            self._signal.emit(i)

        self._signal_result.emit(True)

class ThreadCommandDialog(QThread):
    _signal = pyqtSignal(int)
    _signal_result = pyqtSignal(bool)
    _signal_list = pyqtSignal(list)

    def __init__(self):
        super(ThreadCommandDialog, self).__init__()

    def __del__(self):
        self.terminate()
        self.wait()

    def run(self):
        list_four = []
        list_four.append("four")
        fours = get_all_four_ben_names("four")
        for i in range(30):
            self._signal.emit(i)

        for four in fours:
            list_four.append(four)
        self._signal_list.emit(list_four)

        for i in range(30, 60):
            self._signal.emit(i)

        bon_commande_number = get_last_bon_commande_number("commande")

        if bon_commande_number:
            bon_commande_number = bon_commande_number[0]
            bon_commande_number = bon_commande_number[0]
        else:
            bon_commande_number = 0

        list_number = []
        list_number.append("number")
        list_number.append(bon_commande_number)

        self._signal_list.emit(list_number)

        list_products = []
        list_products.append("products")
        products = get_all_product_names_no_type()
        for product in products:
            list_products.append(product)

        self._signal_list.emit(list_products)

        for i in range(60, 99):
            self._signal.emit(i)

        self._signal_result.emit(True)


class ThreadAddBonCommande(QThread):
    _signal = pyqtSignal(int)
    _signal_result = pyqtSignal(bool)

    def __init__(self, commande_number, date, fourn, product_list):
        super(ThreadAddBonCommande, self).__init__()
        self.commande_number = commande_number
        self.date = date
        self.fourn = fourn
        self.product_list = product_list

    def __del__(self):
        self.terminate()
        self.wait()

    def run(self):

        for i in range(25):
            self._signal.emit(i)

        if is_commande_number_exist(self.commande_number):
            for i in range(25,99):
                self._signal.emit(i)
            self._signal_result.emit(False)
        else:
            for i in range(25, 65):
                self._signal.emit(i)

            four_id = get_fourn_ben_id_from_name(self.fourn)[0]

            bon_id = add_bon(forming_date(self.date), "commande", four_id[0], self.commande_number)

            for product in self.product_list:
                id = get_product_id_by_name(product[0])[0]
                add_operation(id[0], bon_id, product[1])
                old_qte = get_stock_qte_by_product_id(id[0])[0]
                old_qte = old_qte[0]
                new_qte = old_qte + product[1]
                update_stock_by_commande(id[0], new_qte)


            for i in range(65, 99):
                self._signal.emit(i)

            self._signal_result.emit(True)


class ThreadLoadCommande(QThread):
    _signal = pyqtSignal(int)
    _signal_list = pyqtSignal(list)
    _signal_result = pyqtSignal(bool)

    def __init__(self):
        super(ThreadLoadCommande, self).__init__()

    def __del__(self):
        self.terminate()
        self.wait()

    def run(self):

        for i in range(30):
            self._signal.emit(i)

        commandes = get_all_commande()


        row = 0
        for commande in commandes:
            list_commandes = []
            operations = get_operations_by_commande_id(commande[0])
            list_commandes.append(row)
            list_commandes.append(commande[1])
            list_commandes.append(un_forming_date(commande[2]))
            list_commandes.append(commande[3])
            list_commandes.append(operations)
            self._signal_list.emit(list_commandes)
            row = row + 1

        for i in range(30, 99):
            self._signal.emit(i)

        self._signal_result.emit(True)


