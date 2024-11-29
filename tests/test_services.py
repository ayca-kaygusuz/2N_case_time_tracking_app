import unittest
from database import Database
from services import EmployeeService, AttendanceService

class TestServices(unittest.TestCase):
    def setUp(self):
        self.db = Database(dbname='attendance_db', user='your_username', password='your_password')
        self.employee_service = EmployeeService(self.db)
        self.attendance_service = AttendanceService(self.db)
        
        # Clear the employees and attendance tables for testing
        self.db.execute("DELETE FROM attendance;")
        self.db.execute("DELETE FROM employees;")

    def test_add_employee(self):
        self.employee_service.add_employee("Jane Doe", "2024-01-01")
        
        # Verify the employee was added
        result = self.db.fetchone("SELECT * FROM employees WHERE name = %s;", ('Ali Oz',))
        self.assertIsNotNone(result)  # Ensure the employee exists
        self.assertEqual(result[1], 'Ali Oz')  # Check the name is correct
        self.assertEqual(result[3], 15)  # Default leave_days should be 15

    def test_clock_in(self):
        # First, add an employee to clock in
        self.employee_service.add_employee("John Smith", "2024-01-01")
        
        # Clock in the employee
        self.attendance_service.clock_in(1)  # Assuming this is the ID of John Smith
        
        # Verify the clock-in was recorded
        result = self.db.fetchone("SELECT * FROM attendance WHERE employee_id = %s AND clock_out IS NULL;", (1,))
        self.assertIsNotNone(result)  # Ensure the clock-in record exists
        self.assertIsNotNone(result[2])  # Check that clock_in is not None

    def tearDown(self):
        self.db.execute("DELETE FROM attendance;")
        self.db.execute("DELETE FROM employees;")
        self.db.close()

if __name__ == '__main__':
    unittest.main()