


def forming_date(db_date):
    d = db_date.split("/")
    if not len(d[0]) > 1:
        d[0] = "0" + d[0]
    if len(d[1]) > 1:
        new_date = d[2] + "-" + d[1] + "-" + d[0]
    else:
        new_date = d[2] + "-" + "0" + d[1] + "-" + d[0]
    return new_date

def forming_date_filter(db_date):
    d = db_date.split("/")
    if not len(d[0]) > 1:
        d[0] = "0" + d[0]
    if not len(d[1]) > 1:
        d[1] = "0" + d[1]
    new_date = d[2] + "-" + d[0] + "-" + d[1]

    return new_date

def un_forming_date(new_date):
    d = new_date.split("-")
    if not len(d[0]) > 1:
        d[0] = "0" + d[0]
    db_date = d[2] + "/" + d[1] + "/" + d[0]
    return db_date