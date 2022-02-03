from django.urls import converters

class UsernameConverter:
    '''
        This is used by application side to check whether username parsed in HTTP request is valid
        We create this class to be used in multiple places
        Including users app
    '''
    regex='[a-zA-Z0-9_-]{5,20}'

    def to_python(self,value):
        return value