from peewee import *
from model.department import Department


class Employee(Model):

    artist_id = AutoField(column_name='EmployeeId')
    first_name = TextField(column_name='FirstName')
    last_name = TextField(column_name='LastName')
    position = TextField(column_name='Position', null=True)
    department = ForeignKeyField(Department, related_name='department')

    class Meta:
        database = SqliteDatabase('company_org.sqlite')
        table_name = 'Employee'
