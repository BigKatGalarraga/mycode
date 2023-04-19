def check_even_odd():
    # Get input from user
    num = int(input("Enter a number: "))

    # Check if the number is even or odd
    if num % 2 == 0:
        print(num, "is an even number.")
    else:
        print(num, "is an odd number.")

# Call the function to execute it
check_even_odd()

