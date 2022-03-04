#!/usr/bin/env python3
#
#

import sys
import re

list_format = ['Company', 'Title', 'Location', 'Score', 'Keywords', 'URL']

class JobPost:
  """A class to keep track of each job posting and its relevant stats"""

  def __init__(self, company='', title='', location=''):
    self.company = company
    self.title = title
    self.location = location
    self.age = 0
    self.url = '' # url of job post
    self.keywords = [] # Do I really need to keep track of the matches?
    self.score = 0
    #Could potentially have multiple scores associated with different keyword lists. Such as hardware score and software score, derived from separate keywords.
      #I would make score a dictionary of the form 'category': score. Or maybe category isn't worth storing for each job post, since it will be the same for all of them.
      #It could just be a list of scores implicitly associated with each category
    #Add a 'years experience' variable? Would need to search for common patterns to find that number in a job description
    #negative score? With keywords to avoid
    #I'm not saving the full text because I don't really need it after I parse it.

  def check_post(self, jobtext, keywords):
    self.score = 0
    for word in keywords:
      if re.search(word, jobtext, flags=re.I): # search for keywords, ignoring case
        self.keywords.append(word)
        self.score += 1

  def get_score(self):
    # useful for sorting by score
    return self.score

  def __str__(self):
    # essentially print(self)
    printout = 'Title: ' + self.title
    printout += '\nCompany: ' + self.company
    printout += '\nLocation: ' + self.location
    printout += '\nURL: ' + self.url
    printout += '\nScore: ' + str(self.score) + ': ' + ', '.join(self.keywords)
    return printout

  def get_list(self):
    # in list_format order
    return [self.company, self.title, self.location, self.score, ', '.join(self.keywords), self.url]

def main():
  print('Testing JobPost class')
  job = JobPost('National Instruments', 'Digital Hardware Engineer', 'Austin, TX')
  text = "This job involves doing FPGA stuff. Embedded is cool too. VHDL? Nice!/nI love that."
  keywords = ['FPGA', 'PCB', 'Embedded', 'VHDL']
  job.checkPost(text, keywords)
  print(job)

if __name__ == '__main__':
  main()