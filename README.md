# **Home assignment amazon.ae**

## **About**
This is my solution for the home assessment sent on 20/09/2022.

The main goal is to validate  3 scenarios on the platform amazon.ae, these scenarios are related 
to the user sing in, products & basket and available pages for a signed-out user.

The chosen framework is made using  Selenium and Python-behave (BDD) with a POM approach.
Reports will be created using the JUnit formatter included in the framework.

## **Project structure**
* **Feature file** (Amazon/features/Assessment.feature) on which all the testing scenarios are located
* **Step definition file** (Amazon/features/steps/assessment.py) this is where the step snippets are located for each scenario
* **pages folder** (Amazon/pages) this is where the classes for each page are stored, each one holding the 
methods and variables used in the step definition file
* **resources folder** used for storing temporary files, webdrivers
* **reports folder** is where the JUnit reports will be stored after each execution
* **screenshots folder** all the screenshots for the failing tests will be stored here
* **enviornment.py** file (Amazon/features/environment.py) this is where the methods executed before and after a feature,
 scenario or step are stored
*  **requirements.txt** the used libraries and their version are located in this file

## **Requirements**

* Python 3
* chromedriver.exe for your Chrome browser version (https://chromedriver.chromium.org/downloads)
* Any IDE that supports python (this framework was created using Pycharm on a Windows computer https://www.jetbrains.com/pycharm/download)
* Gherkin plugin (installed in the IDE plugins section)

## **Setup**

* Install Python v ~= 3
* Install python compatible IDE
* Download chromedriver.exe (if needed, add the folder where this .exe is stored to path in environment variables)
* Open the IDE and install the libraries in the **requirements.txt** file
* At the top of the assessment.py file replace the content of the webdriver executable path ("chromedriver.exe")
with the complete path for your webdriver. IE. context.driver = webdriver.Chrome(executable_path="your_path/chromedriver.exe")

## **How to run test**

* **All scenarios:**

In the terminal send the command behave --junit Amazon/features

this will execute all the scenarios (and features) in the feature file

* **One scenario**
In the terminal send the command behave --junit Amazon/features -n 'Scenario name'

IE. behave --junit Amazon/features -n 'Validate that the items are added correctly to the cart'


## **Results**

* JUnit report can be found as an XML file in reports/TESTS-Assessment.xml
* Screenshots for failed tests can be found in Amazon/resources/screenshots 
each screenshot is named after the step in which it failed
