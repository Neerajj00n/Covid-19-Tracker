import requests
import json
from .models import *
import time 
import pandas as pd
import datetime



def daily_report(date_string=None):
    # Reports aggegrade data, dating as far back to 01-22-2020
    # If passing arg, must use above date formatting '01-22-2020'
    report_directory = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'
    
    if date_string is None: 
        yesterday = datetime.date.today() - datetime.timedelta(days=2)
        file_date = yesterday.strftime('%m-%d-%Y')
    else: 
        file_date = date_string 
    
    df = pd.read_csv(report_directory + file_date + '.csv', dtype={"FIPS": str})
    return df

def daily_confirmed():
    # returns the daily reported cases for respective date, 
    # segmented globally and by country
    df = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/new_cases.csv')
    return df


def daily_deaths():
    # returns the daily reported deaths for respective date
    df = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/new_deaths.csv')
    return df


def confirmed_report():
    # Returns time series version of total cases confirmed globally
    df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    return df

def deaths_report():
    # Returns time series version of total deaths globally
    df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    return df

def recovered_report():
    # Return time series version of total recoveries globally
    df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    return d




