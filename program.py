from hr import PayrollSystem, HourlyPolicy
from productivity import ProductivitySystem
from employees import EmployeeDatabase

payroll_system = PayrollSystem()
productivity_system = ProductivitySystem()
employee_database = EmployeeDatabase()
employees = employee_database.employees_m()

manager = employees[0]
manager.payroll = HourlyPolicy(55)

productivity_system.track(employees, 40)
payroll_system.calculate_payroll(employees)