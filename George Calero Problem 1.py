#problem 1
#user input
weight_pounds = float(input('Enter weight in pounds: '))
height_inches = float(input('Enter height in inches: '))

#calculate bmi using imperial formula
bmi_imperial = (weight_pounds / (height_inches **2)) * 703

#calculate bmi and convert to metric measures
weight_kilograms = weight_pounds * 0.453592
height_metric = height_inches * 0.0254
#metric formula
bmi_metric = weight_kilograms / (height_metric ** 2)


#display output
print('BMI (imperial): ', round(bmi_imperial, 2))
print('BMI (metric): ', round(bmi_imperial, 2))