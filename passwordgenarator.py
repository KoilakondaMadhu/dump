def generate_password(number, name):
    # Check if name consists of only lowercase letters
    if name.isalpha() and name.islower():
        # Convert number to absolute value to handle negative numbers
        abs_number = abs(number)
        
        # Ensure length of name is within the specified range
        name_length = min(max(len(name), 1), 100)
        
        # Generate password using a combination of number and name
        password = str(abs_number) + name[:name_length]
        return password
    else:
        return "Invalid"

# Input: Number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Input: Number and Name separated by space
    test_input = input().split()
    number = int(test_input[0])
    name = test_input[1]

    # Output: Print the password for each test case in a new line
    result = generate_password(number, name)
    print(result)