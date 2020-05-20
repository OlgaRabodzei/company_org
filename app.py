import logging
import sys

from model.department import Department
from model.employee import Employee

from database_connection import *

# TODO: Update it to file logging.
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger('__main__')


def start():
    while True:
        try:
            user_input = int(input(
                '''Please chose one of the operations below:
                1 - Show departments
                2 - Add department
                3 - Select department
                10 - Exit
                You choose: '''))
            if user_input == 1:
                show_departments()
            elif user_input == 2:
                add_department()
            elif user_input == 3:
                select_department()
            elif user_input == 10:
                break
            else:
                start()
        except ValueError as exp:
            start()


def show_departments(limit=10):
    query = Department.select().limit(limit)
    departments_list = query.execute()

    print('The departments are:')
    for department in departments_list:
        print(department)

    if not len(departments_list):
        print('Departments list is empty.\n')


def add_department():
    user_input = input('What is a name of the department? ')
    if not user_input:
        return

    Department.create(name=user_input)
    # log.info(f'A new department was added: {new_department}')


def select_department():
    user_input = int(input('What is a department ID?: '))
    department = Department.get_by_id(user_input)
    if not department:
        print('Wrong department Id.')
        return

    while True:
        try:
            user_input = int(input(
                '''What operation would you like to do?
                1 - Show a list of employees
                2 - Add an employee to the list
                3 - Remove an employee from the list
                10 - Back
                You choose: '''))

            if user_input == 1:
                show_employees_from_department(department)
            elif user_input == 2:
                add_employee_to_department(department)
            elif user_input == 3:
                change_employee_department(None)
            elif user_input == 10:
                break
            else:
                select_department()
        except ValueError as exp:
            select_department()


def show_employees_from_department(department: Department):
    query = Employee.select().where(Employee.department == department.department_id)
    employees_list = query.execute()

    if not len(employees_list):
        print('The employee list is empty.')
        return

    print(f'The employee list for {department.name} department is:')
    for employee in employees_list:
        print(employee)


def add_employee_to_department(department: Department):
    first_name = input('What is an employee first name? ')
    last_name = input('What is an employee last name? ')
    position = input('What is an employee position? ')
    Employee.create(first_name=first_name, last_name=last_name, position=position, department=department)


# def change_employee_department(department: Department | None):
#     employee = Employee(department=department)
#     employee.id = int(input('What is an employee Id to update? '))
#     employee.save()


start()
