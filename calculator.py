# Define a function to perform the calculations
def calculate(num1, num2, operation):
  # Check the operation and perform the calculation
  if operation == "add":
    return num1 + num2
  elif operation == "subtract":
    return num1 - num2
  elif operation == "multiply":
    return num1 * num2
  elif operation == "divide":
    return num1 / num2

# Define the main function
def main():
  # Print a welcome message
  print("Welcome to the calculator app!")

  # Loop until the user chooses to quit
  while True:
    # Get the first number and the operation from the user
    num1 = float(input("Enter the first number: "))
    operation = input("Enter the operation (+, -, *, or /): ")

    # Check if the user wants to quit
    if operation == "q":
      break

    # Get the second number from the user
    num2 = float(input("Enter the second number: "))

    # Perform the calculation
    result = calculate(num1, num2, operation)

    # Print the result
    print("The result is:", result)

# Call the main function
main()
