# Jeopardy LLM Task

This is a FastAPI-based application that uses OpenAI's API to simulate a Jeopardy game. The application interacts with a PostgreSQL database to fetch questions and uses AI to generate answers.

---

## Features

- Fetch random Jeopardy questions from the database.
- Use OpenAI's API to generate AI answers.
- Verify the correctness of AI-generated answers.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.9 or higher
- PostgreSQL (running on port `5432`)
- Docker (optional, for containerized deployment)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Leny73/jeopardy-llm-task.git
cd jeopardy-llm-task
```

### 2. Set Up a Virtual Environment

python -m venv .venv
.\.venv\Scripts\activate # On Windows

### 3. Install dependencies

pip install -r requirements.txt

### 4. Setup Database

Ensure PostgreSQL is running on localhost:5432.

Create a database named jeopardy-llm

Update the DATABASE_URL in database.py if necessary:
DATABASE_URL = "postgresql://<username>:<password>@localhost:5432/jeopardy-llm"

Run the database migrations (if applicable):
python app/database.py

### 5. Running the Application

1. Run Locally
   Start the FastAPI application:

Access the application at:

API Docs: http://127.0.0.1:8000/docs
Root Endpoint: http://127.0.0.1:8000

2. Run with Docker
   Build the Docker image:

docker build -t jeopardy-app .

Run the Docker container:

docker run -d -p 8000:8000 jeopardy-app

Access the application at:

API Docs: http://127.0.0.1:8000/docs

### Environment Variables

For security, sensitive information like API keys should be stored in environment variables. Create a .env file in the root directory with the following content:

Load the environment variables in your application using python-dotenv:

### Testing

Run the tests using pytest:

### Troubleshooting

Database Connection Issues
Ensure PostgreSQL is running on localhost:5432.
Verify the DATABASE_URL in database.py or .env.
OpenAI API Key
Ensure the OPENAI_API_KEY is set in your environment variables.
Docker Issues
If the app cannot connect to the database, update the DATABASE_URL to use the host machine's IP address instead of localhost.
