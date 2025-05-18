# Collaborative Task Manager

A Django-based web application for real-time task management and collaboration.

## Features

* User authentication
* Task creation, assignment, and management
* Real-time updates
* Breadcrumb navigation
* User collaboration
* Persistent data storage

## Prerequisites

* Python 3.10+
* Django 4.x
* SQLite


## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/vivekpprakash001/collaborative_task_manager
   cd collaborative_task_manager
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the application:**

   Open [http://localhost:8000](http://localhost:8000) in your browser.

## Running Broadcast Server

1. ** Execute the Broadcast server to run the websockets**
    
    ```bash
   python broadcast_server.py
   ```

## Flow of the Porject

1. **Admin Privileges**
    
    *Admin can be created using the step 5 in the Installation
    *Creation of task
    *Assign users to the task
    *User Add/Edit/Delete Operations
    
2. **User Privileges**
    
    *Listing of the tasks available for the user
    *User can view the task
    *User can add the real time update to the task which can be displayed to other user who are assigned to the same task
    
# Sample Users

1. **Admin**
    username --> admin
    password --> q1w2e3r4
   
2. **User1**
    username --> user1
    password --> u1@q1w2e3r4

3. **User2**
    username --> user2
    password --> u2@q1w2e3r4

