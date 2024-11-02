# Initialize the lecturer assignments dictionary
lecturer_assignments = {
    "Dr. John Doe": ["CS101", "CS202"],
    "Prof. Jane Smith": ["MATH101", "MATH102"],
    "Mr. Michael Johnson": ["PHY101", "PHY102"],
    "Dr. Emily Brown": ["CHEM101", "CHEM102"],
    "Prof. David Lee": ["BIO101", "BIO102"],
    "Asst. Prof. Olivia Taylor": ["ENGL101", "ENGL102"],
    "Dr. Noah Wilson": ["ECON101", "ECON102"],
    "Miss. Sophia Carter": ["PSY101", "PSY102"],
    "Asst. Prof. Jacob Miller": ["SOC101", "SOC102"],
    "Dr. Emma Davis": ["CS101", "MATH101"],
    "Mrs. Ethan Jones": ["CHEM101", "PHY101"],
    "Asst. Prof. Ava Martinez": ["BIO102", "HIST102"],
    "Dr. Oliver Hernandez": ["HIST101", "ENGL101"],
    "Prof. Isabella Garcia": ["PSY102", "SOC102"],
    "Asst. Prof. Liam Lopez": ["CS202", "ECON102"],
    "Dr. Mia Gonzalez": ["MATH102", "PHY102"],
    "Prof. Elijah Rodriguez": ["SOC101", "ENGL102"],
    "Asst. Prof. Amelia Perez": ["BIO101", "ECON101"],
    "Dr. Lucas Sanchez": ["PSY101", "HIST101"],
    "Prof. Evelyn Russell": ["CS101", "CHEM102"]
}

# Loop through the dictionary and print the lecturer assignments
print("Lecturer Assignments:")
for lecturer, courses in lecturer_assignments.items():
    print(f"\nLecturer: {lecturer}")
    for course in courses:
        print(f"  - {course}")
