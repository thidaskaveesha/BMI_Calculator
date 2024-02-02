from time import sleep

def bmi():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers for weight and height.")
        return

    bmi_value = weight / height**2

    def show(bmi):
        if bmi < 18.5:
            print("You are Underweight")
        elif 18.5 <= bmi < 24.9:
            print("You are Normal")
        elif 25 <= bmi < 29.9:
            print("You are Overweight")
        elif bmi >= 30:
            print("You are Obese")

    print("\n")
    show(bmi_value)
    print("\n")

while True:
    bmi()
    choice = input("Do you want to close this program? (y/n): \n \n")
    if choice.lower() == "y":
        print("\nThank you for using this package!")
        sleep(2)
        break

