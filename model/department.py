from peewee import *


class Department(Model):

    department_id = AutoField(column_name='DepartmentId')
    name = TextField(column_name='Name')

    class Meta:
        database = SqliteDatabase('company_org.sqlite')
        table_name = 'Department'
