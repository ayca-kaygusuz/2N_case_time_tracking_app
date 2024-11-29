class Employee:
    def __init__(self, id, name, start_date, leave_days=15):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.leave_days = leave_days

class Attendance:
    def __init__(self, id, employee_id, clock_in, clock_out=None, is_late=False):
        self.id = id
        self.employee_id = employee_id
        self.clock_in = clock_in
        self.clock_out = clock_out
        self.is_late = is_late