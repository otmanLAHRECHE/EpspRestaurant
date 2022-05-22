import os
import sys

from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineDownloadItem

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

pdf_js = QtCore.QUrl.fromLocalFile(
    os.path.join(CURRENT_DIR, "pdfjs/web/viewer.html")
).toString()



class PdfReport(QtWebEngineWidgets.QWebEngineView):
    def __init__(self,  parent=None):
        super(PdfReport, self).__init__(parent)
        QtWebEngineWidgets.QWebEngineProfile.defaultProfile().downloadRequested.connect(
            self.on_downloadRequested
        )

    def load_pdf(self, filename):
        url  = QtCore.QUrl.fromLocalFile(
    os.path.join(CURRENT_DIR, filename)
).toString()
        url_final = QtCore.QUrl.fromUserInput("%s?file=%s" % (pdf_js, url))
        self.load(url_final)
        print(url)
        print(pdf_js)
        print(url_final)

    def sizeHint(self):
        return QtCore.QSize(640, 480)

    @QtCore.pyqtSlot(QtWebEngineWidgets.QWebEngineDownloadItem)
    def on_downloadRequested(self, download):
        path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save File", "sample.pdf", "*.pdf"
        )
        if path:
            download.setPath(path)
            download.accept()



