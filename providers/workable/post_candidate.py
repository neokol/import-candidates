import requests
import os
from dotenv import load_dotenv

load_dotenv() 

token = os.getenv('BEARER_KEY')
subdomain = os.getenv('SUBDOMAIN')

def post_candidate(candidate_data, job_shortcode):
        url = f"https://{subdomain}.workable.com/spi/v3/jobs/{job_shortcode}/candidates"
    
        headers = {
        "accept": "application/json",
        "Authorization": f"{token}"
        }
        
        response = requests.post(url, headers=headers, json={'candidate': candidate_data})
        if response.status_code == 201:
            return response.status_code
        else:
            print(f"Error {response.status_code}: {response.text}")
            return response.status_code