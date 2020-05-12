import logging
import sys

from model.department import Department

# TODO: Update it to file logging.
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger('__main__')

departments_list = []


def start():
    while True:
        try:
            user_input = int(input('1 - Show departments\n2 - Add department\n3 - Exit\nPlease chose one of the '
                                   'operations above: '))
            if user_input == 1:
                show_departments()
            elif user_input == 2:
                add_department()
            elif user_input == 3:
                break
            else:
                start()
        except ValueError as exp:
            start()


def show_departments(limit=10):
    print('The departments are:')
    for department in departments_list:
        print(department)

    if not len(departments_list):
        print('Departments list is empty.\n')


def add_department():
    user_input = input('What is a name of the department? ')
    if not user_input:
        return

    new_department = Department(user_input)
    departments_list.append(new_department)
    log.info(f'A new department was added: {new_department}')


def select_department(name):
    pass


start()
