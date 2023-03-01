#asu job application automation bot
#AUTHOR: CHARLES SHEELAM
#DATE: 12/29/22
#DESCRIPTION: BOT TO AUTOMATE SUBMISSION OF JOB APPLICATIONS ON ASU'S JOB PORTAL

#imports
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

postings = [] #contain all postings
postingUrls = [] #contain url to each job posting

sleepTime = 2
website = "https://shibboleth2.asu.edu/idp/profile/SAML2/Unsolicited/SSO?providerId=https%3A%2F%2Fsso.brassring.com%2Fsso%2Fsaml%2FSAML2PageListener%2FAuthenticationRequestor.aspx%3FLocation%3D5495"
class bot():
    def __init__(self):
        self.driver = driver = webdriver.Chrome(executable_path=r'D:\Users\sheel\Downloads\chromedriver_win32 (2)\chromedriver.exe')

    def openPage(self):

        self.driver.get(website)
        inputUserIdButton = self.driver.find_element(By.ID, "username")
        inputUserIdButton.send_keys("enter your username")
        inputUserPassword = self.driver.find_element(By.ID, "password")
        inputUserPassword.send_keys("enter your password")
        signInButton = self.driver.find_element(By.NAME, "submit")
        signInButton.click()
        sleep(21)
        jobField = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[7]/div[3]/div/div[1]/div[2]/div/div/div[1]/div[1]/div[1]/span/span/span/input")
        #jobField.send_keys("Computer")
        searchButton = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[7]/div[3]/div/div[1]/div[2]/div/div/div[1]/button")
        searchButton.click()
        
        sleep(10)

        jobsNumber = 5

        for x in range (1, jobsNumber + 1):
            currXpath = '/html/body/div[3]/div[2]/div[1]/div[7]/div[3]/div/div/div[4]/div[2]/div/div[1]/ul/li['+ str(x) +']/div[2]/div[2]/span/a'
            #print(currXpath)
            currentListing = self.driver.find_element(By.XPATH, currXpath)
            postingUrls.append(currentListing.get_attribute('href'))


        #i = 1 #to contrl window switching
        
        for currUrl in postingUrls:

            
            self.driver.execute_script("window.open('');")
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.get(currUrl)
            applyButton = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[7]/div[4]/div[2]/div/div[3]/div/div/div/div/button[1]')
            applyButton.click()
            #sleep(sleepTime)
            letsGetStartedButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[7]/div[3]/form/div/div[1]/div[4]/button'))).click()
            sleep(10)
            saveAndContinueButton1 = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[7]/div[3]/form/div/div[1]/div[4]/button')
            saveAndContinueButton1.click()
            #standard application questions
            radioB1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[7]/div[3]/form/div/div[1]/div[2]/div/div/div/div/div/div[2]/fieldset/div/div[2]/input'))).click()
            radioB2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[7]/div[3]/form/div/div[1]/div[2]/div/div/div/div/div/div[6]/fieldset/div/div[2]/input'))).click()
            menu1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[7]/div[3]/form/div/div[1]/div[2]/div/div/div/div/div/div[7]/span[2]/span[2]'))).click()
            selection = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[7]/div[5]/div[1]/ul/li[4]/div'))).click()
            saveAndContinueButton2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[7]/div[3]/form/div/div[1]/div[4]/button'))).click()
            #contact information page
            addResumeB = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[7]/div[3]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div[2]/div[1]/p/a'))).click()
            #sleep(10)
            self.driver.switch_to.frame("profileBuilder")
            savedResumesB = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[4]/button'))).click()
            selectedResumeRadio = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[3]/div/div[1]/fieldset/legend/div[6]/input'))).click()
            sleep(1)
            addFileB = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[3]/div/div[2]/button'))).click()
            self.driver.switch_to.window(self.driver.window_handles[0])
            sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[1])
                #add cover letter
            addCoverLetterB = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[7]/div[3]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[4]/div/div/div[3]/p/a'))).click()
            self.driver.switch_to.frame("profileBuilder")
            savedCoverLetterB = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[4]/button'))).click()
            coverLetterRadio = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[3]/div/div[1]/fieldset/legend/div[14]/input'))).click()
            addFileB2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[3]/div/div[2]/button'))).click()
            saveAndContinueButton3 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[7]/div[3]/form/div/div[1]/div[4]/button'))).click()
            #attachments page
            sleep(2)
            saveAndContinueButton4 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[7]/div[3]/form/div/div[1]/div[4]/button'))).click()
            #references page
            sleep(2)
            saveAndContinueButton5 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[7]/div[3]/form/div/div[1]/div[4]/button'))).click()
            #EEO page
            sleep(2)
            saveAndContinueButton6 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[7]/div[3]/form/div/div[1]/div[4]/button'))).click()
            #eeo race page
            sleep(2)
            saveAndContinueButton7 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[7]/div[3]/form/div/div[1]/div[4]/button'))).click()
            #review page
            sleep(2)
            sendApplicationButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[7]/div[3]/form/div/div[1]/div[4]/button'))).click()
            
            #temporary break
            break

#main
newBot = bot()
newBot.openPage()


