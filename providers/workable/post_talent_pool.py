import requests
from requests.exceptions import RequestException
import os
from dotenv import load_dotenv

token = os.getenv('BEARER_KEY')
subdomain = os.getenv('SUBDOMAIN')

def post_talent_pool(candidate_data:dict):
        url = f"https://{subdomain}.workable.com/spi/v3/talent_pool/candidates"
    
        headers = {
        "accept": "application/json",
        "Authorization": f"{token}"
        }
        
        try:
            response = requests.post(url, headers=headers, json={'candidate': candidate_data})
            response.raise_for_status() 
            if response.status_code == 201:
                return response.status_code, None
            else:
                # Extract error details from the response
                error_info = response.json().get('error', response.text)
                return response.status_code, error_info
        except requests.exceptions.RequestException as e:
            # Handle any request exceptions
            return None, str(e)