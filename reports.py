from openpyxl import load_workbook

from tools import un_forming_date


def program_report(data):
    wb = load_workbook('xslx/program.xlsx')
    ws = wb.active

    menu = data[0]
    month = data[1]
    year = data[2]

    print(menu)
    print(month)
    print(year)

    for i in range(11, 18):
        day = menu[i-11]
        print(day)
        ws["F" + str(i)] = day[0]
        ws["E" + str(i)] = day[1]
        ws["D" + str(i)] = day[2]
        ws["C" + str(i)] = day[3]
        ws["B" + str(i)] = day[4]
        ws["A" + str(i)] = day[5]

    ws["D8"] = month + "/" + year

    wb.save("xslx/program.xlsx")


def sortie_report(data):
    wb = load_workbook('xslx/sortie_model.xlsx')
    ws = wb.active

    sortie = data[0]
    opertations = data[1]

    date = un_forming_date(sortie[2])

    ws["D8"] = date
    ws["E10"] = sortie[3]

    i = 0
    for operation in opertations:
        index = 13+i
        ws["G"+str(int(index))] = i + 1
        if operation[2] == "no_unit":
            prod = str(operation[1])
        else:
            prod = str(operation[1]) + operation[2]

        ws["D" + str(index)] = operation[0]
        ws["B" + str(index)] = prod

        i = i+1


    index = 13 + i

    ws.delete_rows(index, 47 - index)

    wb.save("xslx/raports/sortie.xlsx")



