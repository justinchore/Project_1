import re
import bcrypt

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