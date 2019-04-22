#!/bin/bash


#create virtual environment
python3 -m pip install --user virtualenv


#install virtual environment
python3 -m virtualenv venvtaxiapi 


#activate virtual environment
source venvtaxiapi/bin/activate


#install requirements
python -m pip install -r requirements.txt

