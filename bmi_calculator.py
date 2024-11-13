# Isaiah Lugo
# Midterm Design - CSM III
# Week 5 Assignment - BMI Calculator

# Initialize lists to store heights(in), weights(lbs), and BMIs
heights = [] 
weights = []
bmis = []

# Initialize variables to count underweight, normal weight, and overweight individuals
uw_count = 0
n_count = 0
ow_count = 0

for i in range(6): # There are 6 individuals for each case that will be looped through
    height = input('Enter height (in inches): ') # Prompt for input of height in inches
    weight = input('Enter weight (in pounds): ') # Prompt for input of weight in pounds
    
    # Now we convert height and weight to float and store in arrays
    heights.append(float(height))
    weights.append(float(weight))
    
    # BMI calculation with given info
    bmi = (weights[i] / (heights[i]**2)) * 703
    bmis.append(bmi)
    
    # Classify BMI scores to determine weight class
    if bmi < 18.5:
        uw_count += 1
    elif 18.5 <= bmi < 24.9:
        n_count += 1
    else:
        ow_count += 1

# Output the BMI for each individual
for i in range(6):
    print(f"Individual {i+1} has a BMI of {bmis[i]}")

# Output the count of underweight, normal weight, and overweight individuals
print(f"Underweight: {uw_count}")
print(f"Normal weight: {n_count}")
print(f"Overweight: {ow_count}")
    