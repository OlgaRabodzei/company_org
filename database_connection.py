from peewee import SqliteDatabase

from model.department import Department
from model.employee import Employee

database = SqliteDatabase('company_org.sqlite')
database.create_tables([Employee, Department], safe=True)
