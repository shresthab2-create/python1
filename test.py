#This is input by User
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter the interest rate (in percentage): "))
time = int(input("Enter the time period (in years): "))

# Calculate simple interest
simple = ((principal * rate * time) / 100)

# Display the result
print(f"The calculated simple interest is: {simple}")