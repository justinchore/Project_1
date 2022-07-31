import emoji
##############Account Creation#######################

class InvalidCharactersError(Exception):
    def __init__(self, list):
        def generate_message():
            return f"Invalid characters detected: {list}. Please try again or enter '/q' to exit: " 
        self.message = generate_message()
        
class InvalidNumbersError(Exception):
     def __init__(self, list):
        def generate_message(): 
            return f"Numbers detected: {list}. Please try again or enter '/q' to exit: "
        self.message = generate_message()   

class InvalidEmailFormatError(Exception):
    def __init__(self):
        self.message = "Invalid email. Please try again or enter '/q' to exit: "
    pass

class DuplicateEmailError(Exception):
    def __init__(self):
        self.message = "There is already an account registered to this email. Please log in."
    pass

class InvalidPasswordError(Exception):
    def __init__(self):
        self.message = "Password requirements not met. Please try again or enter '/q' to exit. "
        
class InvalidStreetFormat(Exception):
    def __init__(self):
        self.message = "Street address is not in a valid format. Please try again or enter '/q' to exit. "

class InvalidStateName(Exception):
    def __init__(self):
        self.message = "State name is invalid. Only US zipcodes accepted. Please try again or enter '/q' to exit."
        
class InvalidZipCode(Exception):
    def __init__(self):
        self.message = "Zipcode format is invalid. Please try again or enter '/q' to exit. "
        
##############Authentication#########################

class EmailNotRegistered(Exception):
    def __init__(self):
        self.message = "Email is not registered. Please try again or enter '/q' to exit."

class AuthenticationFailedError(Exception):
    def __init__(self):
        self.message = "Authentication failed. Please try again or enter '/q' to exit."