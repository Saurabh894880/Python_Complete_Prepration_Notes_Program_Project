# Private members :
# Private Members are variables or methods
#  that cannot be accessed directly from outside the class.
#  They are used to restrict access and protect internal data.

# In Python, private members are defined
#  with a double underscore prefix (e.g., self.__salary). 
# Python applies name mangling by internally renaming them (e.g., __salary becomes _ClassName__salary) 
# to prevent direct access.

class Employee:
    def __init__(self, name, salary):
        self.name = name          # public
        self.__salary = salary    # private

    def show_salary(self):
        print("Salary:", self.__salary)

emp = Employee("Robert", 60000)
print(emp.name)          # Public accessible
emp.show_salary()        # Accessing private correctly
# print(emp.__salary)    # Error: Not accessible directly