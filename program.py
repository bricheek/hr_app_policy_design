
import json
from hr import calculate_payroll
from productivity import track
from employees import employee_database, Employee

# from policy interface pattern
# payroll_system = PayrollSystem()
# productivity_system = ProductivitySystem()
# employee_database = EmployeeDatabase()
# employees = employee_database.employees_m()

# manager = employees[0]
# manager.payroll = HourlyPolicy(55)

# productivity_system.track(employees, 40)
# payroll_system.calculate_payroll(employees)

def print_dict(d):
    print(json.dumps(d, indent=2))

employees = employee_database.employees()

track(employees, 40)
calculate_payroll(employees)

temp_secretary = Employee(5)
print('Temporary Secretary: ')
print_dict(temp_secretary.to_dict())