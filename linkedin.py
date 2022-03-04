#!/usr/bin/env python3
#
#

from jobboard import JobBoard
from jobpost import JobPost
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def safe_search(driver, byType, term, returnText=False):
  """try a driver.find_element search and catches exceptions
     a WebElement is returned by default (None if element not found)
     if returnText is True, the text of the WebElement is returned (or 'Not Found' string)"""
  try:
    results = driver.find_element(byType, term)
    if returnText:
      return results.text
    else:
      return results
  except:
    if returnText:
      return 'Not Found'
    else:
      return None


class LinkedIn(JobBoard):
  name = 'LinkedIn'
  url = 'https://www.linkedin.com'

  def job_search(self, browser, title, location, maxNumJobs):
    try:
      jobsLink = browser.find_element(By.ID, 'ember20')
      print('Navigating to jobs page')
      jobsLink.click()
    except:
      print('could not find jobs link') #TODO: make better
      
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
    print('searching...')

    page = 1
    jobCount = 0

    while jobCount < maxNumJobs:
      time.sleep(5) #wait for page to load. Some elements seem to load faster than others, which caused some race conditions.
        # hopefully adding some delay will prevent the server from blocking me

      try:
        panel = browser.find_element(By.CLASS_NAME, 'jobs-search-results')
        scrollOptions = "{top: arguments[0].scrollHeight, left: 0, behavior: 'smooth'}" # smooth behavior to make sure all the jobs load
        browser.execute_script('arguments[0].scroll({0})'.format(scrollOptions), panel)
        #scroll to bottom of results list to load all results on the page
        time.sleep(5) # wait to load the rest of the results
      except:
        print('job search results not found') #TODO: make better

      try:
        jobList = browser.find_elements(By.CLASS_NAME, 'job-card-list__title')
        print('jobs found:', len(jobList))
      except:
        print('No jobs found') #TODO: make better
      
      for job in jobList:
        if jobCount < maxNumJobs:
          job.click()
          time.sleep(1)
          post = JobPost()

          # find job information. If a piece of data cannot be found, it will by 'Not Found'
          post.title = safe_search(browser, By.CSS_SELECTOR, 'h2[class="t-24 t-bold"]', True)
          post.url = safe_search(safe_search(browser, By.CSS_SELECTOR, 'h2[class="t-24 t-bold"]'), By.XPATH, './..').get_property('href') # search parent node for href
            # url is contained in the parent node of the <h2>, but is too ambiguously named to be searched for directly
          post.company = safe_search(browser, By.CSS_SELECTOR, 'a[class="ember-view t-black t-normal"]', True) # TODO: use xpath to find these instead of font
          post.location = safe_search(browser, By.CSS_SELECTOR, 'span[class="jobs-unified-top-card__bullet"]', True)
          details = safe_search(browser, By.ID, 'job-details', True)
          post.check_post(details, self.keywords) #check keywords from the JobBoard superclass
          self.jobs.append(post)
          jobCount += 1
          # TODO: Consider return here if maxNumJobs is hit, then I could remove jobCount checks

      if jobCount < maxNumJobs:
        nextPage = safe_search(browser, By.CSS_SELECTOR, 'li[data-test-pagination-page-btn="{0}"]'.format(page+1))
        if nextPage != None:
          nextPage.click()
          page += 1
        else:
          print('reached end of results at page {0}'.format(page))
          return

def main():
  """test"""
  board = LinkedIn('jgmarsar', 'abc123')
  board.printDetails()

if __name__ == '__main__':
  main()