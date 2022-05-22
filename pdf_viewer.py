import sys

from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineDownloadItem

PDFJS = "file:///web/viewer.html"


class PdfReport(QWebEngineView):
    def __init__(self, filename):
        super(PdfReport, self).__init__()

        print(
            f"PyQt5 version: {QtCore.PYQT_VERSION_STR}, Qt version: {QtCore.QT_VERSION_STR}"
        )

        filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, filter="PDF (*.pdf)")
        if not filename:
            print("please select the .pdf file")
            sys.exit(0)


        settings = self.settings()
        settings.setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        print(filename)
        url = QtCore.QUrl.fromLocalFile(filename)
        self.load(url)


