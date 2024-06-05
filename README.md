# BMI Calculator

A simple Python application to calculate Body Mass Index (BMI) and determine the BMI category based on the user's weight and height.

## Features

- Calculates BMI using the formula: weight (kg) / (height (m) ^ 2)
- Determines BMI category:
  - Underweight: BMI < 18.5
  - Normal weight: 18.5 <= BMI < 24.9
  - Overweight: 25 <= BMI < 29.9
  - Obesity: BMI >= 30
- Validates user input to ensure weight and height are positive numbers

## Requirements

- Python 3.x

## How to Run

1. Clone this repository or download the `bmi_calculator.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `bmi_calculator.py` file is located.
4. Run the script using Python:

    ```bash
    python bmi_calculator.py
    ```

5. Follow the prompts to input your weight in kilograms and height in meters.

## Sample Run

```plaintext
BMI Calculator
Enter your weight in kilograms: 70
Enter your height in meters: 1.75

Your BMI is: 22.86
Category: Normal weight