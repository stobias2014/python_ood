#!/bin/python3

class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Employee Count: {0}".format(empCount))

    def displayEmployee(self):
        print("Employee Name: {0} \t Employee Salary: {1}".format(self.name, self.salary))


emp1 = Employee("John Doe", 4500)
emp2 = Employee("Jane Doe", 5500)

emp1.displayEmployee()
print("Employee Count = {0}".format(Employee.empCount))


