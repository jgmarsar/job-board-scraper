#!/usr/bin/env python3
#
#

import sys

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
    if not hasattr(self, 'name'):
      raise NotImplementedError('Sublass is missing name definition')
    if not hasattr(self, 'url'):
      raise NotImplementedError('Sublass is missing url definition')

  keywords = [] # list of keywords to look for in each job description. It's okay that this will be the same list for all boards

  def printDetails(self):
    print(self.name)
    print(self.url)
    print(self.user)
    print(self.pw)

  def jobSearch(self):
    raise NotImplementedError('jobSearch() must be implemented by subclass')
