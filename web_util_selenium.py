#!/usr/bin/env python3
#
#

import requests
import os
import sys
import subprocess
import webbrowser
from urllib.parse import urljoin
from selenium import webdriver
import getpass
from selenium.webdriver.common.by import By

# open browser
browser = webdriver.Firefox()

def download_open_url(url):
  r = requests.get(url, allow_redirects=True)
  local = 'temp.html'
  open(local, 'wb').write(r.content)
  try:
    subprocess.check_output(local, shell=True)
    print('Success!')
  except subprocess.CalledProcessError as e:
    print(e.output)
    sys.exit(1)
  return
  
  
  #https://www.selenium.dev/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webelement.html?
  
username = 'jgmarsar@gmail.com'
  
def login(url):
  password = getpass.getpass()
  print('Opening url')
  browser.get(url)
  
  try:
    loginForm = browser.find_element(By.CLASS_NAME, 'sign-in-form') # find login element
    userElem = loginForm.find_element(By.NAME, 'session_key')
    passwordElem = loginForm.find_element(By.NAME, 'session_password')
  except:
    print('Login form not found')
    
  userElem.send_keys(username) # Find username and input email
  passwordElem.send_keys(password) #Find pw and enter
  loginForm.submit() #Submits the form; could have used userElem or passwordElem
  input('Opening webpage. Check for human verification and press return when ready')  
  
def jobSearch(title):
  try:
    jobsLink = browser.find_element(By.ID, 'ember20')
    jobsLink.click()
  except:
    print('could not find jobs link')
    
  try:
    titleForm = browser.find_element(By.CLASS_NAME, 'jobs-search-box__input--keyword')
    titleForm = titleForm.find_element(By.CLASS_NAME, 'jobs-search-box__text-input')
    locationForm = browser.find_element(By.CLASS_NAME, 'jobs-search-box__input--location')
    locationForm = locationForm.find_element(By.CLASS_NAME, 'jobs-search-box__text-input')
    searchButton = browser.find_element(By.CLASS_NAME, 'jobs-search-box__submit-button')
  except:
    print('Search form not found')
    
  titleForm.send_keys(title)
  locationForm.send_keys('New York City')
  searchButton.click() 
  return

def parseJobs():
  #create a list of job links
  #go to each link, click it and locate the job description
  #parse the page for key words, location
  #in original job list, go to the next page of jobs
  try:
    jobList = browser.find_elements(By.CLASS_NAME, 'job-card-list__title')
  except:
    print('No jobs found')
  
  for job in jobList:
    job.click()
    details = browser.find_element(By.ID, 'job-details').text
    print(details[:20])
    
  return
  
def main():
  args = sys.argv[1:]
  #run test of this util
  
  if not args:
    print('usage: [--open] url')
    sys.exit(1)
    
  if args[0] == '--open':
    download_open_url(args[1])
  else:
    details = login(args[0])
    jobSearch('Electrical Engineer')
    #submit_form(details[0], args[0])
    
  input('Finished. Return to close browser')
  browser.quit()
  

if __name__ == '__main__':
  main()