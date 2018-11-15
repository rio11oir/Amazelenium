# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14, 2018
@author: River Wong
For the Symbility Intersect Software Engineer in Test Code Challenge Problem
"""

# THINGS TO CHANGE:
logFile = "/test/testLog.csv"

startingPage = "http://www.amazon.ca"
chromeDriverPath = "../drivers/chromedriver.exe"

testUsername = "rwTest"
testEmail = "rwasdf@gmail.com"
testPassword = "thisarealtest"

testStatus = ""
reason = ""

searchText = "memory card" # for Use Case 3
searchTextNonEx = "[alpja]" # for Use Case 4
itemText = "Sandisk Ultra 32GB Class 10 SDHC UHS-I Memory Card Up to 80MB, Grey/Black (SDSDUNC-032G-GN6IN)" # for Use Case 5

sleepTime = 0 # The script will sleep for this amount of seconds at the start of each page


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import re

# Use case 1: See "Sign in"
def use_case_1():
    driver.get(startingPage)
    time.sleep(sleepTime)
    accountElem = driver.find_element_by_id("nav-link-yourAccount")
    accountText = accountElem.text

    if not accountElem.is_displayed():
        testStatus = "failed"
        reason = "\"Your Account\" button is not displayed"
    elif re.match("Hello, [a-zA-Z0-9]+\nYour Account", accountText):
        # signout and return to page
        ActionChains(driver).move_to_element(accountElem).perform()
        time.sleep(0.5)
        driver.find_element_by_id("nav-item-signout").click()
        time.sleep(sleepTime)
        driver.get(startingPage)
        time.sleep(sleepTime)
    elif accountText != "Hello. Sign in\nYour Account":
        print("failed")
        testStatus = "failed"
        reason = "\"Hello. Sign In. Your Account\" is not displayed"



# Use case 2: Sign in
def use_case_2():
    use_case_1()
    accountElem = driver.find_element_by_id("nav-link-yourAccount")
    accountElem.click()
    time.sleep(sleepTime)

    signIn()

def signIn():
    emailField = driver.find_element_by_id("ap_email")
    passwordField = driver.find_element_by_id("ap_password")
    signInSubmitButton = driver.find_element_by_id("signInSubmit")

    """
    if not emailField.is_displayed():
        testStatus = "failed"
        reason = "\"The email\" textbox is not displayed"
    elif not passwordField.is_displayed():
        testStatus = "failed"
        reason = "\"The password\" textbox is not displayed"
    elif not signInSubmitButton.is_displayed():
        testStatus = "failed"
        reason = "\"The Sign In\" button is not displayed"
    """

    emailField.send_keys(testEmail)
    passwordField.send_keys(testPassword)
    signInSubmitButton.click()

# Use case 3: Search
def use_case_3():
    driver.get(startingPage)
    time.sleep(sleepTime)
    searchBox = driver.find_element_by_id("twotabsearchtextbox")

    searchBox.send_keys(searchText + "\n")
    #notice items come up: s-results-list-atf


# Use case 4: Search for non-existent item
def use_case_4():
    driver.get(startingPage)
    time.sleep(sleepTime)
    searchBox = driver.find_element_by_id("twotabsearchtextbox")

    searchBox.send_keys(searchTextNonEx + "\n")
    #notice no items come up: noResultsTitle, "Your search "[alpja]" did not match any products."


# Use case 5: Add to cart and Proceed to checkout
def use_case_5():
    use_case_3()
    driver.find_element_by_xpath("//*[@title='" + itemText + "']").click()
    time.sleep(sleepTime)

    driver.find_element_by_id("add-to-cart-button").click()
    time.sleep(sleepTime)
    driver.find_element_by_id("hlb-ptc-btn-native").click()
    time.sleep(sleepTime)
    signIn()


print("Welcome to Amazelenium, where you can use a Selenium program to do exactly around 5 things with Amazon. Amazing right?!?")
print("Options:\n    - '1' Run use case 1: See 'Sign in'\n    - '2' Run use case 2: Sign in\n    - '3' Run use case 3: Search\n    - '4' Run use case 4: Search for non-existent item\n    - '5' Run use case 5: Add to cart and Proceed to checkout\n    - 'slower' Adds 1 second to the wait time at the start of each new page\n    - 'exit' to exit the script")
while(True):
    userInput = input("Please input the number for the use case you would like to run: ")

    if userInput == '1' or userInput == '2' or userInput == '3' or userInput == '4' or userInput == '5':
        driver = webdriver.Chrome(chromeDriverPath)

    if userInput == '1':
        print("Running use case 1...")
        use_case_1()
        print("Done!")
    elif userInput == '2':
        print("Running use case 2...")
        use_case_2()
        print("Done!")
    elif userInput == '3':
        print("Running use case 3...")
        use_case_3()
        print("Done!")
    elif userInput == '4':
        print("Running use case 4...")
        use_case_4()
        print("Done!")
    elif userInput == '5':
        print("Running use case 5...")
        use_case_5()
        print("Done!")
    elif userInput == 'slower':
        sleepTime += 1
        print("Done!")
    elif userInput == 'exit':
        break
    else:
        print("Input not recognized. Please try again.\n")
        time.sleep(1)
        print("Options:\n    - '1' Run use case 1: See 'Sign in'\n    - '2' Run use case 2: Sign in\n    - '3' Run use case 3: Search\n    - '4' Run use case 4: Search for non-existent item\n    - '5' Run use case 5: Add to cart and Proceed to checkout\n    - 'slower' Adds 1 second to the wait time at the start of each new page\n    - 'exit' to exit the script")


    # Unnecessary logging feature
    """
    logAdd = logAdd

    # Append to log
    log = open(logFile, "a")
    log.write(logAdd)
    log.close()

    # Reset Variables
    logAdd = "\n"
    """

#driver.quit()

print("Clean up complete! :D Pls hire me")