import config
config.POSTGRESQL_PATH_FINDER()

import psycopg2
from datetime import datetime

def connect_db():
    conn = psycopg2.connect(
        dbname='attendance_db',
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432'
    )
    return conn

def add_employee(name, start_date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, start_date) VALUES (%s, %s)", (name, start_date))
    conn.commit()
    cursor.close()
    conn.close()
    
def clock_in(employee_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attendance (employee_id, clock_in) VALUES (%s, %s)", (employee_id, datetime.now()))
    conn.commit()
    cursor.close()
    conn.close()

def clock_out(employee_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE attendance SET clock_out = %s WHERE employee_id = %s AND clock_out IS NULL", (datetime.now(), employee_id))
    conn.commit()
    cursor.close()
    conn.close()
    
def check_late(employee_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT clock_in FROM attendance WHERE employee_id = %s ORDER BY clock_in DESC LIMIT 1", (employee_id,))
    last_clock_in = cursor.fetchone()
    if last_clock_in:
        if last_clock_in[0].time() > datetime.strptime("08:00", "%H:%M").time():
            cursor.execute("UPDATE attendance SET is_late = TRUE WHERE employee_id = %s AND clock_in = %s", (employee_id, last_clock_in[0]))
            conn.commit()
    cursor.close()
    conn.close()
    
#test
if __name__ == "__main__":
    # Example usage
    add_employee("John Doe", "2024-01-01")
    clock_in(1)  # Clock in for employee with ID 1
    clock_out(1)  # Clock out for employee with ID 1
    check_late(1)  # Check if employee 1 was late