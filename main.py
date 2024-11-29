from database import Database
from services import EmployeeService, AttendanceService

def main():
    # Using defaults from config.py
    db = Database()
    # Alternatively, you can specify custom values with db, user, and password

    employee_service = EmployeeService(db)
    attendance_service = AttendanceService(db)

    # Example usage
    # employee_service.add_employee("Ali Oz", "2024-01-01")
    # attendance_service.clock_in(1)  # Clock in for employee with ID 1
    # attendance_service.clock_out(1)  # Clock out for employee with ID 1
    # attendance_service.check_late(1)  # Check if employee 1 was late

    db.close()

if __name__ == "__main__":
    main()