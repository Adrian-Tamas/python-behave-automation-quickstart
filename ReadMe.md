# Description
This is a quick-start for python and behave automation framework. It has everything setup to just start writing tests

# How to use it
* if you just need a skeleton framework to start writing tests or learning automation create a branch from master and start using the framework
* if you want to see a demo of how tests can be written and how the framework works change to the demoLibraryAppTesting branch and from command line run run_behave.py script to execute all tests
or add tags (e.g. --tags=@ui) to execute specific test suite.

# About the framework
* it is currently setup for Rest Api testing, database testing and UI testing
* it is configured to run on a couple of different environments controlled through the config.ini files but adding a new one is very simple:
    * add a new config file and name it as you want while setting up all the values from an existing one specific for this new env
    * add a new env config file in the /configuration folder keeping the naming convention \<env\>_configuration.py
    * based on the env environment variable the correct configuration will be used
* it is configured to run with support for report portal. In order to use report portal:
    * update the link and the project in the config file
    * set the access token of your user in the RP_TOKEN env variable
    * run the tests with the _-Drp_enabled=True_ user flag

# Libs used
* for api testing the builtin _requests_ lib is used
* to map the models it is recommended to use the _namedtuple_ data structure
* for the UI testing the _Selenium_ lib has been integrated 
* for working with the database the _sqlalchemy_ lib has been added

# Environment variables required
| variable key | default | variable description | possible values |
|--------------|---------|----------------------|-----------------|
|env | dev | the env you want to run on | dev, test, any other you setup |
|RP_TOKEN| None | the user access token for Report Portal|

# Command line options to configure execution
As with any command line option use -D<argument>=value to pass it to the execution 

|  argument name | default | variable description | possible values |
|----------------|---------|----------------------|-----------------|
|browser | chrome | the browser to use for UI tests | existing: chrome, firefox, edge; any other you add |
|rp_enabled | False | enable test output to ReportPortal|True or False |
|step_based | True | enable step based reporting for ReportPortal. Scenario level reporting if False | True or False |
|add_screenshot| False | capture screenshot and add it to the reporting for ReportPortal | True or False |