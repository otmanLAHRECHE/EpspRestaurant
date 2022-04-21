


def forming_date(db_date):
    d = db_date.split("/")
    if len(d[1]) > 1:
        new_date = d[2] + "-" + d[1] + "-" + d[0]
    else:
        new_date = d[2] + "-" + "0" + d[1] + "-" + d[0]
    return new_date

def un_forming_date(new_date):
    d = new_date.split("-")
    db_date = d[2] + "/" + d[1] + "/" + d[0]
    return db_date