# Initialize an empty list to store student names
class_list = []

print("Enter student names to build the class list. Type 'done' to finish.")

# Start the loop to collect student names
while True:
    student_name = input("Enter student name: ")
    if student_name.lower() == 'done':  # Exit condition
        break
    class_list.append(student_name)
    print(f"Added {student_name} to the class.")

# Print the final class list
print("\nClass List:")
for student in class_list:
    print(student)
