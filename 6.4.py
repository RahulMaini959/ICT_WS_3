count = 0  # Initialize a counter for the lines

try:
    while True:
        user_input = input()  # Take input from the user
        print(user_input)  # Print the input
        count += 1  # Increment the line counter

except KeyboardInterrupt:
    print("\nProgram interrupted by the user (CTRL-C).")
    print(f"Total lines entered: {count}")
