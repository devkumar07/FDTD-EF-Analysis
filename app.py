import tkinter as tk
from tkinter import filedialog, messagebox
from SERS_Substrate import *

data = SERS_Substrate()

def enhance_electric_field(EF):
    for i in range(0,len(EF)):
        EF[i] = EF[i]**4
    return EF

def process_data(file_name, center, vertical_shift, left, right, center_radius, big_radius):
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
            if (x_i - float(center))*(x_i - float(center)) + (y_i - float(vertical_shift))*(y_i - float(vertical_shift)) +(z_i)*(z_i) <= (float(center_radius)**2):
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

def resultMessage(message):
    popup = tk.Toplevel()
    popup.title("Result")
    label = tk.Label(popup, text=message) #Can add a font arg here
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Close", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def convertData(event=None):
    x, y, z, ef = process_data(master.filename, center.get(), vertical_shift.get(), left.get(), right.get(), max_radius.get(), big_radius.get())
    data.set_x(x)
    data.set_y(y)
    data.set_z(z)
    data.set_ef(ef)
    resultMessage("Data Processed!")

def find_file(event=None):
    F = filedialog.askopenfile(
            initialdir="/",
            title="Select Electric Field file")
    master.filename = F.name

def visualize(event=None):
    print(master.filename)
    e_field = data.get_ef()
    e_field = enhance_electric_field(e_field)
    data.set_ef(e_field)
    data.plot()
    """
    x, y, z, ef = process_data(master.filename)
    plot(x,y,z,ef)
    """

def analyzeEF(event=None):
    print(master.filename)
    EF = data.analyze(small_radius.get(), center.get(), max_radius.get())
    """
    x, y, z, ef = process_data(master.filename)
    EF = analyze(x,y,z,ef)
    """
    EF = enhance_electric_field(EF)
    message = 'Max = '+str("{:.2E}".format(Decimal(max(EF))))+'\n Mean = '+str(calculate_average_EF(EF))+'\n Median = '+str(calculate_median_EF(EF))+'\n Standard Deviation = '+str(calculate_standard_deviation_EF(EF))
    resultMessage(message)

master = tk.Tk()

master.filename =''
tk.Label(master, text="Radius of Center Particle").grid(row=1)
tk.Label(master, text="Radius of Big Particles").grid(row=2)
tk.Label(master, text="Vertical Shift").grid(row=3)
tk.Label(master, text="X-Coordinate of Center Particle").grid(row=4)
tk.Label(master, text="X-Coordinate of Left Big Particle").grid(row=5)
tk.Label(master, text="X-Coordinate of Right Big Particle").grid(row=6)
tk.Label(master, text="Max Radius").grid(row=7)
small_radius = tk.Entry(master)
small_radius.grid(row=1, column=1)
big_radius = tk.Entry(master)
big_radius.grid(row=2, column=1)
vertical_shift = tk.Entry(master)
vertical_shift.grid(row=3, column=1)
center = tk.Entry(master)
center.grid(row=4, column=1)
left = tk.Entry(master)
left.grid(row=5, column=1)
right = tk.Entry(master)
right.grid(row=6, column=1)
max_radius = tk.Entry(master)
max_radius.grid(row=7, column=1)

tk.Button(
        master, text="Import FDTD Electric Field file",
        command=find_file).grid(column=0, row=8, padx=20, pady=5)
tk.Button(master, text='Convert Data', command=convertData).grid(row=9, column=0, sticky=tk.W, pady=4)
tk.Label(master, text=master.filename).grid(row=9, column = 1)
tk.Button(master, text='Quit', command=master.quit).grid(row=10, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Visualize!', command=visualize).grid(row=10, column=1, sticky=tk.W, pady=4)
tk.Button(master, text='Analyze!', command=analyzeEF).grid(row=10, column=2, sticky=tk.W, pady=4)

tk.mainloop()