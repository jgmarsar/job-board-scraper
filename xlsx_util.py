#!/usr/bin/env python3
#
#

from operator import itemgetter
import sys
import openpyxl
from openpyxl.styles import Font
from datetime import date

class Spreadsheet():

  def __init__(self, name):
    self.workbook = openpyxl.Workbook()
    today = date.today().strftime('%Y-%m-%d')
    self.filename = name + '-' + today + '.xlsx' #save workbook in format 'name-YYYY-MM-DD.xlsx'
    self.workbook.save(self.filename) 
    self.workbook['Sheet'] #delete default sheet, we'll add them as we need

  def add_sheet(self, name):
    self.workbook.active = self.workbook.create_sheet(title=name)
    self.workbook.active['A1'] = self.filename + ': ' + name
    self.workbook.save(self.filename)

  def add_row(self, data, font=None):
    sheet = self.workbook.active
    newrow = sheet.max_row + 1
    for index, item in enumerate(data):
      sheet.cell(row=newrow, column=index+1).value = item
      if font != None:
        sheet.cell(row=newrow, column=index+1).font = font
    self.workbook.save(self.filename)
  
  def close_file(self):
    self.workbook.save(self.filename)
    self.workbook.close()
