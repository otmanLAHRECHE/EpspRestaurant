from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from pdf_reports import program_report
from threads import ThreadCreateReport


class ExportUi(QtWidgets.QMainWindow):
    def __init__(self, type, data):
        super(ExportUi, self).__init__()
        uic.loadUi("./user_interfaces/export.ui", self)

        self.d= data
        print(self.d)
        self.type = type


        self.ttl = self.findChild(QtWidgets.QLabel, "label")
        self.progress = self.findChild(QtWidgets.QProgressBar, "progressBar")
        self.progress.setValue(0)
        self.status = self.findChild(QtWidgets.QLabel, "label_2")
        self.export = self.findChild(QtWidgets.QPushButton, "pushButton")
        self.export.setEnabled(False)
        self.export.setIcon(QIcon("./icons/download2.png"))
        self.export.clicked.connect(self.export_pdf)
        self.status.setText("Preparation des données")

        self.thr = ThreadExport()
        self.thr._signal.connect(self.signal_accept)
        self.thr._signal_result.connect(self.signal_accept)
        self.thr.start()



    def export_pdf(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save data", "",
                                                  "PDF(*.pdf);;All Files(*.*) ")

        # if file path is blank return back
        if filePath == "":
            message = "destination untrouvable"
            self.alert_(message)
        else:
            if self.type == "prog":
                print(filePath)
                program_report(self.d[0], self.d[1], self.d[2], filePath)
                self.close()
            else:
                print("ok")


    def signal_accept(self, progress):
        if type(progress) == int:
            self.progress.setValue(progress)
        elif type(progress) == bool:
            self.progress.setValue(100)
            self.data = progress
            self.status.setText("complete")
            self.export.setEnabled(True)


    def alert_(self, message):
        alert = QMessageBox()
        alert.setWindowTitle("alert")
        alert.setText(message)
        alert.exec_()