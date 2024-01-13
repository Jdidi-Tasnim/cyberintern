def check_password_complexity(password):
    # Define criteria
    length_criteria = 8
    uppercase_criteria = 1
    lowercase_criteria = 1
    digit_criteria = 1
    special_char_criteria = 1

    # Check length
    if len(password) < length_criteria:
        return "Weak: Password should be at least {} characters long.".format(length_criteria)

    # Check uppercase letters
    if not any(char.isupper() for char in password):
        return "Weak: Password should contain at least one uppercase letter."

    # Check lowercase letters
    if not any(char.islower() for char in password):
        return "Weak: Password should contain at least one lowercase letter."

    # Check digits
    if not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one digit."

    # Check special characters
    special_characters = set("!@#$%^&*(),.?\":{}|<>")
    if not any(char in special_characters for char in password):
        return "Weak: Password should contain at least one special character: !@#$%^&*(),.?\":{}|<>"

    # Strong password
    return "Strong: Password meets complexity criteria."

# Example usage:
password_input = input("Enter your password: ")
result = check_password_complexity(password_input)
print(result)
