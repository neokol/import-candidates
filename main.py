from fastapi import FastAPI, HTTPException, UploadFile, File
import os
from dotenv import load_dotenv

from csv_parser.parser import CSVParser
from csv_parser.transformer import DataTransformer
from helpers.get_shortcode import get_shortcode_for_job_title
from providers.workable.get_jobs import RequestJobs
from providers.workable.post_candidate import post_candidate
from providers.workable.post_talent_pool import post_talent_pool

app = FastAPI(
    title="Task 2 - Workable Assignment",
    description="Upload Candidates with Wokable API",
    version="0.0.1",
    contact={
        "name":"Neoklis Kollias",
        "email":"ineokol@gmail.com"
    }
)

load_dotenv() 

@app.post("/upload_candidates")
async def upload_candidates(file: UploadFile = File(...)):
    
        # Validate file type
        if not file.filename.endswith('.csv'):
            raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV file.")

        your_first_name = os.getenv('FIRST_NAME')
        your_surname = os.getenv('LAST_NAME')

        # Create instances of the parser and transformer
        parser = CSVParser()
        transformer = DataTransformer(your_first_name, your_surname)
        
        parsed_data = parser.parse(file.file)  

        # Transform the data
        transformed_data, job_title = transformer.transform(parsed_data)
        print(transformed_data)
        job_fetcher = RequestJobs()
        jobs = job_fetcher.fetch_jobs()
        job_title_to_shortcode = {job.title: job.shortcode for job in jobs}

        print(job_title_to_shortcode)

        shortcode = get_shortcode_for_job_title(job_title=job_title, job_title_to_shortcode = job_title_to_shortcode)

        
        # Initialize lists to collect results
        success_candidates = []
        failed_candidates = []
        for candidate in transformed_data:
            try:
                post = post_candidate(candidate_data=candidate,job_shortcode=shortcode )
                if post == 201:
                    print(f"Candidate '{candidate['name']}' created successfully.")
                    success_candidates.append(candidate['name'])
                else:
                    print(f"Failed to create candidate '{candidate['name']}'. Status code: {post}")
                    failed_candidates.append(candidate['name'])
            except Exception as e:
                print(f"Exception occurred while processing candidate '{candidate['name']}': {e}")
                failed_candidates.append(candidate['name'])
                
        # Prepare the response
        return {
            "message": "File processed successfully",
            "total_candidates": len(transformed_data),
            "successful_imports": success_candidates,
            "failed_imports": failed_candidates
        }
        

    


@app.post("/upload_talent_pool")
async def upload_talents(file: UploadFile = File(...)):
    
        # Validate file type
        if not file.filename.endswith('.csv'):
            raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV file.")

        your_first_name = os.getenv('FIRST_NAME')
        your_surname = os.getenv('LAST_NAME')

        # Create instances of the parser and transformer
        parser = CSVParser()
        transformer = DataTransformer(your_first_name, your_surname)
        
        parsed_data = parser.parse(file.file)  
        
        # Transform the data
        transformed_data, job_title = transformer.transform(parsed_data)
        print(transformed_data)
        # Initialize lists to collect results
        success_candidates = []
        failed_candidates = []
        for candidate in transformed_data:
            try:
                print(candidate)
                status_code, error_info = post_talent_pool(candidate)
                if status_code == 201:
                    print(f"Candidate '{candidate['name']}' created successfully.")
                    success_candidates.append(candidate['name'])
                else:
                    print(f"Failed to create candidate '{candidate['name']}'. Status code: {status_code}. Error: {error_info}")
                    failed_candidates.append({
                        'name': candidate['name'],
                        'error': error_info
                    })
            except Exception as e:
                print(f"Exception occurred while processing candidate '{candidate['name']}': {e}")
                failed_candidates.append({
                    'name': candidate['name'],
                    'error': str(e)
                })
                
        # Prepare the response
        return {
            "message": "File processed successfully",
            "total_candidates": len(transformed_data),
            "successful_imports": success_candidates,
            "failed_imports": failed_candidates
        }