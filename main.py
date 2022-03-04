#!/usr/bin/env python3
#
#

import getpass
import sys

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
  board.keywords = ['FPGA', 'VHDL', 'Embedded', 'C\+\+', 'hardware', 'PCB', 'Electrical', 'oscilloscope', 'SPI'] # styled for regex
  browser.get(board.url)

  input('continue when logged in') #TODO: make robust

  board.job_search(browser, 'Firmware Engineer', 'New York, New York', 30)

  workbook = Spreadsheet('Search')
  board.print_jobs_to_sheet(workbook)
  workbook.close_file()

  browser.quit()

if __name__ == '__main__':
  main()