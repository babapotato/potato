from requests import get
import logging

URL_API = "http://api.covid19api.com"

def download_summary():
  
  # Send the request to url using the get method and store the response in response
  response = get(f'{URL_API}/summary')
  # Check response status for the code 200 (OK)
  if response.status_code == 200:
    # Do successAction
    logging.info('Successfully received Dutch data from COVID19 API')
    return response.json()
    
  # Otherwise, something went wrong
  else:
    # Do errorAction
    logging.error(f'an error has occured: HTTP status {response.status_code}')
    return {}


def download_confirmed_per_country(country):
  
  # Send the request to url using the get method and store the response in response
  response = get(f'{URL_API}/country/{country}/status/confirmed')
  # Check response status for the code 200 (OK)
  if response.status_code == 200:
    # Do successAction
    logging.info('Successfully received Dutch data from COVID19 API')
    return { "data" : response.json() }
    
  # Otherwise, something went wrong
  else:
    # Do errorAction
    logging.error(f'an error has occured: HTTP status {response.status_code}')
    return {}
  