from openpyxl import load_workbook


def program_report(data):
    wb = load_workbook('xslx/pr.xlsx')
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

    wb.save("xslx/pr.xlsx")



