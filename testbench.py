#!/usr/bin/env python3
#
# Test the functions other than web scraping

import getpass
import sys
import os
from linkedin import LinkedIn
from jobpost import JobPost
from xlsx_util import Spreadsheet

def main():
  board = LinkedIn('user', 'pw')
  board.keywords = ['FPGA', 'VHDL', 'Embedded', 'C\+\+', 'New York', 'hardware', 'PCB'] # styled for regex

  board.jobs.append(JobPost('Company1','EE','NYC'))
  board.jobs[0].score = 3
  board.jobs[0].keywords = ['FPGA', 'VHDL']
  board.jobs[0].url = 'url.com'

  board.jobs.append(JobPost('Company2','software','NYC'))
  board.jobs[1].score = 5
  board.jobs[1].keywords = ['FPGA', 'embedded C']
  board.jobs[1].url = 'url.com'

  resultsDir = 'results_test'
  if not os.path.exists(resultsDir):
    os.mkdir(resultsDir)
  path = os.path.join(os.getcwd(), resultsDir)
  workbook = Spreadsheet(path, 'Test')
  board.print_jobs_to_sheet(workbook)
  workbook.close_file()

if __name__ == '__main__':
  main()