def check_email(string):
    if ' ' not in string and '@' in string and '@.' not in string and string.rfind('.') > string.find('@'):
        return True
    else:
        return False
