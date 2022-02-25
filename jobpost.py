#!/usr/bin/env python3
#
#

import sys
import re

class JobPost:
  """A class to keep track of each job posting and its relevant stats"""

  def __init__(self, company='', title='', location=''):
    self.company = company
    self.title = title
    self.location = location
    self.keywords = []
    self.score = 0

  def checkPost(self, jobtext, keywords):
    for word in keywords:
      if re.search(word, jobtext, flags=re.I):
        self.keywords.append(word)
        self.score += 1

def main():
  print('Testing JobPost class')
  job = JobPost('National Instruments', 'Digital Hardware Engineer', 'Austin, TX')
  text = "This job involves doing FPGA stuff. Embedded is cool too. VHDL? Nice!/nI love that."
  keywords = ['FPGA', 'PCB', 'Embedded', 'VHDL']
  job.checkPost(text, keywords)
  print(job.score, ':', job.keywords)

if __name__ == '__main__':
  main()