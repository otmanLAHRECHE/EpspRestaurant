from epsp_pdf import EpspPdf


def program_report(data, month, year):
    pdf = EpspPdf(orientation="landscape", format="A4")
    pdf.alias_nb_pages()
    pdf.add_page()
    index = "/pdf_reports/program_report.pdf"
    pdf.output("./pdf_reports/program_report.pdf")

    return index