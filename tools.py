


def forming_date(db_date):
    d = db_date.split("/")
    new_date = d[2] + "-" + d[1] + "-" + d[0]
    return new_date