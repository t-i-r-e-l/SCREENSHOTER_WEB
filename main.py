from FORMS.main_window import Ui_MainWindow
from FORMS.web_browser import Ui_web_browser
import sys

import string
import random

from PyQt5 import QtCore, QtGui, QtWidgets

class windows(QtWidgets.QMainWindow):  

    def __init__(self, ConstType):
        super(windows, self).__init__()
        self.ui = ConstType()
        self.ui.setupUi(self)
        if ConstType == Ui_MainWindow:
            self.ui.pushButton_show_site.clicked.connect(self.show_site)
            self.ui.pushButton_create_a_screenshot.clicked.connect(self.screenshot)

    def show_site(self):
        brow.setUrl(QtCore.QUrl(self.ui.lineEdit_website.text()))
        ap.resize(int(self.ui.lineEdit_width.text()), int(self.ui.lineEdit_height.text()))
        brow.resize(int(self.ui.lineEdit_width.text()), int(self.ui.lineEdit_height.text()))
        brow.setZoomFactor(float(self.ui.lineEdit_sitescale.text()))
        ap.show()

    def screenshot(self):
        #brow.setUrl(QtCore.QUrl(self.ui.lineEdit_website.text()))
        #ap.resize(int(self.ui.lineEdit_width.text()), int(self.ui.lineEdit_height.text()))
        #brow.resize(int(self.ui.lineEdit_width.text()), int(self.ui.lineEdit_height.text()))
        #brow.setZoomFactor(float(self.ui.lineEdit_sitescale.text()))
        #ap.show()

        img = QtGui.QPixmap(int(self.ui.lineEdit_width.text()), int(self.ui.lineEdit_height.text()))
        brow.render(img)
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
        img.save('SCREENSHOTs/' + res + '.png')

        ap.close()

    

app = QtWidgets.QApplication([])
application = windows(Ui_MainWindow)
application0 = windows(Ui_web_browser)

ap = application0
brow = ap.ui.web_browser_2

application.show()
exit = sys.exit(app.exec())