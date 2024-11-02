# Initialize an empty dictionary for departments
departments = {}

# List of courses based on the given table
course_data = [
    ("CS101", "Introduction to Computer Science", "Computer Science", "S1"),
    ("CS202", "Data Structures and Algorithms", "Computer Science", "S2"),
    ("MATH101", "Calculus I", "Mathematics", "S1"),
    ("MATH102", "Calculus II", "Mathematics", "S2"),
    ("PHY101", "General Physics I", "Physics", "S1"),
    ("PHY102", "General Physics II", "Physics", "S2"),
    ("CHEM101", "General Chemistry I", "Chemistry", "S1"),
    ("CHEM102", "General Chemistry II", "Chemistry", "S2"),
    ("BIO101", "Biology I", "Biology", "S1"),
    ("BIO102", "Biology II", "Biology", "S2"),
    ("HIST101", "American History I", "History", "S1"),
    ("HIST102", "American History II", "History", "S2"),
    ("ENGL101", "English Composition I", "English", "S1"),
    ("ENGL102", "English Composition II", "English", "S2"),
    ("ECON101", "Principles of Economics", "Economics", "S1"),
    ("ECON102", "Intermediate Microeconomics", "Economics", "S2"),
    ("PSY101", "Introduction to Psychology", "Psychology", "S1"),
    ("PSY102", "Developmental Psychology", "Psychology", "S2"),
    ("SOC101", "Introduction to Sociology", "Sociology", "S1"),
    ("SOC102", "Social Problems", "Sociology", "S2")
]

# Populate the departments dictionary
for course_id, course_name, department, semester in course_data:
    if department not in departments:
        departments[department] = []  # Initialize an empty list for courses
    departments[department].append((course_id, course_name))  # Add course tuple

# Print the courses for each department
print("Class Schedule by Department:")
for department, courses in departments.items():
    print(f"\nDepartment: {department}")
    for course_id, course_name in courses:
        print(f"  - {course_id}: {course_name}")
