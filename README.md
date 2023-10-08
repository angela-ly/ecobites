# Ecobites Backend 


## Overview
TBU 


## Initial Setup 
These steps have been completed. You will need to only activate the environment to run the code. 
Visit the [freeCodeCamp for more info](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/).
Virtualenv is a tool to set up your Python environments. You can install venv to your host Python by running this command in your terminal:
        pip3 install virtualenv   

To use venv in your project, in your terminal, create a new project folder, cd to the project folder in your terminal, and run the following command:
         python<version> -m venv <virtual-environment-name>

To activate your virtual environment, run the code below:
        source env/bin/activate

Generate a text file listing all your project dependencies by running the code below:
        pip3 freeze > requirements.txt



## Running the backend 
First activate your virtual environment, run the code below:
        source env/bin/activate


Instead of having to install each dependency one by one, they could just run the code below to install all your dependencies within their own copy of the project:
        > ~ pip3 install -r requirements.txt


To deactivate your virtual environment, simply run the following code in the terminal:
         ~ deactivate


Flask needs to know, the .py file to run. So run that command:
         export FLASK_APP=ecobites.py

To run the application:
         flask run