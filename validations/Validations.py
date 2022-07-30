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