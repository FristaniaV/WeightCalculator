def BMI():
    height = float(input('Enter the height in cm: '))
    weight = float(input('Enter the weigth in kg: '))

    height = height/100

    bmi = weight / (height * height)

    if (bmi < 18.5):
        bmiRes = "underweight"
    elif (bmi >= 18.5 and bmi < 25):
        bmiRes = "ideal"
    elif (bmi >= 25 and bmi < 29.9):
        bmiRes = "overweight"
    elif (bmi >= 30):
        bmiRes = "obesity"

    print()
    print(f"Your BMI is {bmi} and you are {bmiRes}")
    print()

    choice = str(input('Do you still want to use the calculator [y | n] ? '))
    if (choice == 'y'):
        Menu()
    elif (choice == 'n'):
        print("Thank you for using this application!")
        quit()

def WHR():
    gender = str(input('Enter gender [woman || man]: '))
    waist = float(input('Enter waist size in cm: '))
    hip = float(input('Enter hip size in cm: '))

    wrh = waist / hip

    if (gender == "man"):
        if (wrh < 0.9):
            wrhRes = "low"
        elif (wrh >= 0.9 and wrh < 0.99):
            wrhRes = "medium"
        elif (wrh >= 1):
            wrhRes = "high"
    elif (gender == "woman"):
        if (wrh < 0.8):
            wrhRes = "low"
        elif (wrh >= 0.8 and wrh < 0.89):
            wrhRes = "medium"
        elif (wrh >= 0.9):
            wrhRes = "high"

    print()
    print(f"Your waist-to-hip ratio is {wrh} and your cardiovascular risk is {wrhRes}")
    print()

    choice = str(input('Do you still want to use the calculator [y | n] ? '))
    if (choice == 'y'):
        Menu()
    elif (choice == 'n'):
        print("Thank you for using this application!")
        quit()


def RFM():
    gender = str(input('Enter gender [woman || man]: '))
    height = float(input('Enter the height in cm: '))
    waist = float(input('Enter waist size in cm: '))

    hxw = height / waist

    if (gender == "man"):
        rfm = 64 - (20 * hxw)
        if (rfm >= 18 and rfm <= 24):
            rfmRes = "average"
        elif (rfm > 24):
            rfmRes = "obese"
    elif (gender == "woman"):
        rfm = 76 - (20 * hxw)
        if (rfm >= 25 and rfm <= 31):
            rfmRes = "average"
        elif (rfm > 31):
            rfmRes = "obese"

    print()
    print(f"Your RFM is {rfm}%. It's {rfmRes}.")
    print()

    choice = str(input('Do you still want to use the calculator [y | n] ? '))
    if (choice == 'y'):
        Menu()
    elif (choice == 'n'):
        print("Thank you for using this application!")
        quit()

def Menu():           
    print('Welcome to Weight Calculator!')
    print()

    print('1. Body Mass Index')
    print('2. Waist-to-hip ratio')
    print('3. Relative Fat Mass')

    choose = int(input('>> '))

    print()

    if (choose == 1):
        BMI()
    elif (choose == 2):
        WHR()
    elif (choose == 3):
        RFM()

Menu()
