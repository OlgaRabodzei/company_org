from peewee import *
from model.department import Department


class Employee(Model):

    id = AutoField(column_name='EmployeeId')
    first_name = TextField(column_name='FirstName')
    last_name = TextField(column_name='LastName')
    position = TextField(column_name='Position', null=True)
    department = ForeignKeyField(Department, related_name='department')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.position} ({self.id})'

    class Meta:
        database = SqliteDatabase('company_org.sqlite')
        table_name = 'Employee'
