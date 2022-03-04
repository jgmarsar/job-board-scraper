#!/usr/bin/env python3
#
#

import sys
from jobpost import JobPost
import jobpost
import xlsx_util
from openpyxl.styles import Font

class JobBoard:
  """
  This is intended to be used with a subclass only. All of the variables will be overwritten. This will likely be edited once I make a subclass.
  I may find that this parent class is only necessary to enforce certain attributes of its subclasses.
  Subclass required defitions:
  name
  url
  jobSearch()
  """
  def __init__(self, user, pw):
    self.user = user
    self.pw = pw
    self.jobs = []
    if not hasattr(self, 'name'):
      raise NotImplementedError('Sublass is missing name definition')
    if not hasattr(self, 'url'):
      raise NotImplementedError('Sublass is missing url definition')

  keywords = [] # list of keywords to look for in each job description. It's okay that this will be the same list for all boards
  # keywords = {} # dictionary could be of the form "category": ['keyword1','keyword2','keyword3'] to have multiple scores based on different types of keywords
    # for example, I might rank job posts based on hardware keywords and software keywords separately

  def print_details(self):
    print(self.name)
    print(self.url)
    print(self.user)
    print(self.pw)

  def job_search(self):
    raise NotImplementedError('jobSearch() must be implemented by subclass')

  def print_jobs_to_sheet(self, workbook):
    self.jobs = sorted(self.jobs, key=JobPost.get_score, reverse=True) # sort job list by score in descending order
    workbook.add_sheet(self.name)
    workbook.add_row(jobpost.list_format, Font(bold=True)) # Add header row
    for job in self.jobs:
      workbook.add_row(job.get_list()) # print each job in a new row

