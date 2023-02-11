
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

import urllib.request
from ui_mainwindow import Ui_MainWindow




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.save_location=QLineEdit()
        self.ui.pb.clicked.connect(self.download)
        self.ui.pb2.clicked.connect(self.browse_File)

    def browse_File(self):
        save_file=QFileDialog.getSaveFileName(self,caption="save file as" , filter="All File(*.*)")
        self.save_location.setText(save_file)
    def download(self):
        url= self.ui.lineEdit.text()
        save_location=self.ui.lineEdit_2.text()

        try:
            urllib.request.urlretrieve(url,save_location ,self.report)
        except Exception:
            QMessageBox.information(self , "Warning" , "Download is filed")
            return

        QMessageBox.information(self , "Information" , "Download is complete")
        self.ui.progressBar.setValue(0)
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")

    def report(self,blocknum,blocksize,totalsize):
        readsofar=blocknum * blocksize
        if totalsize > 0:
            percent=readsofar *100 / totalsize
            self.ui.progressBar.setValue(int(percent))


app = QApplication(sys.argv)
mainwindow = MainWindow()
mainwindow.setWindowTitle("Pydownloader")
mainwindow.show()

app.exec()