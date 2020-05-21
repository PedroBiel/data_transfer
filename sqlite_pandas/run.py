# -*- coding: utf-8 -*-
"""
Data transfer
From SQLite to pandas DataFrame

Created on 07.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


import sys

import pandas as pd

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from controller.app_controller import Controller


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        """Export a SQLite3 database to a pandas DataFrame."""

        QMainWindow.__init__(self, parent)
        uic.loadUi('view/mainwindow.ui', self)
        
        # App objects.
        self.df = pd.DataFrame()
        self.dir_db_name = ''  # Directory and name of the SQLite3 database.
        self.table = ''  # Name of the table in the SQLite3 database.
        self.message = ''
        
        # PyQt5 objects.
        self.lne_dir = self.lineEditDirectory
        self.lne_db = self.lineEditNameDataBase
        self.lne_table = self.lineEditTable
        self.btn_import_sql = self.pushButtonImportSQLite
        self.txt_df = self.textEditDataFrame
        self.lbl_msg = self.labelMessage
        
        # Class instances.
        self.controller = Controller(self)
        
        # Events.
        self.btn_import_sql.clicked.connect(self.controller.import_sql)
        # self.btn_display_df.clicked.connect(self.display_df)
        
    def display_dataframe(self):
        """Display the pandas DataFrame in the MainWindow."""
        
        self.txt_df.clear()
        str_df = str(self.df)
        self.txt_df.setText(str_df)
        
    def display_message(self):
        """
        Display a message when the export to the SQLite3 database is finish.
        """

        self.lbl_msg.setText(self.message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
