import unittest
from database import Database
from services import EmployeeService, AttendanceService

class TestServices(unittest.TestCase):
    def setUp(self):
        self.db = Database(dbname='attendance_db', user='your_username', password='your_password')
        self.employee_service = EmployeeService(self.db)
        self.attendance_service = AttendanceService(self.db)

    def test_add_employee(self):
        self.employee_service.add_employee("Jane Doe", "2024-01-01")
        # Further assertions can be made here to verify the changes

    def test_clock_in(self):
        self.attendance_service.clock_in(1)
        # Further assertions can be made here to verify clock-ins

    def tearDown(self):
        self.db.close()

if __name__ == '__main__':
    unittest.main()