# Prompt the user for input by completing the code
num1 = input(float())
num2 = input(float())

# Perform calculations
# Input the code needed to create the calculations
# There should be three code lines to resolve this
addition_result = num1 + num2
subtraction_result = num1 - num2
multiplication_result = num1 * num2

# Handle division by zero
if num2 != 0:
    # Input the code to resolve this
    division_result = "Error! You've entered 0 as a divisor"
else:
    # Input the code to resolve this
    division_result = num1 / num2

# Display the results
# Complete the code to display the calculations
# there should be four print statements
print(f"{num1} + {num2} = {addition_result}")
print(f"{num1} - {num2} = {subtraction_result}")
print(f"{num1} * {num2} = {multiplication_result}")
print(f"{num1} / {num2} = {division_result}")