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
   git clone https://github.com/yourusername/collaborative_task_manager.git
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
