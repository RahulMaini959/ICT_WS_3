# Initialize an empty dictionary for course enrollments
course_enrollments = {}

# List of enrollments based on the given table
enrollment_data = [
    (1001, "CS101", "S1"), (1001, "MATH101", "S1"),
    (1002, "CS101", "S1"), (1002, "MATH102", "S2"),
    (1003, "CS202", "S2"), (1003, "PHY101", "S1"),
    (1004, "CS202", "S2"), (1004, "CHEM101", "S1"),
    (1005, "BIO101", "S1"), (1005, "HIST101", "S1"),
    (1006, "BIO102", "S2"), (1006, "ENGL101", "S1"),
    (1007, "ECON101", "S1"), (1007, "PSY101", "S1"),
    (1008, "ECON102", "S2"), (1008, "SOC101", "S1"),
    (1009, "PSY102", "S2"), (1009, "SOC102", "S2"),
    (1010, "CS101", "S1"), (1010, "MATH101", "S1")
]

# Populate the course_enrollments dictionary
for student_id, course_id, semester in enrollment_data:
    if student_id not in course_enrollments:
        course_enrollments[student_id] = []  # Initialize an empty list for courses
    course_enrollments[student_id].append(course_id)

# Print the course enrollments
print("Student Course Enrollments:")
for student_id, courses in course_enrollments.items():
    print(f"Student ID {student_id}: Enrolled in {', '.join(courses)}")