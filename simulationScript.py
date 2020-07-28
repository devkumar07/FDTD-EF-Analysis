import pandas as pd
import numpy as np
import math
import statistics
from decimal import Decimal


def radius_threshold(x_i , y_i, z_i, radius, max_radius, center):
    r = round(math.sqrt((x_i - float(center))**2 + y_i**2 + z_i**2),1)
    if r >= float(radius) and r <= float(max_radius):
        return True
    else:
        return False

def enhance_electric_field(EF):
    for i in range(0,len(EF)):
        EF[i] = EF[i]**4
    return EF

def calculate_average_EF(EF):
    return "{:.2E}".format(Decimal(statistics.mean(EF)))

def calculate_median_EF(EF):
    return "{:.2E}".format(Decimal(statistics.median(EF)))

def calculate_standard_deviation_EF(EF):
    return "{:.2E}".format(Decimal(statistics.stdev(EF)))

print("Begining simulation")
data = SERS_Substrate()
center = 0
left = -23
right = 23
center_radius = 5
big_radius = 15
file_name = 'e_field.txt'
x, y, z, ef = process_data(file_name,center, left, right, center_radius, big_radius)

data = pd.read_csv(file_name, sep='\t', header=None)
x = data.iloc[0]
x = x.multiply(other = 1000000000, fill_value = 0)
x = x.values
y = data.iloc[1]
y = y.multiply(other = 1000000000, fill_value = 0)
y = y.values
z = data.iloc[2]
z = z.multiply(other = 1000000000, fill_value = 0)
z = z.values
ef = data.iloc[3]
ef = ef.values
new_x = []
new_y = []
new_z = []
new_e = []

for i in range(0,len(x)):
    x_i = x[i]
    y_i = y[i]
    z_i = z[i]
    e_i = ef[i]
    if (x_i - float(center))*(x_i - float(center)) + (y_i)*(y_i) +(z_i)*(z_i) <= (float(center_radius)**2):
        new_x.append(x_i)
        new_y.append(y_i)
        new_z.append(z_i)
        new_e.append(e_i)
    
    if (x_i - float(left))*(x_i - float(left)) + (y_i)*(y_i) +(z_i)*(z_i) <= (float(big_radius)**2):
        new_x.append(x_i)
        new_y.append(y_i)
        new_z.append(z_i)
        new_e.append(e_i)
    
    if (x_i - float(right))*(x_i - float(right)) + (y_i)*(y_i) +(z_i)*(z_i) <= (float(big_radius)**2):
        new_x.append(x_i)
        new_y.append(y_i)
        new_z.append(z_i)
        new_e.append(e_i)
    
x = np.array(new_x)
y = np.array(new_y)
z = np.array(new_z)
ef = np.array(new_e)

print("Data Processed!")

new_e = []
for i in range(0,len(x)):
    x_i = x[i]
    y_i = y[i]
    z_i = z[i]
    e_i = ef[i]
    check = radius_threshold(x_i,y_i,z_i, radius, max_radius, center)
    if check == True:
        new_e.append(e_i)

EF = enhance_electric_field(new_e)
message = 'Max = '+str("{:.2E}".format(Decimal(max(EF))))+'\n Mean = '+str(calculate_average_EF(EF))+'\n Median = '+str(calculate_median_EF(EF))+'\n Standard Deviation = '+str(calculate_standard_deviation_EF(EF))
print(message)
