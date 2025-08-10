# Flask Comment API

A lightweight backend API built with **Flask** and **SQLAlchemy** for managing comments linked to tasks.  
It has **no frontend buttons or pages** — you interact with it by sending HTTP requests (e.g., via Postman or cURL).

---

## Features

- Add, edit, delete, and view all comments.
- Built using Flask 
Framework.
- SQLite database for storage.
- Automated testing using **PyTest**.
- Easy to test with **Postman** or command-line tools like `cURL`.

---

## Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Yaswanthpatnam/flask-comment-api.git
cd flask-comment-api

---

### 2️⃣ Create and activate a virtual environment

# Create virtual environment
python -m venv venv

# Activate it
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

### 3️⃣ Install dependencies

pip install -r requirements.txt


### 4️⃣ Run the server

python run.py


### 5️⃣ Server start location

http://127.0.0.1:5000/

--- 

### How to Use – API Routes
Use Postman or curl to test the following endpoints.

# Get all comments
GET /comments

# Add a new comment

POST /comments

{
    "task_id": 1,
    "content": "This is a new comment"
  
}

# Edit/update a comment

PUT /comments/<id>

{
    "content": "Updated comment content"
}

# Delete a comment

DELETE /comments/<id>

---

### Testing

# Install PyTest

pip install pytest

# Run tests

pytest

