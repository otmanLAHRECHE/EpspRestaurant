from epsp_pdf import EpspPdf


def program_report(data, month, year, path):
    pdf = EpspPdf(orientation="landscape", format="A4")
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.output(path)
