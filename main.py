import sys
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *

# GUI FILE
from ui_mining import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # PAGES
        ########################################################################

        # PAGE 1
        self.ui.informations_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.info_page))

        # PAGE 2
        self.ui.rpc_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.rpc_page))

        # PAGE 3
        self.ui.rpg_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.rpg_page))

        # Page 4
        self.ui.rrc_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.rrc_page))

        # Page 5
        self.ui.results_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.results_page))

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        # ==> END ##


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
