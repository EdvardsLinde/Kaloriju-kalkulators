def calorie_needs(Weight, Height, Age, Gender, Activity_level):

    if Gender.lower() == 'male':
        bmr = 88.362 + (13.397 * Weight) + (4.799 * Height) - (5.677 * Age)
    elif Gender.lower() == 'female':
        bmr = 447.593 + (9.247 * Weight) + (3.098 * Height) - (4.330 * Age)
    else:
        return "Invalid gender input"

    activity_factors = {
        'Low activity': 1.2,
        'Light activity': 1.375,
        'Moderate activity': 1.55,
        'High activity': 1.725,
        'Very high activity': 1.9
    }

    if Activity_level in activity_factors:
        calories = bmr * activity_factors[Activity_level]
    else:
        return "Invalid activity level input"
    
    round(calories)

    deficit_calories = calories - 500
    surplus_calories = calories + 500

    return {
        'maintenance': round(calories),
        'deficit': round(deficit_calories),
        'surplus': round(surplus_calories)
    }


Weight = float(input("Enter your weight (kg): "))
Height = float(input("Enter your height (cm): "))
Age = int(input("Enter your age: "))
Gender = input("Enter your gender (male/female): ")
Activity_level = input("Enter your activity level (Low activity, Light activity, Moderate activity, High activity, Very high activity): ")


results = calorie_needs(Weight, Height, Age, Gender, Activity_level)

if isinstance(results, dict):
    print(f"To maintain your weight: {results['maintenance']} kcal/day")
    print(f"For weight loss (deficit): {results['deficit']} kcal/day")
    print(f"For weight gain (surplus): {results['surplus']} kcal/day")
else:
    print(results)