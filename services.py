from datetime import datetime
from database import Database
from objectClasses.Employee import Employee
from objectClasses.Attendance import Attendance

class EmployeeService:
    def __init__(self, database: Database):
        self.database = database

    def add_employee(self, name, start_date):
        query = "INSERT INTO employees (name, start_date) VALUES (%s, %s)"
        self.database.execute(query, (name, start_date))

class AttendanceService:
    def __init__(self, database: Database):
        self.database = database

    def clock_in(self, employee_id):
        query = "INSERT INTO attendance (employee_id, clock_in) VALUES (%s, %s)"
        self.database.execute(query, (employee_id, datetime.now()))

    def clock_out(self, employee_id):
        query = """
        UPDATE attendance 
        SET clock_out = %s 
        WHERE employee_id = %s AND clock_out IS NULL
        """
        self.database.execute(query, (datetime.now(), employee_id))

    def check_late(self, employee_id):
        query = """
        SELECT clock_in FROM attendance 
        WHERE employee_id = %s ORDER BY clock_in DESC LIMIT 1
        """
        last_clock_in = self.database.fetchone(query, (employee_id,))
        if last_clock_in and last_clock_in[0].time() > datetime.strptime("08:00", "%H:%M").time():
            update_query = """
            UPDATE attendance 
            SET is_late = TRUE 
            WHERE employee_id = %s AND clock_in = %s
            """
            self.database.execute(update_query, (employee_id, last_clock_in[0]))