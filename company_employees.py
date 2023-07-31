class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary
    
    def __str__(self):
        return f'Name: {self.name}, Employee ID: {self.emp_id}'
        
class Company:
    def __init__(self):
        self.employees = []
        
    def hire_employee(self, employee):
        self.employees.append(employee)
            
    def fire_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                break
    
    def get_employee(self,emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                return employee
        return None
            
    
# Create a few employees
employee1 = Employee("John Smith", 101, "Marketing", 50000)
employee2 = Employee("Jane Doe", 102, "Finance", 60000)

# Create the company
my_company = Company()

# Hire employees
my_company.hire_employee(employee1)
my_company.hire_employee(employee2)

# Print the list of employees
for employee in my_company.employees:
    print(employee)

# Fire an employee with ID 101
my_company.fire_employee(101)

# Get an employee by their ID
employee_info = my_company.get_employee(102)
if employee_info:
    print("Found employee:", employee_info)
else:
    print("Employee not found.")