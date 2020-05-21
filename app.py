import logging
import sys
from peewee import DoesNotExist
from model.department import Department
from model.employee import Employee

from database_connection import *

logging.basicConfig(filename='app.log',
                    filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
log = logging.getLogger('__main__')


def start():
    while True:
        try:
            user_input = int(input(
                '''Please chose one of the operations below:
                1 - Department menu
                2 - Employee menu
                10 - Exit
                You choose: '''))
            if user_input == 1:
                department_menu()
            elif user_input == 2:
                employee_menu()
            elif user_input == 10:
                break
            else:
                start()
        except ValueError as exp:
            start()


def department_menu():
    while True:
        try:
            user_input = int(input(
                '''Please chose one of the operations below:
                1 - Show departments
                2 - Add department
                3 - Show a list of employees
                4 - Edit department name
                5 - Edit department employees list
                10 - Back
                You choose: '''))
            if user_input == 1:
                show_departments()
            elif user_input == 2:
                add_department()
            elif user_input == 3:
                show_employees_from_department(select_department())
            elif user_input == 4:
                edit_department_name(select_department())
            elif user_input == 5:
                edit_department_employees_list(select_department())
            elif user_input == 10:
                break
            else:
                department_menu()
        except ValueError as exp:
            department_menu()


def employee_menu():
    while True:
        try:
            user_input = int(input(
                '''Please chose one of the operations below:
                1 - Show all employees
                2 - Add employee
                3 - Edit employee
                4 - Delete employee
                10 - Back
                You choose: '''))
            if user_input == 1:
                show_employees()
            elif user_input == 2:
                add_employee(department=None)
            elif user_input == 3:
                edit_employee(select_employee())
            elif user_input == 4:
                employee = select_employee()
                log.info(f'An employee {employee.id} is deleted.')
                employee.delete_instance()
            elif user_input == 10:
                break
            else:
                employee_menu()
        except ValueError as exp:
            employee_menu()


def show_departments(offset=0, limit=10):
    query = Department.select().offset(offset).limit(limit)
    departments_list = query.execute()

    print('The departments are:')
    for department in departments_list:
        print(department)

    if not len(departments_list):
        print('Departments list is empty.')


def show_employees(offset=0, limit=10):
    query = Employee.select().offset(offset).limit(limit)
    employees_list = query.execute()

    print('The employees are:')
    for employee in employees_list:
        print(employee)

    if not len(employees_list):
        print('There is no employees.')


def add_department():
    user_input = input('What is a name of the department? ')
    if not user_input:
        return

    new_department = Department.create(name=user_input)
    log.info(f'A new department was added: {new_department}')


def select_department():
    try:
        user_input = int(input('What is a department ID?: '))
        return Department.get_by_id(user_input)
    except DoesNotExist:
        select_department()


def show_employees_from_department(department: Department):
    query = Employee.select().where(Employee.department == department.id)
    employees_list = query.execute()

    if not len(employees_list):
        print('The employee list is empty.')
        return

    print(f'The employee list for {department.name} department is:')
    for employee in employees_list:
        print(employee)


def edit_department_name(department: Department):
    name = str(input('What is a new department name? '))
    department.name = name
    department.save()
    log.info(f'A department name was updated: {department}')


def edit_department_employees_list(department: Department):
    while True:
        try:
            user_input = int(input(
                '''Please chose one of the operations below:
                1 - Add employee to the department
                2 - Remove employee from the department
                10 - Back
                You choose: '''))
            if user_input == 1:
                add_employee(department)
            elif user_input == 2:
                employee = Employee(department=None)
                employee.id = int(input('What is an employee ID to remove from the department? '))
                employee.save()
            elif user_input == 10:
                break
            else:
                edit_department_employees_list()
        except ValueError as exp:
            edit_department_employees_list()


def add_employee(department: [Department, None]):
    first_name = str(input('What is an employee first name? '))
    last_name = str(input('What is an employee last name? '))
    position = str(input('What is an employee position? '))
    while not department:
        user_input = int(input('What is a department ID? '))
        department = Department.get_by_id(user_input)
    employee = Employee.create(first_name=first_name, last_name=last_name, position=position, department=department)
    log.info(f'An employee was created {employee}')


def select_employee():
    try:
        user_input = int(input('What is a employee ID?: '))
        return Employee.get_by_id(user_input)
    except DoesNotExist:
        select_employee()


def edit_employee(employee: Employee):
    first_name = str(input(f'What is an employee first name?({employee.first_name}) '))
    if first_name:
        employee.first_name = first_name

    last_name = str(input(f'What is an employee last name?({employee.last_name}) '))
    if last_name:
        employee.last_name = last_name

    position = str(input(f'What is an employee position?({employee.position}) '))
    if position:
        employee.position = position

    try:
        department = int(input(f'What is an employee department id?({employee.department_id}) '))
        department = Department.get_by_id(department)
    except DoesNotExist:
        department = None
    except ValueError:
        department = None

    if department:
        employee.department = department

    employee.save()
    log.info(f'An employee was updated {employee}')


start()
