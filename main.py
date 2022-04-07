

import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication

import app
from threads import ThreadLoadingApp

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'EPSP_Djanet.EPSP_Guard.1'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("./user_interfaces/loading_app.ui", self)

        self.label = self.findChild(QtWidgets.QLabel, "loading_progress_status")
        self.progress = self.findChild(QtWidgets.QProgressBar, "my_progressBar")
        self.progress.setValue(20)

        self.t = ThreadLoadingApp()
        self.t._signal.connect(self.signal_accepted)
        self.t._signal_result.connect(self.signal_accepted)
        self.t.start()

    def signal_accepted(self, progress):
        if type(progress) == int:
            self.progress.setValue(progress)
        else:
            self.progress.setValue(100)
            self.label.setText("Wellcome")
            self.next_page = app.AppUi()
            self.next_page.show()
            self.close()




def main():
    app = QApplication(sys.argv)
    # app.setLayoutDirection(Qt.RightToLeft)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()



