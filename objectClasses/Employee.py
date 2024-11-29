class Employee:
    def __init__(self, id, name, start_date, leave_days=15):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.leave_days = leave_days