import sqlite3


def get_all_product(type):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select stock.stock_id, product.name, stock.qnt, product.unit from stock inner join product in stock.stock_id = product.product_id where product.type =?'
    cur.execute(sql_q, (type))
    connection.close()
    return cur.fetchall()


def get_all_product_names(type):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select product.name from product where product.type =?'
    cur.execute(sql_q, (type))
    connection.close()
    return cur.fetchall()


def get_product_id_by_name(name):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'Select product.product_id from product where product.name =?'
    cur.execute(sql_q, (name))
    connection.close()
    return cur.fetchall()


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
    cur.execute(sql_q, (qnt, product_id))
    connection.commit()

    connection.close()


def update_product(name, type, unit):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'update product set name = ? and  type = ? and  unit = ?'
    cur.execute(sql_q, (name, type, unit))
    connection.commit()

    connection.close()


def update_stock(product_id, qnt):
    connection = sqlite3.connect("database/database.db")
    cur = connection.cursor()
    sql_q = 'update stock set qnt = ? and  stocked_id = ? '
    cur.execute(sql_q, (qnt, product_id))
    connection.commit()

    connection.close()
