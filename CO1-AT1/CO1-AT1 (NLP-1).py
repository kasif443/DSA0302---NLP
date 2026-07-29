import re

# Sample Resume
resume = """
Name: Rahul Sharma
Email: rahul.sharma@gmail.com
Phone: 9876543210

Skills: Python, Java, SQL, Machine Learning

Experience: 3 years
"""

# Extract Name
name = re.search(r"Name:\s*(.*)", resume)
if name:
    name = name.group(1)

# Extract Email
email = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", resume)

# Extract Mobile Number
phone = re.findall(r"\b\d{10}\b", resume)

# Detect Technical Skills
skills = ["Python", "Java", "SQL", "Machine Learning", "NLP"]
found_skills = []

for skill in skills:
    if re.search(skill, resume, re.IGNORECASE):
        found_skills.append(skill)

# Extract Years of Experience
exp = re.search(r"(\d+)\s+years?", resume, re.IGNORECASE)
experience = int(exp.group(1)) if exp else 0

# Display Structured Summary
print("----- Candidate Profile -----")
print("Name:", name)
print("Email:", email[0] if email else "Not Found")
print("Phone:", phone[0] if phone else "Not Found")
print("Skills:", ", ".join(found_skills))
print("Experience:", experience, "years")

# Eligibility Check
if experience >= 2 and "Python" in found_skills:
    print("\nStatus: Eligible for Shortlisting")
else:
    print("\nStatus: Not Eligible")
