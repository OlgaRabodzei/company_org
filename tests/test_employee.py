import unittest
from database_connection import *


class EmployeeTest(unittest.TestCase):

    def setUp(self) -> None:
        database.create_tables([Employee, Department], safe=True)
        employee = Employee.create(first_name='John', last_name='Smith')
        self._employee_id = employee.id

    def tearDown(self) -> None:
        employee = Employee.get(Employee.id == self._employee_id)
        employee.delete_instance()

    def test_employee_table_exists(self):
        self.assertTrue(Employee.table_exists())

    def test_first_name(self):
        employee = Employee.get(Employee.id == self._employee_id)
        self.assertEqual(employee.first_name, 'John')

    def test_edit_employee(self):
        employee = Employee.get(Employee.id == self._employee_id)
        department = Department.create(name='TestDepartment')
        employee.department = department
        employee.save()
        # Test adding department.
        employee = Employee.get(Employee.id == self._employee_id)
        self.assertEqual(employee.department, department)
        # Test removing department.
        department.delete_instance(recursive=True)
        employee = Employee.get(Employee.id == self._employee_id)
        self.assertFalse(employee.department)

