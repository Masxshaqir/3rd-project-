# Function to calculate BMI
def calculate_bmi(weight, height):
    # Calculate BMI using the formula: weight (kg) / (height (m) ^ 2)
    bmi = weight / (height ** 2)
    return bmi

# Function to get the BMI category based on BMI value
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Function to get a valid number input from the user
def get_valid_input(prompt):
    while True:
        try:
            # Ask the user to enter a number
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                # Inform the user if they entered a non-positive number
                print("Please enter a positive number.")
        except ValueError:
            # Inform the user if they entered an invalid input
            print("Invalid input. Please enter a number.")

def main():
    # Print a welcome message
    print("BMI Calculator")

    # Get the user's weight in kilograms with validation
    weight = get_valid_input("Enter your weight in kilograms: ")

    # Get the user's height in meters with validation
    height = get_valid_input("Enter your height in meters: ")

    # Calculate the BMI
    bmi = calculate_bmi(weight, height)

    # Get the BMI category
    category = get_bmi_category(bmi)

    # Print the BMI value
    print(f"\nYour BMI is: {bmi:.2f}")

    # Print the BMI category
    print(f"Category: {category}")

# This line ensures that the main function runs when the script is executed
if __name__ == "__main__":
    main()