# Description
This is a quick-start for python and behave automation framework. It has everything setup to just start writing tests

# How to use it
* if you just need a skeleton framework to start writing tests or learning automation create a branch from master and start using the framework
* if you want to see a demo of how tests can be written and how the framework works change to the demoLibraryAppTesting branch

# About the framework
* it is currently setup for Rest Api testing and UI testing
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
* to map the models it is recommended to use the namedtuple data structure
* for the UI testing the Elementium lib has been integrated 

# Environment variables required
| variable key | variable description | possible values |
|--------------|----------------------|-----------------|
|env | the env you want to run on | dev, test, any other you setup |
|RP_TOKEN| the user access token for Report Portal|

