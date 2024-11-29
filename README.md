# 2N_case_time_tracking_app

## Description

The Attendance Tracker is a simple Python application that allows you to manage employee attendance. It uses PostgreSQL as the database to store employee details and attendance records. The application adheres to the SOLID principles for clean and maintainable code.

## Features

- Add employees to the database.
- Record clock-in and clock-out times for employees.
- Check if an employee was late based on clock-in times.

## Prerequisites

- Python 3.6 or higher
- PostgreSQL 12 or higher
- psycopg2 package

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/attendance_tracker.git
   cd attendance_tracker

2. **Install dependencies:**
    ```bash
    pip install psycopg2

3. **Set up the Postgre SQL database:**
    Start your PostgreSQL server and connect. Create a new database for the application (default is attendance_db). Create the necessary employee and attendance tables. Example:

    ```sql
    CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    leave_days INT DEFAULT 15
    );

    CREATE TABLE attendance (
    id SERIAL PRIMARY KEY,
    employee_id INT REFERENCES employees(id),
    clock_in TIMESTAMP,
    clock_out TIMESTAMP,
    is_late BOOLEAN DEFAULT FALSE
    );

4. **Configure database connection:**
    You may modify the config.py file to set your PostgreSQL default database connection details, or enter when prompted.

## Usage
    Run the application:
    ```bash
    python main.py

## Testing
    Run the following command in the directory:
    ```bash
    python -m unittest discover -s tests

## License
    This project is copyrighted under GNU GPL v3. For details, please refer to the LICENSE file.

## Contact
    For questions or feedback, if you already don't have my other personal contact info, you may contact me through LinkedIn, which is linked through my github profile, and also registered with the same name.

    © 2024 Ayça Kaygusuz