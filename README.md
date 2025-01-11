### **Application Purpose**  
This application provides a simple and intuitive GUI for executing a compiled OpenModelica model with user-defined start and stop times. It enables users to select the executable file, input simulation parameters, and ensures that the time constraints adhere to the condition: **0 ≤ start time < stop time < 5**. The tool streamlines the simulation process by automating execution while enhancing user experience through validation and error handling.  

### **Project Overview**  
The project consists of two main tasks:  
1. **Model Compilation** – Using OpenModelica to compile the "TwoConnectedTanks" model and generate an executable program along with its required dependencies.  
2. **GUI Application Development** – Creating a Python-based graphical user interface (GUI) to run the generated executable with specified parameters.  

### **Implementation Steps**  
1. Install **OpenModelica** on a Windows 10/11 system.  
2. Download the model package and load all models into **OMEdit**, which is bundled with OpenModelica.  
3. Compile the **"TwoConnectedTanks"** model to generate an executable and its necessary dependencies.  
4. Gather the executable and its dependent files (not all are uploaded due to size constraints).  
5. Develop a Python GUI application with the following features:  
   - **Three input fields**:  
     - **Executable Path**: Allows selection of the compiled OpenModelica executable.  
     - **Start Time**: Numeric input for the simulation's start time.  
     - **Stop Time**: Numeric input for the simulation's stop time.  
   - A **Browse** button for selecting the executable file.  
   - A **Run** button to launch the executable with the specified start and stop times.  
6. Implement argument passing to the executable using OpenModelica’s simulation flags (Refer to: [OpenModelica User Guide](https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/simulationflags.html#simflag-override)).  
7. Ensure input validation, enforcing the constraint: **0 ≤ start time < stop time < 5**.  

### **Technologies Used**  
- **Python 3.6+**  
- **PyQt6**  
- **OpenModelica**  
- **Windows 10/11**  

### **Application Features**  
#### **Graphical User Interface (GUI)**  
- Input fields for selecting the executable, start time, and stop time.  
- A file browser for easy executable selection.  
- A button to execute the model simulation.  

#### **Validation & Error Handling**  
- Ensures valid numeric input and adheres to **0 ≤ start time < stop time < 5**.  
- Checks for a valid file path and prevents execution if inputs are incorrect.  
- Displays user-friendly error messages for invalid selections.  

#### **Object-Oriented Design (OOP)**  
- Encapsulates logic within a **ModelLauncherApp** class.  
- Implements modular methods for clarity and maintainability.  

#### **Code Quality**  
- Follows **PEP8** standards for readability and organization.  

### **How to Run the Application**  
1. Install **PyQt6**:  
   ```sh
   pip install PyQt6
   ```  
2. Save the script as **ModelLauncher.py**.  
3. Run the script:  
   ```sh
   python ModelLauncher.py
   ```  

### **Usage Instructions**  
1. Click **Browse** to select the compiled OpenModelica executable.  
2. Enter valid **start** and **stop** times.  
3. Click **Run** to execute the simulation with the specified parameters.  
