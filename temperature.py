
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temp = float(input("Enter temperature: "))
unit = input("Enter temperature unit (C or F): ")

if unit == "C".lower():
    converted_temp = celsius_to_fahrenheit(temp)
    print("{:.2f}C is equivalent to {:.2f}F".format(temp, converted_temp))
    
elif unit == "F".lower():
    converted_temp = fahrenheit_to_celsius(temp)
    print("{:.2f}F is equivalent to {:.2f}C".format(temp, converted_temp ))
    
else:
    print("Error : invalid unit entered, please enter C or F")    
    