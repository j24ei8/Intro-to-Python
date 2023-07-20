# Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_emp_details.
# Sample Employee Data:
#   "ADAMS", "E7876", 50000, "ACCOUNTING"
#   "JONES", "E7499", 45000, "RESEARCH"
#   "MARTIN", "E7900", 50000, "SALES"
#   "SMITH", "E7698", 55000, "OPERATIONS"
# 1) Use 'assign_department' method to change the department of an employee.
# 2) Use 'print_employee_details' method to print the details of an employee.
# 3) Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following formula:
#   overtime = hours_worked - 50
#   Overtime amount = (overtime * (salary / 50))


class Employee:

  def __init__(self, emp_name, emp_id, emp_salary, emp_department):
    self.emp_id = emp_id
    self.emp_name = emp_name
    self.emp_salary = emp_salary
    self.emp_department = emp_department

  def assign_department(self, new_department):
    self.emp_department = new_department

  def print_employee_details(self):
    print("Emplyee Detail for", self.emp_name)
    print("Employee ID:", self.emp_id)
    print("Employee Salary:", self.emp_salary)
    print("Employee Department:", self.emp_department)
    print()

  def calculate_emp_salary(self, salary, hours_worked):
    if hours_worked > 50:
      overtime_amount = (hours_worked - 50) * (salary / 50)
      self.emp_salary = salary + overtime_amount


# "ADAMS", "E7876", 50000, "ACCOUNTING"
# "JONES", "E7499", 45000, "RESEARCH"
# "MARTIN", "E7900", 50000, "SALES"
# "SMITH", "E7698", 55000, "OPERATIONS"
# "SHIN", "E7777", 10000, "TECH"

shin = Employee("SHIN", "E7777", 10000, "TECH")
shin.print_employee_details()
shin.assign_department("ACCOUNTING")
shin.print_employee_details()
shin.calculate_emp_salary(10000, 55)
shin.print_employee_details()
