students = []  # List to store student names

while True:
    student_name = input("Enter student name (or type 'quit', 'exit', or '0' to stop): ").strip()
    
    # Check for exit conditions
    if student_name.lower() in ['quit', 'exit', '0']:
        print("\nExiting the program...")
        print(f"Exit parameter: '{student_name}'")
        print(f"Total students entered: {len(students)}")
        print("List of students:", ", ".join(students))
        break  # Exit the loop
    
    # Add the student to the list if not exiting
    students.append(student_name)



students = []  # List to store student names
active = True  # Active variable to control the loop

while active:
    student_name = input("Enter student name (or type 'stop' to end): ").strip()
    
    # Check for exit condition
    if student_name.lower() == 'stop':
        active = False  # Set active to False to end the loop
        print("\nExiting the program...")
    
    else:
        students.append(student_name)  # Add the student to the list

# Print the final list of students and the total count
print(f"\nTotal students entered: {len(students)}")
print("List of students:", ", ".join(students))



max_cap = int(input("Enter room capacity: "))  # Get room capacity
students = []  # List to store student names

while True:
    student_name = input("Enter student name: ").strip()
    
    # Add student to the list
    students.append(student_name)
    
    # Check if we reached the room's capacity
    if len(students) >= max_cap:
        print("\nRoom capacity reached! Exiting...")
        break  # Exit the loop

# Print the final list of students and the max capacity
print(f"\nTotal students entered: {len(students)} (Max Capacity: {max_cap})")
print("List of students:", ", ".join(students))



count = 0  # Initialize a counter for the lines

try:
    while True:
        user_input = input()  # Take input from the user
        print(user_input)  # Print the input
        count += 1  # Increment the line counter

except KeyboardInterrupt:
    print("\nProgram interrupted by the user (CTRL-C).")
    print(f"Total lines entered: {count}")
