# Prompt the user for input
weight = float(input("Please enter your weight in kilograms: "))
height = float(input("Please enter your height in meters: "))

# Calculate the BMI
bmi = weight / (height ** 2)

# Determine BMI category and provide feedback
if bmi < 18.5:
    category = "underweight"
    advice = "It's important to eat a nutritious diet to gain weight in a healthy manner."
elif 18.5 <= bmi < 24.9:
    category = "normal weight"
    advice = "Great job! Maintain your current lifestyle to keep a healthy weight."
elif 25 <= bmi < 29.9:
    category = "overweight"
    advice = "Consider a balanced diet and regular exercise to lose weight healthily."
else:
    category = "obese"
    advice = "It's advisable to consult with a healthcare provider for a plan to reduce weight."

# Display the result
print(f"Your BMI is {bmi:.2f}. You are classified as {category}. {advice}")