class Person:
    def _init_(self, name):
        self.name = name


class Employee:
    def _init_(self, emp_id):
        self.emp_id = emp_id


class Manager(Person, Employee):
    def _init_(self, name, emp_id, department):
        Person._init_(self, name)
        Employee._init_(self, emp_id)
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Department:", self.department)


# Example
m = Manager("Sanchit", 101, "IT")
m.display()
