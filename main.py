#!/usr/bin/env python3
#
#

import getpass
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from linkedin import LinkedIn
from jobpost import JobPost
from xlsx_util import Spreadsheet

def main():
  # open browser
  browser = webdriver.Firefox()
  browser.implicitly_wait(5) #poll for five seconds whenever searching for an element
  board = LinkedIn('user', 'pw')
  board.keywords = ['FPGA', 'VHDL', 'Embedded', 'C\+\+', 'hardware', 'PCB', 'Electrical', 'oscilloscope', '(SPI|I2C)', \
    'LabVIEW', 'sustainability', 'serial', '(digital|computer)', 'micro(controller|processor)'] # styled for regex
  browser.get(board.url)

  input('continue when logged in') #TODO: make robust

  location = 'New York, New York'
  board.job_search(browser, 'Electrical Engineer', location, 100)
  board.job_search(browser, 'Embedded Engineer', location, 100)
  board.job_search(browser, 'Firmware Engineer', location, 100)
  board.job_search(browser, 'Computer Hardware Engineer', location, 100)

  resultsDir = 'results'
  if not os.path.exists(resultsDir):
    os.mkdir(resultsDir)
  path = os.path.join(os.getcwd(), resultsDir)
  workbook = Spreadsheet(path, 'Search')
  board.print_jobs_to_sheet(workbook)
  workbook.close_file()

  browser.quit()

if __name__ == '__main__':
  main()