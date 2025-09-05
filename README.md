# Flask Comment API

A lightweight RESTful API for managing comments, built with Flask and SQLAlchemy. Interact with it using tools like Postman, Thunder Client, or Insomnia.

## Features
✅ Create, read, update, and delete comments

✅ Filter comments by task ID

✅ SQLite database with SQLAlchemy ORM

✅ Comprehensive testing with pytest


##  Installation & Setup

## Clone the repo and navigate to it

git clone <https://github.com/Yaswanthpatnam/flask-comment-api>
cd flask-comment-api

## Create and activate a virtual environment
python -m venv venv
#### On Windows:
venv\Scripts\activate
#### On macOS/Linux:
source venv/bin/activate

##  Install dependencies
pip install -r requirements.txt

### Run the server
python run.py
Server URL: http://localhost:5000

## Test with Postman/Thunder Client
Once the server is running, open your API client and try these requests:

#### Action	Method	URL	Body (Raw JSON)  
##### Create Comment "POST"	 - http://localhost:5000/api/comments	

    {
     "task_id": 1, "content": "My first comment" 
    }
##### Get All Comments "GET" - http://localhost:5000/api/comments

##### Get One Comment "GET" - http://localhost:5000/api/comments/1

##### Update Comment "PUT" - http://localhost:5000/api/comments/1	

    { 
        "content": "Updated text" 
    }

##### Delete Comment "DELETE" - http://localhost:5000/api/comments/1

### API Endpoint Reference
All endpoints are prefixed with: http://localhost:5000/api

Endpoint	Method	Description
- /health	GET	Check if the API is running.
- /comments	POST	Create a new comment. Requires task_id and content.
- /comments	GET	Get a list of all comments.
- /comments?task_id=1	GET	Filter: Get comments for a specific task.
- /comments/id	GET	Get a single comment by its ID.
- /comments/id	PUT	Update a comment's content.
- /comments/id	DELETE	Delete a comment by its ID.

## Running Tests

To ensure everything works, run the test suite:

### Install pytest if you haven't
pip install pytest

### Run the tests
pytest -v