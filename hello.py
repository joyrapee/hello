def say_hello(name):
    """Function that returns a greeting message."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name:")  # Ask for user input
    print(say_hello(user_name))  # Print the greeting message
