from requests import get
import logging

def download_summary():
  
  # Send the request to url using the get method and store the response in response
  response = get("http://api.covid19api.com/summary")
  # Check response status for the code 200 (OK)
  if response.status_code == 200:
    # Do successAction
    return response.json()
    
  # Otherwise, something went wrong
  else:
    # Do errorAction
    logging.error(f'an error has occured: HTTP status {response.status_code}')
    return {}
