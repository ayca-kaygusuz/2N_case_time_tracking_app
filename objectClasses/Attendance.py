# © 2024 Ayça Kaygusuz

class Attendance:
    def __init__(self, id, employee_id, clock_in, clock_out=None, is_late=False):
        self.id = id
        self.employee_id = employee_id
        self.clock_in = clock_in
        self.clock_out = clock_out
        self.is_late = is_late