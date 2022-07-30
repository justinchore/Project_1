class InvalidCharactersError(Exception):
    def __init__(self, list):
        def generate_message():
            return f"Invalid characters detected: {list}. Please try again or enter '/q' to exit: " 
        self.message = generate_message()
        
class InvalidNumbersError(Exception):
     def __init__(self, list):
        def generate_message(): 
            return f"Numbers detected: {list}. Please try again or enter '/q' to exit"
        self.message = generate_message()   
        