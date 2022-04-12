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
    sql_q = 'Select fb.name from fb where fb.type =?'
    cur.execute(sql_q, (type,))
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
