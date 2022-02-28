#!/usr/bin/env python3
#
#

import getpass
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from linkedin import LinkedIn

def main():
  # open browser
  browser = webdriver.Firefox()
  browser.implicitly_wait(5) #poll for five seconds whenever searching for an element
  board = LinkedIn('user', 'pw')
  board.keywords = ['FPGA', 'VHDL', 'Embedded', 'C\+\+', 'New York', 'hardware', 'PCB'] # styled for regex
  browser.get(board.url)

  input('continue when logged in') #TODO: make robust

  jobs = board.jobSearch(browser, 'Electrical Engineer', 'New York, New York')
  print(jobs)

  browser.quit()

if __name__ == '__main__':
  main()