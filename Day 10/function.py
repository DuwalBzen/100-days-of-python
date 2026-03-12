# Functions and Outputs
# DocSting -> Use for multiline or comment that document your code

# You can also use the title function
"""
def format_name(f_name, l_name):
    formated_f_name = ""
    formated_l_name = ""
    for index, char in enumerate(f_name):
        if index == 0:
            formated_f_name += char.upper()
        else:
            formated_f_name += char

    for index, char in enumerate(l_name):
        if index == 0:
            formated_l_name += char.upper()
        else:
            formated_l_name += char


    print(formated_f_name, formated_l_name)
"""
def format_name(f_name, l_name):
    """Take a first and last name and format it to return the
    title case version of the name."""
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

f_name = input("Enter your first name: ").lower()
l_name = input("Enter your last name: ").lower()

formated_string = format_name(f_name, l_name)
print(formated_string)

