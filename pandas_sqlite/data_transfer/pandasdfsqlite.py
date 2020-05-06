# -*- coding: utf-8 -*-
"""
Data transfer
From pandas DataFrame to SQLite

Created on 06.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


import sqlite3


class PandasDFSQLite:

    def __init__(self, df, dir_db_name, table):
        """Transfers data from a pandas DataFrame to a SQLite data base."""
        
        self.df = df  # pandas DataFrame to convert.
        self.dir_db_name = dir_db_name  # Directory and name of the database.
        self.table = table  # Table of the database.

    def df_to_sql(self):
        """Writes records stored in a DataFrame to a SQL database."""

        conn = sqlite3.connect(self.dir_db_name)
        self.df.to_sql(self.table, conn, if_exists='replace', index=False)
