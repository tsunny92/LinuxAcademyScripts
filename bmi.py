#!/usr/bin/env python3.6

# BMI = (Weight in kg / height in meters measured)

def details():
    height = float(input("Enter the height in inches or meters "))
    weight = float(input("Enter the weight in pounds or kilograms "))
    system = input("Are you measuremens in imperial or metric ").lower().strip()
    return (height, weight, system)

def cal_bmi(height, weight, system='metric'):
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2 ))
    return bmi

while True:
    height , weight , system = details()
    if system.startswith('i'):
        bmi = cal_bmi(height, weight, system)
        print(f"Your BMI is {bmi}")
        break
    elif system.startswith('m'):
        bmi = cal_bmi(height, weight)
        print(f"Your BMI is {bmi}")
        break
    else:
        print(f"Kindly use correct measurements system ")
         
