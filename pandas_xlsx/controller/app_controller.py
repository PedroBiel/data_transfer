# -*- coding: utf-8 -*-
"""
Data transfer
From pandas DataFrame to Excel

Created on 07.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


from data.app_data import Data
from data_transfer.pandasdfxlsx import PandasDFXLSX


class Controller:
    
    def __init__(self, mainwindow):
        """Controller of the apllication."""
        
        self.w = mainwindow

    # Import pandas DataFrame.
    def import_df(self):
        """Import pandas DataFrame from data."""
        
        self.w.df = self.get_dataframe()
        self.w.display_dataframe()

    def get_dataframe(self):
        """Get the pandas DataFrame."""
        
        df = Data.data_frame
        
        return df

    # Export to Excel.
    def export_xlsx(self):
        """
        Export pandas DataFrame to a Excel spreadsheet in the indicated
        directory.
        """
        
        directory = self.w.lne_dir.text()
        wb_name = self.w.lne_wb.text()
        self.w.dir_db_name = directory + '\\' + wb_name + '.xlsx'
        self.w.ws_name = self.w.lne_ws.text()
        self.df_to_xlsx()
        self.w.display_message()
        
    def df_to_xlsx(self):
        """From pandas DataFrame to Excel spreadsheet."""
        
        wb_name = self.w.lne_wb.text()
        
        if wb_name != '':
            
            try:
                df_xlsx = PandasDFXLSX(
                    self.w.df, self.w.dir_db_name, self.w.ws_name
                    )
                df_xlsx.df_to_excel()
                
            except ValueError as e:
                self.w.message = str(e)
                
            else:
                self.w.message = 'Done!'
                
        else:
            self.w.message = 'Empty name of the Excel spreadsheet'
