# SauceSwagLabs
This repo is for demonstrating how to use [Selenium](https://www.selenium.dev/documentation/overview/) and [unittest](https://docs.python.org/3/library/unittest.html) for UI testing. The website used is from [SauceLabs](https://www.saucedemo.com/v1/index.html)

## Creating the virtual Environment
Once the repo has been downloaded, execute the following command:

### **>python3 -m venv ./venv**

Note that ./venv is the name of the directory for your virtual environment, so it's name can be changed. Next, execute the following command:

### **>python3 -m pip install -r requirements.txt**

This will install the required packages needed to execute the test cases for the provided website.


## Executing the Script
Provided you are in the repo, run the following command:
### **>python3 sauce_demo_test.py**

Note that in this file, a webdriver for the Safari browser is used, but can be changed to one for Chrome or Firefox.
