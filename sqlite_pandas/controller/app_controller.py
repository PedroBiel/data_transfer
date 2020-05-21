# -*- coding: utf-8 -*-
"""
Data transfer
From SQLite to pandas DataFrame

Created on 07.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


from data_transfer.sqlitepandasdf import SQLitePandasDF


class Controller:
    
    def __init__(self, mainwindow):
        """Controller of the apllication."""
        
        self.w = mainwindow

    # Import SQLite3 database.
    def import_sql(self):
        """Import SQLite3 database to pandas DataFrame."""
        
        directory = self.w.lne_dir.text()
        db_name = self.w.lne_db.text()
        self.w.dir_db_name = directory + '\\' + db_name + '.db'
        self.w.table = self.w.lne_table.text()
        self.sql_to_df()
        self.w.display_dataframe()
        self.w.display_message()
        
    def sql_to_df(self):
        """From SQLlite table to pandas DataFrame."""
        
        db_name = self.w.lne_db.text()
        table = self.w.lne_table.text()
        
        if (db_name != '') and (table != ''):
            print('\n db_name 1:', db_name != '')
            print('\n table 1:', table != '')
            
            try:
                sql_pd = SQLitePandasDF(self.w.dir_db_name, self.w.table)
                self.w.df = sql_pd.sql_to_df()
                
            except ValueError as e:
                self.w.message = str(e)
                
            else:
                self.w.message = 'Done!'
                
        else:
            self.w.df.drop(self.w.df.index, inplace=True)
            self.w.message = 'Empty name of database and/or table'
            print('\n db_name 2:', db_name)
            print('\n table 2:', table)
        
        
        
        
        
        

        

    # def get_dataframe(self):
    #     """Get the pandas DataFrame."""
        
        
    #     self.df_to_sql()
    #     self.w.display_message()
        
        
        
        
    #     dir_db_name = self.lne_dir + '\\' + self.lne_db
        
        
        
        
    #     df = Data.data_frame
        
    #     return df

    # # Export to SQLite3.
    # def export_sql(self):
    #     """
    #     Export pandas DataFrame to a SQLite3 database in the indicated
    #     directory.
    #     """
        
    #     directory = self.w.lne_dir.text()
    #     db_name = self.w.lne_db.text()
    #     self.w.table = self.w.lne_table.text()
    #     self.w.dir_db_name = directory + '\\' + db_name + '.db'
    #     self.df_to_sql()
    #     self.w.display_message()
        
    # def df_to_sql(self):
    #     """From pandas DataFrame to SQLlite table."""
        
    #     db_name = self.w.lne_db.text()
        
    #     if db_name != '':
            
    #         try:
    #             df_sql = PandasDFSQLite(
    #                 self.w.df, self.w.dir_db_name, self.w.table
    #                 )
    #             df_sql.df_to_sql()
                
    #         except ValueError as e:
    #             self.w.message = str(e)
                
    #         else:
    #             self.w.message = 'Done!'
                
    #     else:
    #         self.w.message = 'Empty name of database'
