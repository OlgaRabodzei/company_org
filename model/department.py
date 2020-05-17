from peewee import *


class Department(Model):

    id = AutoField(column_name='DepartmentId')
    name = TextField(column_name='Name')

    def __str__(self):
        return f'{self.name} ({self.id})'

    class Meta:
        database = SqliteDatabase('company_org.sqlite')
        table_name = 'Department'
