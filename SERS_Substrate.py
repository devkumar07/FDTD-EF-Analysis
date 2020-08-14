#This is a class for SERS Substrate
import pandas as pd
import numpy as np
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import math
import statistics
from decimal import Decimal


class SERS_Substrate:
    def __init__(self, x = '', y = '' , z = '', ef = ''):
        self.x = x
        self.y = y
        self.z = z
        self.ef = ef
    
    # Defining Getters

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def get_z(self):
        return self.z
    
    def get_ef(self):
        return self.ef

    # Defining Setters
    
    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y

    def set_z(self, z):
        self.z = z
    
    def set_ef(self, ef):
        self.ef = ef

    def plot(self):

        fig = plt.figure(figsize=(8,8))
        ax = fig.add_subplot(111, projection='3d')

        ef = self.ef
        ef = np.log10(ef)
        
        img = ax.scatter(self.x, self.y, self.z, c=ef, cmap=plt.hot())
        fig.colorbar(img)

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')


        plt.show()

    def analyze(self, radius, center, max_radius):

        new_e = []
        x = self.x
        y = self.y
        z = self.z
        ef = self.ef
        for i in range(0,len(x)):
            x_i = x[i]
            y_i = y[i]
            z_i = z[i]
            e_i = ef[i]
            check = radius_threshold(x_i,y_i,z_i, radius, max_radius, center)
            if check == True:
                new_e.append(e_i)
        return new_e

def radius_threshold(x_i , y_i, z_i, radius, max_radius, center):
        r = round(math.sqrt((x_i - float(center))**2 + y_i**2 + z_i**2),1)
        if r >= float(radius) and r <= float(max_radius):
            return True
        else:
            return False
def calculate_average_EF(EF):
    return "{:.2E}".format(Decimal(statistics.mean(EF)))

def calculate_median_EF(EF):
    return "{:.2E}".format(Decimal(statistics.median(EF)))

def calculate_standard_deviation_EF(EF):
    return "{:.2E}".format(Decimal(statistics.stdev(EF)))