# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter

email = "elek.viz@exam.com"

def name_from_email(email):
    full_name = email.rsplit('@')[0]
    last_name = full_name.split('.')[1]
    first_name = full_name.split('.')[0]
    name = (last_name + " " + first_name)
    print(name.title())

name_from_email(email)