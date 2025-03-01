#Check bmi
bmi_value = float(input("Enter you Bmi : "))
if bmi_value < 18.5:
    print("Underweight")
elif bmi_value < 25 :
    print("Normal weight")
else:
    print("Overweight")