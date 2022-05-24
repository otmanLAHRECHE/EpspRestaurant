import xlsxwriter as xlsxwriter




def program_report():
    workbook = xlsxwriter.Workbook('xslx_models/Program_report.xlsx')

    worksheet = workbook.add_worksheet("My sheet")

    scores = (
        ['ankit', 1000],
        ['rahul', 100],
        ['priya', 300],
        ['harshita', 50],
    )

    row = 0
    col = 0

    for name, score in (scores):
        worksheet.write(row, col, name)
        worksheet.write(row, col + 1, score)
        row += 1

    workbook.close()



