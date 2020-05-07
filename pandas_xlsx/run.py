# -*- coding: utf-8 -*-
"""
Data transfer
From pandas DataFrame to Excel

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
        """Export a pandas DataFrame to a Excel spreadsheet."""

        QMainWindow.__init__(self, parent)
        uic.loadUi('view/mainwindow.ui', self)
        
        # App objects.
        self.df = pd.DataFrame()
        self.dir_wb_name = ''  # Directory and name of the Excel workbook.
        self.ws_name = ''  # Name of the Excel worksheet.
        self.message = ''
        
        # PyQt5 objects.
        self.btn_import_df = self.pushButtonImportDF
        self.txt_df = self.textEditDataFrame
        self.lne_dir = self.lineEditDirectory
        self.lne_wb = self.lineEditNameWorkbook
        self.lne_ws = self.lineEditNameWorksheet
        self.btn_export_xlsx = self.pushButtonExportExcel
        self.lbl_msg = self.labelMessage
        
        # Class instances.
        self.controller = Controller(self)
        
        # Events.
        self.btn_import_df.clicked.connect(self.controller.import_df)
        self.btn_export_xlsx.clicked.connect(self.controller.export_xlsx)
        
    def display_dataframe(self):
        """Display the pandas DataFrame in the MainWindow."""
        
        str_df = str(self.df)
        self.txt_df.setText(str_df)
        
    def display_message(self):
        """
        Display a message when the export to the Excel spreadsheet is finish.
        """

        self.lbl_msg.setText(self.message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
