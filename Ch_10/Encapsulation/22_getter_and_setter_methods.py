# #Getter and Setter Methods
# In Python, getter and setter methods are used to access and modify private attributes safely. 
# Instead of accessing private data directly, these methods provide controlled access, allowing you to:

# Read data using a getter method.

# Update data using a setter method with optional validation or restrictions.

# Here's an example of getter and setter methods in a class:

class Employee:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def get_salary(self):    # Getter method
        return self.__salary

    def set_salary(self, amount):   # Setter method
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount!")

emp = Employee()
print(emp.get_salary())  # Access salary using getter

emp.set_salary(60000)   # Update salary using setter
print(emp.get_salary())