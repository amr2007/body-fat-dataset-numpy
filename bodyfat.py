import numpy as np 

data = np.genfromtxt('bodyfat.csv', delimiter=',', skip_header=1)

print(data.shape)
print(data[:5])
print(data.dtype)


body_fat = data[:,1]

# max bodyfat
max_bodyfat = np.max(body_fat)


# min bodyfat
min_bodyfat = np.min(body_fat)

# Age
age = data[:,2]

# Average bodyfat
avg_bodyfat = np.mean(body_fat)

# BMI
weight = data[:,3]
height = data[:,4]
bmi = (weight * 703)/ height**2

print(f"min Age: {int(np.min(age))}")
print(f"max Age: {int(np.max(age))}")
print(f"min Bodyfat: {min_bodyfat:.2f}%")
print(f"max Bodyfat: {max_bodyfat:.2f}%")
print(f"Average Body fat: {avg_bodyfat:.2f}%")
print(f"BMI: {np.round(bmi, 2)}")
print(f"Average BMI: {np.mean(bmi):.2f}")