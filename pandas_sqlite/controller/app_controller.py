# -*- coding: utf-8 -*-
"""
Data transfer
From pandas DataFrame to SQLite

Created on 06.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


from data.app_data import Data
from data_transfer.pandasdfsqlite import PandasDFSQLite


class Controller:
    
    def __init__(self, mainwindow):
        """Controller of the apllication."""
        
        self.w = mainwindow

    # Import pandas DataFrame.
    def import_df(self):
        """Imports pandas DataFrame from data."""
        
        self.w.df = self.get_dataframe()
        self.w.display_dataframe()

    def get_dataframe(self):
        """Get the pandas DataFrame."""
        
        df = Data.data_frame
        
        return df

    # Export to SQLite3.
    def export_sql(self):
        """
        Exports pandas DataFrame to a SQLite3 database in the indicated
        directory.
        """
        
        directory = self.w.lne_dir.text()
        db_name = self.w.lne_db.text()
        self.w.table = self.w.lne_table.text()
        self.w.dir_db_name = directory + '\\' + db_name + '.db'
        self.df_to_sql()
        self.w.display_message()
        
    def df_to_sql(self):
        """From pandas DataFrame to SQLlite table."""
        
        db_name = self.w.lne_db.text()
        
        if db_name != '':
            
            try:
                df_sql = PandasDFSQLite(
                    self.w.df, self.w.dir_db_name, self.w.table
                    )
                df_sql.df_to_sql()
                
            except ValueError as e:
                self.w.message = str(e)
                
            else:
                self.w.message = 'Done!'
                
        else:
            self.w.message = 'Empty name of database'
