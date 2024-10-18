Function to calculate daily calorie needs based on user input
def calorie_needs(Weight, Height, Age, Gender, Activity_level):
    
    # Calculate Basal Metabolic Rate (BMR) for males
    if Gender.lower() == 'male':
        bmr = 88.362 + (13.397 * Weight) + (4.799 * Height) - (5.677 * Age)
    # Calculate BMR for females
    elif Gender.lower() == 'female':
        bmr = 447.593 + (9.247 * Weight) + (3.098 * Height) - (4.330 * Age)
    # Return an error message if the gender input is invalid
    else:
        return "Invalid gender input"
    
    # Dictionary mapping activity levels to their corresponding multipliers
    activity_factors = {
        'Low activity': 1.2,           # Sedentary or very light activity
        'Light activity': 1.375,       # Light exercise or sports 1-3 days a week
        'Moderate activity': 1.55,     # Moderate exercise or sports 3-5 days a week
        'High activity': 1.725,        # Hard exercise or sports 6-7 days a week
        'Very high activity': 1.9      # Very hard physical activity or a labor-intensive job
    }
    
    # Check if the provided activity level is valid
    if Activity_level in activity_factors:
        # Calculate daily calorie needs based on BMR and activity level
        calories = bmr * activity_factors[Activity_level]
    else:
        # Return an error message if the activity level input is invalid
        return "Invalid activity level input"
    
    # Round off the calorie values
    round(calories)
    
    # Calculate calorie needs for weight loss (500 kcal deficit) and weight gain (500 kcal surplus)
    deficit_calories = calories - 500
    surplus_calories = calories + 500
    
    # Return a dictionary containing the maintenance, deficit, and surplus calorie values
    return {
        'maintenance': round(calories),          # Calories needed to maintain current weight
        'deficit': round(deficit_calories),      # Calories needed for weight loss
        'surplus': round(surplus_calories)       # Calories needed for weight gain
    }

# Function to interact with the user and get their details
def action():
    # Ask the user for their weight, height, age, gender, and activity level
    Weight = float(input("Enter your weight (kg): "))
    Height = float(input("Enter your height (cm): "))
    Age = int(input("Enter your age: "))
    Gender = input("Enter your gender (male/female): ")
    Activity_level = input("Enter your activity level (Low activity, Light activity, Moderate activity, High activity, Very high activity): ")
    
    # Call the calorie_needs function with user inputs and store the result
    results = calorie_needs(Weight, Height, Age, Gender, Activity_level)
    
    # Check if the result is a dictionary (valid output)
    if isinstance(results, dict):
        # Print the user's maintenance, deficit, and surplus calorie needs
        print(f"To maintain your weight: {results['maintenance']} kcal/day")
        print(f"For weight loss (deficit): {results['deficit']} kcal/day")
        print(f"For weight gain (surplus): {results['surplus']} kcal/day")
    else:
        # Print an error message if the result is not valid
        print(results)

# Loop to allow the user to repeat the process
answer = "yes"
while answer == "yes":
    action()  # Call the action function to calculate calorie needs
    answer = input("Gribi atkārtot? (ievadi 'yes'): ")  # Ask the user if they want to repeat the process
