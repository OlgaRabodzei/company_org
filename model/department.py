class Department:

    def __init__(self, name, employees=None):
        self._name = str(name)
        self._employees = employees
        if employees is None:
            self._employees = []

    def __repr__(self):
        return '<Department: %s ("%s")>' % (self.__class__.__name__, self._name)

    def __str__(self):
        return f'{self._name} ({len(self._employees)})'

    def add_employee(self):
        pass

    def delete_employee(self, employee_id):
        pass

    def list_employee(self):
        pass
