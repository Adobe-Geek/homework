from datetime import date


class Department:
    def __init__(self, name, abbreviation, manager):
        self.name = name
        self.abbreviation = abbreviation
        self.manager = manager
        self.size = []

    def add_employee(self, employee):
        if len(self.size) < 20:
            self.size.append(employee)
        else:
            return "Dapartment is fully staffed"

    def employees_on_vac(self):
        return len([employee for employee in self.size if employee.is_on_vacation()])

    def add_employee_vacation(self, employee, start_day, end_day):
        if self.employees_on_vac() < 5:
            employee.add_vacation(start_day, end_day)
            return f"Vacation added for {employee.last_name}"
        else:
            return f"Too many employees are already on vacation"


class Employee:
    def __init__(
        self,
        num,
        last_name,
        first_name,
        passport,
        dob,
        pob,
        address,
        position,
        salary,
        start_date,
    ):
        self.num = num
        self.last_name = last_name
        self.first_name = first_name
        self.passport = passport
        self.dob = dob
        self.pob = pob
        self.address = address
        self.position = position
        self.salary = salary
        self.start_date = start_date
        self.position_history = [self.position]
        self.vacation = []
        self.pto = 0

    def get_salary(self):
        service_length = date.today().year - self.start_date.year
        return self.salary * (1.012**service_length)

    def change_position(self, new_position):
        self.position_history.append(new_position)
        self.position = new_position

    def add_vacation(self, start_day, end_day):
        self.vacation.append((start_day, end_day))
        vac_days = (end_day - start_day).days
        self.pto += vac_days

    def is_on_vacation(self):
        for start_day, end_day in self.vacation:
            if start_day <= date.today() <= end_day:
                return True
        return False

    def on_vacation(self):
        if self.is_on_vacation():
            return f"{self.last_name} is off today"
        else:
            return f"{self.last_name} is working today"


department = Department("Finance", "Fin", "Harry Proper")
emp1 = Employee(
    1,
    "Bond",
    "James",
    "12345",
    date(1980, 5, 5),
    "Rivne",
    "Piotrkowska 45",
    "Engineer",
    1200,
    date(2015, 10, 21),
)
print(department.add_employee(emp1))
print(department.add_employee_vacation(emp1, date(2024, 7, 1), date(2014, 7, 1)))
print(emp1.on_vacation())
