FDTD 3D Visualization and EF Particle Analysis

Requirements
  - Python3
  - Anaconda/Python Modules: Pandas, Numpy, Matplotlib
  - A ".txt" file containing the x,y,z coordinates and the respective Electric Field values
  
 Step 1: Export the Electric Field data to a text file
 
    Using the ".lsf" script provided in this repository, import the script to FDTD and change the Montior title and the wavelength index as desired in the ".lsf" script. 
    Execute the script and the electric field scirpt will be exported.
    
    For more information, please refer to: https://support.lumerical.com/hc/en-us/articles/360034923933-Creating-3D-visualizations-with-MATLAB 
    
  Step 2: Using the application

      Open terminal (Mac OS) or Command prompt (Windows) and navigate to the respective destination where the repository is located on your computer. 
      Type "python3 app.py"
      You will be greeted with a Dialog box. 
      
  Step 3: Process the Data
  
      Fill the corresponding information of the substrate including the radius and the coordinates of the structure.
      Click on "Import FDTD Electric Field file" to import the recently exported text file containing the E-Field values.
      Click on "Convert Data" for the application to process the data into something the application can understand. When successful, you will recieve a message saying the Data is processed.
  
  Step 4: Choose the functionality you desire
  
      That is it! Click on visualize if you would like to see the 4-D projection of the substrate or click on analyze to get statistical analysis about the substrate!
      

Coming soon: A stand-alone executable is under production and will be released soon.


Note: This application currently only supports the visualization and analysis of trimer structures.
      
  
