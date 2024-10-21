import requests
import os
from dotenv import load_dotenv

load_dotenv() 

token = os.getenv('BEARER_KEY')
subdomain = os.getenv('SUBDOMAIN')


class Job:
    def __init__(self, title, shortcode):
        self.title = title
        self.shortcode = shortcode


class RequestJobs:
    
    def fetch_jobs(self):
        url = f"https://{subdomain}.workable.com/spi/v3/jobs?limit=50"

        headers = {
        "accept": "application/json",
        "Authorization": f"{token}"
        }

        response = requests.get(url, headers=headers)
        
        
        if response.status_code == 200:
            jobs_data = response.json()
            if jobs_data:
                jobs_list = jobs_data.get('jobs', [])
                jobs = []
                for job in jobs_list:
                    title = job.get('title')
                    shortcode = job.get('shortcode')
                    if title and shortcode:
                        job_obj = Job(title, shortcode)
                        jobs.append(job_obj)
                        # print(f"Title: {job_obj.title}, Shortcode: {job_obj.shortcode}")
        return jobs


