from SERS_Substrate import *

def process_data(file_name, center, left, right, center_radius, big_radius):
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

        return x,y,z,ef

print("Begining simulation")
data = SERS_Substrate()
center = 0
left = -23
right = 23
center_radius = 5
big_radius = 15
file_name = 'e_field.txt'
x, y, z, ef = process_data(file_name,center, left, right, center_radius, big_radius)
data.set_x(x)
data.set_y(y)
data.set_z(z)
data.set_ef(ef)
print("Data Processed!")

EF = data.analyze(small_radius.get(), center.get(), max_radius.get())
EF = enhance_electric_field(EF)
message = 'Max = '+str("{:.2E}".format(Decimal(max(EF))))+'\n Mean = '+str(calculate_average_EF(EF))+'\n Median = '+str(calculate_median_EF(EF))+'\n Standard Deviation = '+str(calculate_standard_deviation_EF(EF))
print(message)