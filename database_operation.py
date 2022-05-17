import sqlite3


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
    sql_q = 'Select * from bon where bon.bon_number =?'
    cur.execute(sql_q, (commande_number,))
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
    sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id order by date(bon.dt) DESC LIMIT 50'
    cur.execute(sql_q)
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
    sql_q = 'Select bon.bon_id from bon  where bon.bon_number = ?'
    cur.execute(sql_q, (com_number,))
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

    if filter[1] == 0:
        q_order = "order by date(bon.dt) DESC"
    else:
        q_order = "order by date(bon.dt) ASC"

    filter_type = filter[2]

    arg1 = ""
    arg1_2 = ""
    arg2 = ""

    if filter_type[0] == 0:
        q_filter = 'bon.bon_number = ?'
        arg2 = filter_type[1]
    else:
        if filter_type[1] != "all":
            q_filter = 'fb.name = ?'
            arg2 = filter_type[1]
        else:
            q_filter = ''


    if date[0] == 1:
        q_date = 'date(bon.dt) < ?'
        arg1 = date[1]
    elif date[0] == 2:
        q_date = 'date(bon.dt) > ?'
        arg1 = date[1]
    elif date[0] == 3:
        q_date = 'BETWEEN date(?) AND date(?)'
        arg1 = date[1]
        arg1_2 = date[2]
    else:
        q_date = ''


    if arg1 == "":
        if arg2 == "":
            if filter[1] == 0:
                sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where order by date(bon.dt) DESC LIMIT 50'
                cur.execute(sql_q)
            else:
                sql_q = 'Select bon.bon_id, bon.bon_number, bon.dt, fb.name from bon inner join fb on bon.fb_fk_id = fb.fb_id where order by date(bon.dt) ASC LIMIT 50'
                cur.execute(sql_q)

        else:
            if filter[1] == 0:
                q_order = "order by date(bon.dt) DESC"
            else:
                q_order = "order by date(bon.dt) ASC"
            cur.execute(sql_q,(arg2,))
    else:
        if arg1_2 == "":
            if arg2 == "":
                if filter[1] == 0:
                    q_order = "order by date(bon.dt) DESC"
                else:
                    q_order = "order by date(bon.dt) ASC"
                cur.execute(sql_q,(arg1,))
            else:
                if filter[1] == 0:
                    q_order = "order by date(bon.dt) DESC"
                else:
                    q_order = "order by date(bon.dt) ASC"
                cur.execute(sql_q, (arg1, arg2))
        else:
            if arg2 == "":
                if filter[1] == 0:
                    q_order = "order by date(bon.dt) DESC"
                else:
                    q_order = "order by date(bon.dt) ASC"
                cur.execute(sql_q,(arg1, arg1_2))
            else:
                if filter[1] == 0:
                    q_order = "order by date(bon.dt) DESC"
                else:
                    q_order = "order by date(bon.dt) ASC"
                cur.execute(sql_q, (arg1, arg1_2, arg2))

    cur.execute(sql_q)
    unit = cur.fetchall()
    connection.close()
    return unit





