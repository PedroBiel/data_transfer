# -*- coding: utf-8 -*-
"""
Data transfer
From pandas DataFrame to Excel

Created on 07.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


import pandas as pd
# import xlsxwriter


class PandasDFXLSX:

    def __init__(self, df, dir_wb_name, ws_name):
        """
        Create a spreadsheet using the XlsxWriter module.
        https://xlsxwriter.readthedocs.io/index.html
        """
        
        self.df = df  # pandas DataFrame to convert.
        self.dir_wb_name = dir_wb_name  # Directory and name of the Excel workbook.
        self.ws_name = ws_name  # Name of the Excel worksheet.

    def df_to_excel(self):
        """Write the data to the Excel worksheet."""

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(self.dir_wb_name, engine='xlsxwriter')
        
        # Convert the dataframe to an XlsxWriter Excel object.
        self.df.to_excel(writer, sheet_name=self.ws_name)
        
        # Get the XlsxWriter workbook and worksheet objects.
        wb = writer.book
        ws = writer.sheets[self.ws_name]
        
        # Add some cell formats.
        format1 = wb.add_format()
        format1.set_align('center')

        # Set the column width and format.
        ws.set_column('A:A', 5, format1)
        ws.set_column('B2:D4', 10, format1)
        
        # Close the Pandas Excel writer.
        writer.save()
