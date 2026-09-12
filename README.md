# Devops-CI-CD-project

# About the Project
This project is a robust web application designed to demonstrate the seamless integration of development and operations. Built using Python (Flask), it provides a secure environment for user registration and authentication. The core of this project lies in its automated CI/CD pipeline, orchestrated by Jenkins, ensuring efficient and continuous delivery to the cloud.

# Key Features
- User Authentication: Secure registration and login functionalities using Flask-SQLAlchemy for database management and werkzeug for password hashing.
- Automated Deployment: A fully functional CI/CD pipeline built with Jenkins that automates the build and deployment process.
- Responsive Frontend: Clean and intuitive user interface designed with HTML/CSS.
- Cloud Ready: Optimized for cloud instances, providing accessible deployment on designated ports.

# Technologies Used
- Backend: Python, Flask, Flask-SQLAlchemy, Werkzeug Security
- Frontend: HTML, CSS
- CI/CD / DevOps: Jenkins, Git/GitHub, Linux
- Database: SQLite (SQLAlchemy)

# CI/CD Pipeline Workflow
- Code Commit: Any updates in the source code are pushed to the GitHub repository.
- Webhook Trigger: Pushes trigger a Jenkins webhook automatically.
- Build & Test: Jenkins pulls the latest code, runs predefined tests (using test_app.py), and prepares the environment.
- Deploy: The application is deployed dynamically to the target cloud instance, running continuously in the background.

# Getting Started
To run this project locally, follow these steps:
# Prerequisites
- Python installed on your local machine
- Jenkins configured with necessary plugins for Git and Python

# Installation
 1. Clone the repository:
 - ''' git clone https://github.com/nithish23rr-art/Devops-CI-CD-project.git '''
 2.Navigate to the project directory:
 - ''' cd Devops-CI-CD-project '''
3.Install dependencies:
- ''' ./venv/bin/pip install Flask '''
- ''' ./venv/bin/pip install -r requirements.txt '''
4.Set up the database and run the application:
 - ''' nohup python3 web_application.py > app.log 2>&1 & '''
Usage
 1. Access the application at
- ''' http://172.21.162.50:5000/register '''
     Use the Register page to create a new account.
2. Log in to your account with the created credentials
