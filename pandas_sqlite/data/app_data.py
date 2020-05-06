# -*- coding: utf-8 -*-
"""
Data transfer
From pandas DataFrame to SQLite

Created on 06.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


import pandas as pd


class Data:
    """Data of the application."""
    
    
    data_frame = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
        })
