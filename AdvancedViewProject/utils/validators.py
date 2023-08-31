from django.core.exceptions import ValidationError
import re

class CustomPasswordValidator():
    
    def __init__(self):
        pass

    def validate(self, password, user=None):
        if all(
            (re.search('[0-9]', password),
             re.search('[a-z]', password),
             re.search('[A-Z]', password))
             ):
            return
        raise ValidationError("Password require 0-9, a-z and A-Z")
    
    def get_help_text(self):
        return "Password require 0-9, a-z and A-Z"