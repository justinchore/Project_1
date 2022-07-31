import re

class Validations(object):
    @staticmethod
    def special_chars_validation(input):
        pattern = re.compile(r"[@_!#$%^&*()<>?/\|}{~:]")
        return pattern.findall(input)
    
    @staticmethod
    def no_numbers_validation(input):
        match = re.findall('[0-9]+', input)
        return match
    
    @staticmethod
    def email_format_validation(input):
        pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        match = re.fullmatch(pattern, input)
        return match 
    
    @staticmethod
    def pw_format_validation(input):
        pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
        match = re.search(pattern, input)
        return match 
    
    @staticmethod
    def street_address_validation(input):
        pattern = "^(\d+) ?([A-Za-z](?= ))? (.*?) ([^ ]+?) ?((?<= )APT)? ?((?<= )\d*)?$"
        match = re.search(pattern, input)
        return match