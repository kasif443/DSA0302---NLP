import re

# Student Details
reg_no = "23CSE101"
email = "23cse101@university.edu"
course_code = "CSE202"
semester = "5"
mobile = "9876543210"

# Validate Register Number
if re.fullmatch(r"\d{2}[A-Z]{3}\d{3}", reg_no):
    print("Register Number: Valid")
    reg_valid = True
else:
    print("Register Number: Invalid")
    reg_valid = False

# Validate Email
if re.fullmatch(r"[a-zA-Z0-9._%+-]+@university\.edu", email):
    print("Email: Valid")
    email_valid = True
else:
    print("Email: Invalid")
    email_valid = False

# Validate Course Code
if re.fullmatch(r"[A-Z]{3}\d{3}", course_code):
    print("Course Code: Valid")
    course_valid = True
else:
    print("Course Code: Invalid")
    course_valid = False

# Validate Semester (1 to 8)
if re.fullmatch(r"[1-8]", semester):
    print("Semester: Valid")
    sem_valid = True
else:
    print("Semester: Invalid")
    sem_valid = False

# Validate Mobile Number
if re.fullmatch(r"[6-9]\d{9}", mobile):
    print("Mobile Number: Valid")
    mobile_valid = True
else:
    print("Mobile Number: Invalid")
    mobile_valid = False

# Final Registration Status
if reg_valid and email_valid and course_valid and sem_valid and mobile_valid:
    print("\nRegistration Status: Successful")
else:
    print("\nRegistration Status: Failed")
