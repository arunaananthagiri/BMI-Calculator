import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

# BMI Calculation
def calculate_bmi(weight, height):
    return weight / (height ** 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# GUI Design
class BMICalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BMI Calculator")
        self.geometry("400x400")
        self.resizable(False, False)
        
        # User inputs
        self.name_label = tk.Label(self, text="Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)
        
        self.weight_label = tk.Label(self, text="Weight (kg):")
        self.weight_label.pack(pady=5)
        self.weight_entry = tk.Entry(self)
        self.weight_entry.pack(pady=5)
        
        self.height_label = tk.Label(self, text="Height (m):")
        self.height_label.pack(pady=5)
        self.height_entry = tk.Entry(self)
        self.height_entry.pack(pady=5)
        
        # Buttons
        self.calculate_button = tk.Button(self, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.pack(pady=20)
        
    
        
        # Result display
        self.result_label = tk.Label(self, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)
        
        # Data storage in memory
        self.bmi_data = {}

    def calculate_bmi(self):
        try:
            name = self.name_entry.get()
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            
            if weight <= 0 or height <= 0:
                raise ValueError("Weight and height must be positive values.")
            
            bmi = calculate_bmi(weight, height)
            category = categorize_bmi(bmi)
            
            self.result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")
            
            # Store the data in memory
            if name not in self.bmi_data:
                self.bmi_data[name] = []
            self.bmi_data[name].append((datetime.now().strftime('%Y-%m-%d %H:%M:%S'), bmi))
            
            messagebox.showinfo("Success", "BMI calculated successfully.")
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
    
    def view_history(self):
        name = self.name_entry.get()
        data = self.bmi_data.get(name, [])
        
        if not data:
            messagebox.showinfo("No Data", "No historical data found for this user.")
            return
        
        dates = [record[0] for record in data]
        bmis = [record[1] for record in data]
        
        # Plotting
        fig, ax = plt.subplots()
        ax.plot(dates, bmis, marker='o', linestyle='-')
        ax.set_xlabel("Date")
        ax.set_ylabel("BMI")
        ax.set_title(f"BMI Trend for {name}")
        ax.grid(True)
        
        # Displaying the plot in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20)

# Run the application
app = BMICalculator()
app.mainloop()
