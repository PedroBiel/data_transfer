# -*- coding: utf-8 -*-
"""
Data transfer
From SQLite to pandas DataFrame

Created on 07.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


import pandas as pd
import sqlite3


class SQLitePandasDF:

    def __init__(self, dir_db_name, table):
        """
        Transfer data from a SQLite database to a pandas DataFrame.
        The path and the name of the database are one and the same parameter
        (one string).
        The name of the database has the extension.
        """
    
        self.dir_db_name = dir_db_name  # Directory and name of the database with extension.
        self.table = table  # Table of the database.

    def sql_to_df(self):
        """Read the SQLite3 database into the pandas DataFrame."""
        
        conn = sqlite3.connect(self.dir_db_name)
        df = pd.read_sql('SELECT * FROM ' + self.table + ';', conn)
            
        return df


class SQLitePandasDF2:

    def __init__(self, directory, db_name, table):
        """
        Transfer data from a SQLite database to a pandas DataFrame.
        The path and the database name are two different parameters (two
        strings).
        The name of the database does not have the extension.
        """
    
        self.dir = directory  # Directory where the database is located.
        self.db_name = db_name  # name of the database without extension.
        self.table = table  # Tabla de la base de datos.

    def sql_to_df(self):
        """Read the SQLite3 database into the pandas DataFrame."""
        
        db = self.dir + '/' + self.db_name + '.db'
        conn = sqlite3.connect(db)
        df = pd.read_sql('SELECT * FROM ' + self.tbl + ';', conn)

        return df
