#!/usr/bin/env python3
#
#

from jobboard import JobBoard
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

searchAll = False # True = go through full results list; False = just the first page

class LinkedIn(JobBoard):
  name = 'LinkedIn'
  url = 'https://www.linkedin.com'

  def jobSearch(self, browser, title, location):
    try:
      jobsLink = browser.find_element(By.ID, 'ember20')
      print('Navigating to jobs page')
      jobsLink.click()
    except:
      print('could not find jobs link') #TODO: make better
    #time.sleep(1)
      
    try:
      titleForm = browser.find_element(By.CLASS_NAME, 'jobs-search-box__input--keyword')
      titleForm = titleForm.find_element(By.CLASS_NAME, 'jobs-search-box__text-input')
      locationForm = browser.find_element(By.CLASS_NAME, 'jobs-search-box__input--location')
      locationForm = locationForm.find_element(By.CLASS_NAME, 'jobs-search-box__text-input')
      searchButton = browser.find_element(By.CLASS_NAME, 'jobs-search-box__submit-button')
    except:
      print('Search form not found') #TODO: make better
      
    titleForm.send_keys(title)
    locationForm.send_keys(location)
    searchButton.click() 

    page = 1
    results = []

    done = False
    while not done:
      time.sleep(2) #wait for page to load. Some elements seem to load faster than others, which caused some race conditions.

      try:
        panel = browser.find_element(By.CLASS_NAME, 'jobs-search-results')
        browser.execute_script('arguments[0].scroll(0,arguments[0].scrollHeight)', panel)
        #scroll to bottom of results list to load all results on the page
        time.sleep(1) # wait to load the rest of the results
      except:
        print('job search results not found') #TODO: make better

      try:
        jobList = browser.find_elements(By.CLASS_NAME, 'job-card-list__title')
      except:
        print('No jobs found') #TODO: make better
      
      for job in jobList:
        job.click()
        try:
          post = JobPost()
          post.title = browser.find_element(By.CSS_SELECTOR, 'h2[class="t-24 t-bold"]').text
          post.url = browser.find_element(By.CSS_SELECTOR, 'h2[class="t-24 t-bold"]').find_element(By.XPATH, './..').get_property('href') # search parent node for href
            # url is contained in the parent node of the <h2>, but is too ambiguously named to be searched for directly
          post.company = browser.find_element(By.CSS_SELECTOR, 'a[class="ember-view t-black t-normal"]').text # TODO: something better than finding these by font?
          post.location = browser.find_element(By.CSS_SELECTOR, 'span[class="jobs-unified-top-card__bullet"]').text
          details = browser.find_element(By.ID, 'job-details').text
          post.checkPost(details, self.keywords) #check keywords from the JobBoard superclass
          results.append(post)
        except:
          print('no details found')
      
      if searchAll:
        try:
          nextPage =  browser.find_element(By.CSS_SELECTOR, 'li[data-test-pagination-page-btn="{0}"]'.format(page+1))
          nextPage.click()
          page += 1
        except:
          print('reached end of results at page {0}'.format(page))
          done = True
      else:
        done = True

    return results



def main():
  """test"""
  board = LinkedIn('jgmarsar', 'abc123')
  board.printDetails()

if __name__ == '__main__':
  main()