import pandas as pd
import numpy as np
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import math
import statistics
from decimal import Decimal

def process_data(file_name):
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
        if (x_i+6.5)*(x_i+6.5) + (y_i)*(y_i) +(z_i)*(z_i) <= 25:
            new_x.append(x_i)
            new_y.append(y_i)
            new_z.append(z_i)
            new_e.append(e_i)
        
        if (x_i+29.5)*(x_i+29.5) + (y_i)*(y_i) +(z_i)*(z_i) <= 225:
            new_x.append(x_i)
            new_y.append(y_i)
            new_z.append(z_i)
            new_e.append(e_i)
        
        if (x_i-16.5)*(x_i-16.5) + (y_i)*(y_i) +(z_i)*(z_i) <= 225:
            new_x.append(x_i)
            new_y.append(y_i)
            new_z.append(z_i)
            new_e.append(e_i)
        
    x = np.array(new_x)
    y = np.array(new_y)
    z = np.array(new_z)
    ef = np.array(new_e)

    return x,y,z,ef

def plot(x, y, z, ef):

    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection='3d')


    img = ax.scatter(x, y, z, c=ef, cmap=plt.hot())
    fig.colorbar(img)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')


    plt.show()

def analyze(x,y,z,ef):
    new_e = []
    for i in range(0,len(x)):
        x_i = x[i]
        y_i = y[i]
        z_i = z[i]
        e_i = ef[i]
        check = radius_threshold(x_i,y_i,z_i,5)
        if check == True:
            new_e.append(e_i)
    return new_e

def radius_threshold(x,y,z,radius):
    r = round(math.sqrt((x+6.5)**2 + y**2 + z**2),1)
    if r == float(radius):
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
    return "{:.2E}".format(Decimal(statistics.mean(EF)))

def calculate_standard_deviation_EF(EF):
    return "{:.2E}".format(Decimal(statistics.mean(EF)))
        