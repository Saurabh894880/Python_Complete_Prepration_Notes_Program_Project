# - User-defined exceptions are created by defining a new class that inherits from Python's built-in Exception class or one of its subclasses.
# - By doing this, we can create custom error messages and handle specific errors in a way that makes sense for our application.

# Steps to Create and Use User-Defined Exceptions :

# - Define a New Exception Class: Create a new class that inherits from Exception or any of its subclasses.
# - Raise the Exception: Use the raise statement to raise the user-defined exception when a specific condition occurs.
# - Handle the Exception: Use try-except blocks to handle the user-defined exception.

# Step 1: Define a custom exception class
class InvalidAgeError(Exception):
    def __init__(self, age, msg="Age must be between 0 and 120"):
        self.age = age
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.age} -> {self.msg}'

# Step 2: Use the custom exception in your code
def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    else:
        print(f"Age set to: {age}")

# Step 3: Handling the custom exception
try:
    set_age(150)  # This will raise the custom exception
except InvalidAgeError as e:
    print(e)


# Example 2 :
class InvalidAgeError(Exception):
    def __init__(self, age, msg="Age must be between 0 and 120", error_code=1001):
        self.age = age
        self.msg = msg
        self.error_code = error_code
        super().__init__(self.msg)

    def __str__(self):
        return f"[Error Code {self.error_code}] {self.age} -> {self.msg}"
        
try:
    set_age(150)  # This will raise the custom exception
except InvalidAgeError as e:
    print(e)


# 3. Real World Example :

class InvalidEmailError(Exception):
    def __init__(self, email, msg="Invalid email format"):
        self.email = email
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f"{self.email} -> {self.msg}"

def set_email(email):
    if "@" not in email:
        raise InvalidEmailError(email)
    print(f"Email set to: {email}")

try:
    set_email("userexample.com")
except InvalidEmailError as e:
    print(e)