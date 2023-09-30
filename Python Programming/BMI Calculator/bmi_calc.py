def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")
    weight_kg = float(input("Enter your weight in kilograms: "))
    height_m = float(input("Enter your height in meters: "))

    if weight_kg <= 0 or height_m <= 0:
        print("Invalid input. Weight and height must be positive.")
    else:
        bmi = calculate_bmi(weight_kg, height_m)
        category = classify_bmi(bmi)
        print(f"Your BMI is {bmi:.2f}, which is categorized as '{category}'.")

if __name__ == "__main__":
    main()
