import logging
import sys
from peewee import *

from model.department import Department
from model.employee import Employee

# TODO: Update it to file logging.
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger('__main__')


def start():
    init_empty_db()
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


def init_empty_db():
    database = SqliteDatabase('company_org.sqlite')
    if not len(database.get_tables()):
        database.init('company_org.sqlite')
        database.create_tables([Employee, Department])


def show_departments(limit=10):
    query = Department.select().limit(limit)
    departments_list = query.dicts().execute()

    print('The departments are:')
    for department in departments_list:
        print(f'{department.get("name")} ({department.get("department_id")})')

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

    # TODO Add department menu.
    # 1 - employee list
    # 2 - add employee
    # 4 - remove employee from department

    query = Employee.select().where(Employee.department == department.department_id)
    employees_list = query.dicts().execute()

    if not len(employees_list):
        print('The employee list is empty.\n')
        return

    print(f'The employee list for {department.name} department is:')
    for employee in employees_list:
        print(f'{employee.get("first_name")} {employee.get("last_name")} {employee.get("position")}')


start()
