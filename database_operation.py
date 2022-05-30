import sqlite3
from calendar import monthrange

from tools import forming_date, forming_date_filter


def get_all_product(type):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select stock.stock_id, product.name, stock.qnt, product.unit from stock inner join product on stock.stocked_id = product.product_id where product.type =?'
    cur.execute(sql_q, (type,))
    result = cur.fetchall()
    connection.close()
    return result


def get_all_product_names(type):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select product.name from product where product.type =?'
    cur.execute(sql_q, (type,))
    result = cur.fetchall()
    connection.close()
    return result

def get_all_product_names_no_type():
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select product.name from product'
    cur.execute(sql_q)
    result = cur.fetchall()
    connection.close()
    return result

def get_unit_by_product_name(name):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select product.unit from product.name =?'
    cur.execute(sql_q, (name,))
    result = cur.fetchall()
    connection.close()
    return result


def get_product_id_by_name(name):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select product.product_id from product where product.name =?'
    cur.execute(sql_q, (name,))
    result = cur.fetchall()
    connection.close()
    return result


def add_new_product(name, type, unit):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'insert into product (name, type, unit) values (?, ?, ?)'
    cur.execute(sql_q, (name, type, unit))
    connection.commit()
    connection.close()


def add_new_stock(product_id, qnt):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'insert into stock (qnt, stocked_id) values (?, ?)'
    cur.execute(sql_q, (float(qnt), product_id))
    connection.commit()
    connection.close()


def update_product(id, name, type, unit):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'update product set name = ?, type = ?, unit = ? where product.product_id = ?'
    cur.execute(sql_q, (name, type, unit, id))
    connection.commit()
    connection.close()


def update_stock(id, qnt):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'update stock set qnt = ?  where stock.stock_id = ?'
    cur.execute(sql_q, (qnt, id))
    connection.commit()
    connection.close()

def update_stock_by_commande(id_product, qnt):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'update stock set qnt = ?  where stock.stocked_id = ?'
    cur.execute(sql_q, (qnt, id_product))
    connection.commit()
    connection.close()

def get_stock_qte_by_product_id(product_id):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select stock.qnt from stock inner join product on stock.stocked_id = product.product_id where product.product_id =?'
    cur.execute(sql_q, (product_id,))
    result = cur.fetchall()
    connection.close()
    return result


def is_product_exist(name):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select count(*) from product where product.name =?'
    cur.execute(sql_q, (name,))
    count = cur.fetchall()[0]
    connection.close()
    if count[0] == 0:
        return False
    else:
        return True

def get_product_id_by_stock_id(stock_id):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select stock.stocked_id from stock where stock.stock_id =?'
    cur.execute(sql_q, (stock_id,))
    result = cur.fetchall()
    connection.close()
    return result

def search_food(search_text):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select stock.stock_id, product.name, stock.qnt, product.unit from stock inner join product on stock.stocked_id = product.product_id where product.type =? and product.name like ?'
    cur.execute(sql_q, ("food", "%" + str(search_text) + "%"))
    result = cur.fetchall()
    connection.close()
    return result

def is_four_ben_exist(name):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select count(*) from fb where fb.name =?'
    cur.execute(sql_q, (name,))
    count = cur.fetchall()[0]
    connection.close()
    if count[0] == 0:
        return False
    else:
        return True

def add_new_four_ben(name, type):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'insert into fb (name, type) values (?, ?)'
    cur.execute(sql_q, (name, type))
    connection.commit()
    connection.close()

def get_all_four_ben(type):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select fb.fb_id, fb.name from fb where fb.type =?'
    cur.execute(sql_q, (type,))
    result = cur.fetchall()
    connection.close()
    return result

def get_fourn_ben_id_from_name(name):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select fb.fb_id from fb where fb.name =?'
    cur.execute(sql_q, (name,))
    result = cur.fetchall()
    connection.close()
    return result

def update_four_ben(id, name):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'update fb set name = ? where fb.fb_id = ?'
    cur.execute(sql_q, (name,  id))
    connection.commit()
    connection.close()

def delete_four_ben(id):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'delete from fb where fb.fb_id = ?'
    cur.execute(sql_q, (id,))
    connection.commit()
    connection.close()

def get_all_four_ben_names(type):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select fb.name from fb where fb.type =?'
    cur.execute(sql_q, (type,))
    result = cur.fetchall()
    connection.close()
    return result

def get_last_bon_commande_number(type):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select bon.bon_number from bon where bon.type =? order by bon.bon_number DESC'
    cur.execute(sql_q, (type,))
    result = cur.fetchall()
    connection.close()
    return result

def is_commande_number_exist(commande_number):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select * from bon where bon.bon_number =? and bon.type =?'
    cur.execute(sql_q, (commande_number,'commande'))
    result = cur.fetchall()
    connection.close()
    if result:
        return True
    else:
        return False

def add_bon(date, type, fb_fk_id, bon_number):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'insert into bon (dt, type, fb_fk_id, bon_number) values (?, ?, ?, ?)'
    cur.execute(sql_q, (date, type, fb_fk_id, bon_number))
    connection.commit()
    id = cur.lastrowid
    connection.close()
    return id

def add_operation(product_op_id, bon_op_id, qnt):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'insert into opertation (product_op_id, bon_op_id, qnt) values (?, ?, ?)'
    cur.execute(sql_q, (product_op_id, bon_op_id, qnt))
    connection.commit()
    connection.close()

def get_product_type_by_name(name):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select product.unit from product where product.name =?'
    cur.execute(sql_q, (name,))
    unit = cur.fetchall()
    connection.close()
    return unit

def get_all_commande():
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? order by date(bon.dt) DESC LIMIT 50'
    cur.execute(sql_q, ('commande',))
    unit = cur.fetchall()
    connection.close()
    return unit

def get_operations_by_commande_id(id_bon_commande):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select product.name, opertation.qnt, product.unit from product inner join opertation on product.product_id = opertation.product_op_id where opertation.bon_op_id = ?'
    cur.execute(sql_q, (id_bon_commande,))
    unit = cur.fetchall()
    connection.close()
    return unit

def get_commande_id_by_bon_com_number(com_number):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select bon.bon_id from bon  where bon.bon_number = ? and bon.type = ?'
    cur.execute(sql_q, (com_number, 'commande'))
    unit = cur.fetchall()
    connection.close()
    return unit

def update_bon(bon_id, date, type, fb_fk_id, bon_number):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'update bon set dt=?, type=?, fb_fk_id=?, bon_number=? where bon.bon_id =?'
    cur.execute(sql_q, (date, type, fb_fk_id, bon_number, bon_id))
    connection.commit()
    connection.close()

def delete_all_bon_operation(bon_id):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'delete from opertation where opertation.bon_op_id = ?'
    cur.execute(sql_q, (bon_id,))
    connection.commit()
    connection.close()

def delete_bon_commande(bon_id):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'delete from bon where bon.bon_id = ?'
    cur.execute(sql_q, (bon_id,))
    connection.commit()
    connection.close()


def filter_commande(filter):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    date = filter[0]



    filter_type = filter[2]

    arg1 = ""
    arg1_2 = ""
    arg2 = ""


    if date[0] == 1:
        arg1 = forming_date_filter(date[1])
        print(arg1)
        if filter_type[0] == 1:
            arg2 = filter_type[1]
            if filter[1] == 0:
                sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) <= date(?) and bon.bon_number = ? order by date(bon.dt) DESC LIMIT 50'
                cur.execute(sql_q, ('commande',arg1,arg2))
            else:
                sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) <= date(?) and bon.bon_number = ? order by date(bon.dt) ASC LIMIT 50'
                cur.execute(sql_q, ('commande',arg1, arg2))
        else:
            if filter_type[1] != "all":
                arg2 = filter_type[1]
                if filter[1] == 0:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) <= date(?) and fb.name = ? order by date(bon.dt) DESC LIMIT 50'
                    cur.execute(sql_q, ('commande',arg1, arg2))
                else:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) <= date(?) and fb.name = ? order by date(bon.dt) ASC LIMIT 50'
                    cur.execute(sql_q, ('commande',arg1, arg2))
            else:
                if filter[1] == 0:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) <= date(?) order by date(bon.dt) DESC LIMIT 50'
                    cur.execute(sql_q, ('commande',arg1,))
                else:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) <= date(?) order by date(bon.dt) ASC LIMIT 50'
                    cur.execute(sql_q, ('commande',arg1,))
    elif date[0] == 2:
        arg1 = forming_date_filter(date[1])
        if filter_type[0] == 1:
            arg2 = filter_type[1]
            if filter[1] == 0:
                sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) >= date(?) and bon.bon_number = ? order by date(bon.dt) DESC LIMIT 50'
                cur.execute(sql_q, ('commande',arg1,arg2))
            else:
                sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) >= date(?) and bon.bon_number = ? order by date(bon.dt) ASC LIMIT 50'
                cur.execute(sql_q, ('commande',arg1, arg2))
        else:
            if filter_type[1] != "all":
                arg2 = filter_type[1]
                if filter[1] == 0:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) >= date(?) and fb.name = ? order by date(bon.dt) DESC LIMIT 50'
                    cur.execute(sql_q, ('commande',arg1, arg2))
                else:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) >= date(?) and fb.name = ? order by date(bon.dt) ASC LIMIT 50'
                    cur.execute(sql_q, ('commande',arg1, arg2))
            else:
                if filter[1] == 0:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) >= date(?) order by date(bon.dt) DESC LIMIT 50'
                    cur.execute(sql_q, ('commande',arg1,))
                else:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) >= date(?) order by date(bon.dt) ASC LIMIT 50'
                    cur.execute(sql_q, ('commande',arg1,))
    elif date[0] == 3:
        arg1 = forming_date_filter(date[1])
        arg1_2 = forming_date_filter(date[2])
        if filter_type[0] == 1:
            arg2 = filter_type[1]
            if filter[1] == 0:
                sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) BETWEEN date(?) AND date(?) and bon.bon_number = ? order by date(bon.dt) DESC LIMIT 50'
                cur.execute(sql_q, ('commande',arg1, arg1_2, arg2))
            else:
                sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) BETWEEN date(?) AND date(?) and bon.bon_number = ? order by date(bon.dt) ASC LIMIT 50'
                cur.execute(sql_q, ('commande',arg1, arg1_2, arg2))
        else:
            if filter_type[1] != "all":
                arg2 = filter_type[1]
                if filter[1] == 0:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) BETWEEN date(?) AND date(?) and fb.name = ? order by date(bon.dt) DESC LIMIT 50'
                    cur.execute(sql_q, ('commande',arg1, arg1_2, arg2))
                else:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) BETWEEN date(?) AND date(?) and fb.name = ? order by date(bon.dt) ASC LIMIT 50'
                    cur.execute(sql_q, ('commande',arg1, arg1_2, arg2))
            else:
                if filter[1] == 0:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) BETWEEN date(?) AND date(?) order by date(bon.dt) DESC LIMIT 50'
                    cur.execute(sql_q, ('commande',arg1, arg1_2,))
                else:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) BETWEEN date(?) AND date(?) order by date(bon.dt) ASC LIMIT 50'
                    cur.execute(sql_q, ('commande',arg1, arg1_2))
    else:
        if filter_type[0] == 1:
            arg2 = filter_type[1]
            if filter[1] == 0:
                sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and bon.bon_number = ? order by date(bon.dt) DESC LIMIT 50'
                cur.execute(sql_q, ('commande',arg2,))
            else:
                sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and  bon.bon_number = ? order by date(bon.dt) ASC LIMIT 50'
                cur.execute(sql_q, ('commande',arg2,))
        else:
            if filter_type[1] != "all":
                arg2 = filter_type[1]
                if filter[1] == 0:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and fb.name = ? order by date(bon.dt) DESC LIMIT 50'
                    cur.execute(sql_q, ('commande',arg2,))
                else:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and fb.name = ? order by date(bon.dt) ASC LIMIT 50'
                    cur.execute(sql_q, ('commande',arg2,))
            else:
                if filter[1] == 0:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? order by date(bon.dt) DESC LIMIT 50'
                    cur.execute(sql_q, ('commande',))
                else:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? order by date(bon.dt) ASC LIMIT 50'
                    cur.execute(sql_q, ('commande',))

    unit = cur.fetchall()
    connection.close()
    return unit


def get_filtred_operations_by_commande_id(id_bon_commande, filter):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    filter_type = filter[2]


    args = filter_type[2]
    if args:
        args.insert(0,id_bon_commande)
        l = len(args) - 1
        sql_q = 'Select product.name, opertation.qnt, product.unit from product inner join opertation on product.product_id = opertation.product_op_id where opertation.bon_op_id = ? and product.name in ({seq})'.format(
    seq=','.join(['?']*l))
        cur.execute(sql_q, args)
    else:
        sql_q = 'Select product.name, opertation.qnt, product.unit from product inner join opertation on product.product_id = opertation.product_op_id where opertation.bon_op_id = ?'
        cur.execute(sql_q, (id_bon_commande,))


    unit = cur.fetchall()
    connection.close()
    return unit


def is_sortie_number_exist(sortie_number):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select * from bon where bon.bon_number =? and bon.type =?'
    cur.execute(sql_q, (sortie_number,'sortie'))
    result = cur.fetchall()
    connection.close()
    if result:
        return True
    else:
        return False


def get_all_sorties():
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? order by date(bon.dt) DESC LIMIT 50'
    cur.execute(sql_q, ('sortie',))
    unit = cur.fetchall()
    connection.close()
    return unit


def get_sortie_id_by_bon_sort_number(com_number):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select bon.bon_id from bon  where bon.bon_number = ? and bon.type = ?'
    cur.execute(sql_q, (com_number, 'sortie'))
    unit = cur.fetchall()
    connection.close()
    return unit

def get_selected_sortie_by_sortie_number(bon_number):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and bon.bon_number = ? order by date(bon.dt) DESC LIMIT 50'
    cur.execute(sql_q, ('sortie', bon_number))
    unit = cur.fetchall()
    connection.close()
    return unit


def filter_sorties(filter):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    date = filter[0]


    filter_type = filter[2]

    arg1 = ""
    arg1_2 = ""
    arg2 = ""


    if date[0] == 1:
        arg1 = forming_date_filter(date[1])
        print(arg1)
        if filter_type[0] == 1:
            arg2 = filter_type[1]
            if filter[1] == 0:
                sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) <= date(?) and bon.bon_number = ? order by date(bon.dt) DESC LIMIT 50'
                cur.execute(sql_q, ('sortie',arg1,arg2))
            else:
                sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) <= date(?) and bon.bon_number = ? order by date(bon.dt) ASC LIMIT 50'
                cur.execute(sql_q, ('sortie',arg1, arg2))
        else:
            if filter_type[1] != "all":
                arg2 = filter_type[1]
                if filter[1] == 0:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) <= date(?) and fb.name = ? order by date(bon.dt) DESC LIMIT 50'
                    cur.execute(sql_q, ('sortie',arg1, arg2))
                else:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) <= date(?) and fb.name = ? order by date(bon.dt) ASC LIMIT 50'
                    cur.execute(sql_q, ('sortie',arg1, arg2))
            else:
                if filter[1] == 0:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) <= date(?) order by date(bon.dt) DESC LIMIT 50'
                    cur.execute(sql_q, ('sortie',arg1,))
                else:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) <= date(?) order by date(bon.dt) ASC LIMIT 50'
                    cur.execute(sql_q, ('sortie',arg1,))
    elif date[0] == 2:
        arg1 = forming_date_filter(date[1])
        if filter_type[0] == 1:
            arg2 = filter_type[1]
            if filter[1] == 0:
                sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) >= date(?) and bon.bon_number = ? order by date(bon.dt) DESC LIMIT 50'
                cur.execute(sql_q, ('sortie',arg1,arg2))
            else:
                sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) >= date(?) and bon.bon_number = ? order by date(bon.dt) ASC LIMIT 50'
                cur.execute(sql_q, ('sortie',arg1, arg2))
        else:
            if filter_type[1] != "all":
                arg2 = filter_type[1]
                if filter[1] == 0:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) >= date(?) and fb.name = ? order by date(bon.dt) DESC LIMIT 50'
                    cur.execute(sql_q, ('sortie',arg1, arg2))
                else:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) >= date(?) and fb.name = ? order by date(bon.dt) ASC LIMIT 50'
                    cur.execute(sql_q, ('sortie',arg1, arg2))
            else:
                if filter[1] == 0:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) >= date(?) order by date(bon.dt) DESC LIMIT 50'
                    cur.execute(sql_q, ('sortie',arg1,))
                else:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) >= date(?) order by date(bon.dt) ASC LIMIT 50'
                    cur.execute(sql_q, ('sortie',arg1,))
    elif date[0] == 3:
        arg1 = forming_date_filter(date[1])
        arg1_2 = forming_date_filter(date[2])
        if filter_type[0] == 1:
            arg2 = filter_type[1]
            if filter[1] == 0:
                sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) BETWEEN date(?) AND date(?) and bon.bon_number = ? order by date(bon.dt) DESC LIMIT 50'
                cur.execute(sql_q, ('sortie',arg1, arg1_2, arg2))
            else:
                sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) BETWEEN date(?) AND date(?) and bon.bon_number = ? order by date(bon.dt) ASC LIMIT 50'
                cur.execute(sql_q, ('sortie',arg1, arg1_2, arg2))
        else:
            if filter_type[1] != "all":
                arg2 = filter_type[1]
                if filter[1] == 0:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) BETWEEN date(?) AND date(?) and fb.name = ? order by date(bon.dt) DESC LIMIT 50'
                    cur.execute(sql_q, ('sortie',arg1, arg1_2, arg2))
                else:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) BETWEEN date(?) AND date(?) and fb.name = ? order by date(bon.dt) ASC LIMIT 50'
                    cur.execute(sql_q, ('sortie',arg1, arg1_2, arg2))
            else:
                if filter[1] == 0:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) BETWEEN date(?) AND date(?) order by date(bon.dt) DESC LIMIT 50'
                    cur.execute(sql_q, ('sortie',arg1, arg1_2,))
                else:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and date(bon.dt) BETWEEN date(?) AND date(?) order by date(bon.dt) ASC LIMIT 50'
                    cur.execute(sql_q, ('sortie',arg1, arg1_2))
    else:
        if filter_type[0] == 1:
            arg2 = filter_type[1]
            if filter[1] == 0:
                sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and bon.bon_number = ? order by date(bon.dt) DESC LIMIT 50'
                cur.execute(sql_q, ('sortie',arg2,))
            else:
                sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and  bon.bon_number = ? order by date(bon.dt) ASC LIMIT 50'
                cur.execute(sql_q, ('sortie',arg2,))
        else:
            if filter_type[1] != "all":
                arg2 = filter_type[1]
                if filter[1] == 0:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and fb.name = ? order by date(bon.dt) DESC LIMIT 50'
                    cur.execute(sql_q, ('sortie',arg2,))
                else:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? and fb.name = ? order by date(bon.dt) ASC LIMIT 50'
                    cur.execute(sql_q, ('sortie',arg2,))
            else:
                if filter[1] == 0:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? order by date(bon.dt) DESC LIMIT 50'
                    cur.execute(sql_q, ('sortie',))
                else:
                    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where bon.type = ? order by date(bon.dt) ASC LIMIT 50'
                    cur.execute(sql_q, ('sortie',))

    unit = cur.fetchall()
    connection.close()
    return unit


def get_filtred_operations_by_sortie_id(id_bon_commande, filter):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    filter_type = filter[2]


    args = filter_type[2]
    if args:
        args.insert(0,id_bon_commande)
        l = len(args) - 1
        sql_q = 'Select product.name, opertation.qnt, product.unit from product inner join opertation on product.product_id = opertation.product_op_id where opertation.bon_op_id = ? and product.name in ({seq})'.format(
    seq=','.join(['?']*l))
        cur.execute(sql_q, args)
    else:
        sql_q = 'Select product.name, opertation.qnt, product.unit from product inner join opertation on product.product_id = opertation.product_op_id where opertation.bon_op_id = ?'
        cur.execute(sql_q, (id_bon_commande,))


    unit = cur.fetchall()
    connection.close()
    return unit


def get_bon_by_month(type, data):

    year = data[2]
    month = int(data[0]) + 1
    day_start = 1
    day_end = monthrange(year, month)[1]

    date1 = day_start + "/" + month + "/" + year
    date1 = forming_date(date1)
    date2 = day_end + "/" + month + "/" + year
    date2 = forming_date(date2)


    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select bon.bon_id from bon  where bon.type = ? and date(bon.dt) >= date(?) and date(bon.dt) <= date(?)'
    cur.execute(sql_q, (type, date1, date2))
    unit = cur.fetchall()
    connection.close()
    return unit


def get_bon_by_year(type, year):


    month = 1
    day_start = 1
    day_end = monthrange(year, 12)[1]

    date1 = day_start + "/" + "01" + "/" + year
    date1 = forming_date(date1)
    date2 = day_end + "/" + "12" + "/" + year
    date2 = forming_date(date2)


    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select bon.bon_id from bon  where bon.type = ? and date(bon.dt) >= date(?) and date(bon.dt) <= date(?)'
    cur.execute(sql_q, (type, date1, date2))
    unit = cur.fetchall()
    connection.close()
    return unit














