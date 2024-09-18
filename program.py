# Basic Python Program

# Function to print a greeting message
def greet(name):
    return f"Hello, {name}!"

# Main function
if __name__ == "__main__":
    # Variables
    user_name = "World"

    # Conditional statement
    if user_name:
        print(greet(user_name))  # Output: Hello, World!
    else:
        print("Hello, Stranger!")

