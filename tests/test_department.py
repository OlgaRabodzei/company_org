import unittest
from database_connection import *


class DepartmentTest(unittest.TestCase):

    def setUp(self) -> None:
        database.create_tables([Employee, Department], safe=True)
        department = Department.create(name='TestDepartment')
        self._department_id = department.id

    def tearDown(self) -> None:
        department = Department.get(Department.id == self._department_id)
        department.delete_instance()

    def test_department_table_exists(self):
        self.assertTrue(Department.table_exists())

    def test_name(self):
        department = Department.get(Department.id == self._department_id)
        self.assertEqual(department.name, 'TestDepartment')

    def test_department_employee(self):
        department = Department.get(Department.id == self._department_id)
        # Test adding employee.
        employee = Employee.create(first_name='John', last_name='Smith', department=department)
        employees_from_dep = Employee.select().where(Employee.department == department).execute()
        self.assertTrue(employees_from_dep)

        # Test removing employee.
        employee.department = None
        employee.save()
        employees_from_dep = Employee.select().where(Employee.department == department).execute()
        self.assertFalse(employees_from_dep)

        # Clean up test.
        employee.delete_instance()


if __name__ == '__main__':
    unittest.main()
