# You can test your doctests with python -m doctest p9_1.py -v
import re

def validate_social_security_number(social_security: str) -> bool: 
    """Validate social security number, e.g., 123-45-6789 (no spaces)
    Args:
        social_security: social security number to validate
    Returns:
        True if social security is valid, False otherwise
    >>> validate_social_security_number('123-45-6789')
    True

    >>> validate_social_security_number('765-23-9873')
    True

    >>> validate_social_security_number('12d-df-34hj')
    False
    """
    matches = []
    match_check = re.match('(\d{3})-(\d{2})-(\d{4})', social_security, flags=0)
    if match_check == None:
        check = False
    else:
        matches.append(social_security)
        check = True
    return check
    

def validate_zip(zip: str) -> bool: 
    """Validate zip code (5 digits), e.g, '12345' is valid, '1 23 45' is not.
    Args:
        zip: zip code to validate
    Returns:
        True if zip is valid, False otherwise
    >>> validate_zip('63040')
    True

    >>> validate_zip('97403')
    True

    >>> validate_zip('234580')
    False
    """
    matches = []
    match_check = re.match('\d{5}$', zip)
    if match_check == None:
        check = False
    else:
        matches.append(zip)
        check = True
    return check
    
def validate_zip_plus(zip_plus: str) -> bool:
    """Validate zip plus code, five digits followed by a dash and four more digits, 
        e.g., 41243-1234 (no spaces).
    Args:
        zip_plus: zip plus code to validate
    Returns:
        True if zip plus is valid, False otherwise
    >>> validate_zip_plus('12345-3647')
    True
    >>> validate_zip_plus('321-67 9')
    False
    >>> validate_zip_plus('54 g-234 5')
    False
    """
    matches = []
    match_check = re.match('(\d{5})-(\d{4})$', zip_plus)
    if match_check == None:
        check = False
    else:
        matches.append(zip_plus)
        check = True
    return check

def validate_phone(phone: str) -> bool:
    """Validate phone number, e.g., 123-456-7890 or (123)456-7890 or 123.456.7890
    Args:
        phone: phone number to validate
    Returns:
        True if phone is valid, False otherwise

    Examples:
        The following are examples of valid phone numbers:
            (123) 456-7890
            (123)456-7890
            123-456-7890
            123.456.7890
        The following are examples of invalid phone numbers:
            (123)4567890
            456-7890
            123 456-7890
    >>> validate_phone('636-293-5743')
    True
    >>> validate_phone('(123)4567890')
    False
    >>> validate_phone('314.673.2983')
    True
    """
    matches = []
    match_check = re.match('\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}', phone)
    if match_check == None:
        check = False
    else: 
        matches.append(phone)
        check = True
    return check


def validate_email(email: str) -> bool:
    """Validate email address, e.g., myname212@thing1.thing2.com (case-insensitive).
    Args:
        email: email address to validate
    Returns:
        True if email is valid, False otherwise
    Examples:
        The following are examples of valid email addresses:
            bnorris2@uoregon.edu
            norris@cs.uoregon.edu
            yippee_skippy@yee-haw.wheeeee
            fun-times@Deschutes.hall.uoregon.edu
        The following are examples of invalid email addresses:
            b@norris2@uoregon.edu
            b norris@uoregon.edu
            bnorris2@uoregon..edu
            norris@uoregon.edu-org

    >>> validate_email('sozmatx807@yahoo.com')
    True

    >>> validate_email('meow8028@gmail.com')
    True
    
    >>> validate_email('blahblah blah@comcast.net')
    False
    """
    matches = []
    match_check = re.match(r'^\w+@\w+.+\w', email)
    if match_check == None:
        check = False
    else:
        matches.append(email)
        check = True
    return check

def main():
    """Use this main to do your own function calls and other testing, it will not be used in 
    grading."""


# --- You shouldn't need to change final_main ----
def final_main():
    """Run all the functions in this file."""
    for what in ['social_security_number', 'zip', 'zip_plus', 'email', 'phone']:
        func = globals()['validate_' + what]  # the function to call
        user_input = input(f"Please enter {what}: ")
        if func(user_input):   # call the function
            print(f"{user_input} is a valid {' '.join(what.split('_'))}.")
        else:
            print(f"{user_input} is NOT a valid {' '.join(what.split('_'))}.")


if __name__ == '__main__':
    main()
    #final_main()  # uncomment if you want to call all functions in this file