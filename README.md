# Application Overview

This application is developed using Python and leverages the FastAPI framework to create high-performance API endpoints. It is designed to facilitate the import and processing of candidate data from CSV files, integrating seamlessly with the Workable API to add candidates either to specific job postings or to the talent pool.

## How to Install and Run the Project

### Clone the Repository:

```
git clone https://github.com/neokol/import-candidates.git
cd import-candidates
```

### Install Poetry (if not already installed):

On Unix/Linux/macOS:

```
curl -sSL https://install.python-poetry.org | python3 -
```

On Windows (PowerShell):

```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Ensure that Poetry's bin directory is in your PATH.

### Install Dependencies:

```
poetry install
```

Run the application using Uvicorn throught Poetry:

```
poetry run uvicorn main:app --reload
```

## Uploading Candidates to Specific Jobs

Open your browser and navigate to http://127.0.0.1:8000/docs.

### Locate the /upload_candidates Endpoint.

Upload Your CSV File:

1. Click "POST /upload_candidates" to expand the endpoint.
2. Click "Try it out".
3. Use the "Choose File" button to select your CSV file.
4. Click "Execute" to upload and process the file.

### Uploading Candidates to the Talent Pool

Open your browser and navigate to http://127.0.0.1:8000/docs.

Locate the /upload_talent_pool Endpoint.

Upload Your CSV File:

1. Click "POST /upload_candidates" to expand the endpoint.
2. Click "Try it out".
3. Use the "Choose File" button to select your CSV file.
4. Click "Execute" to upload and process the file.
