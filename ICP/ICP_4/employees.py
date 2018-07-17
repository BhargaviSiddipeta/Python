class Employee:
    # to count number of employees
    employee_count = 0
    #Creating a constructor and assiging varible names to parameters
    def __init__(self,name,family,salary,department):
        # set the values
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

        #Employee.employee_count +=1

    #creating avg_salary method to return fixed salary of an employee
    def fixed_salary(self):
        return self.salary

# child class for the employee class
class Full_time_employee(Employee):
    # Creating a constructor and assiging varible names to parameters
    def __init__(self, name, family, salary, department, extra_salary ):
       super().__init__(name,family,salary,department)
       self.extra_salary = extra_salary
        # increment employee counter
       Employee.employee_count += 1

    # creating full_time_employee_avg_sal method to return the salary of an full-time employee
    def full_time_employee_avg_sal(self):
        avg_sal = Employee.fixed_salary(self) + self.extra_salary
        return avg_sal

#creatng object for Full_time employee class and passing values into it
emp1 = Full_time_employee("bhargavi", 4, 98752, "Tecnical", 1)
emp2 = Full_time_employee("sandeep", 2, 56987, "Tecni", 7)
# Print details of employee with his average salary
print(f"The employee {emp1.name} who belongs to the {emp1.department} department")
print("His Average salary  is: " ,emp1.full_time_employee_avg_sal())
print(f"The employee {emp2.name} who belongs to the {emp2.department} department")
print("His Average salary is: ", emp2.full_time_employee_avg_sal())
# print the total number of employees in organization
print("Total number of employees in an organization: ", Employee.employee_count)

