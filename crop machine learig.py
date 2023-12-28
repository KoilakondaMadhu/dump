# Import necessary libraries
import tkinter as tk
from tkinter import messagebox
import requests
import json

# Function to get crop recommendations based on input parameters
def get_crop_recommendation(state, district, month):
    # Your logic to fetch crop recommendations from your dataset or API
    # Replace the following line with your actual implementation
    recommended_crops = ["Wheat", "Rice", "Maize"]

    return recommended_crops

# Function to handle button click event
def on_predict_click():
    # Get input values from the user
    state = state_entry.get()
    district = district_entry.get()
    month = month_entry.get()

    try:
        # Validate input (add your own validation logic)
        if not state or not district or not month:
            raise ValueError("Please provide all input parameters.")

        # Get crop recommendations
        crops = get_crop_recommendation(state, district, month)

        # Display the recommendations
        result_text.set(f"Recommended Crops: {', '.join(crops)}")

    except Exception as e:
        # Display an error message if something goes wrong
        messagebox.showerror("Error", str(e))

# Create the main application window
app = tk.Tk()
app.title("Crop Recommendation System")

# Create and place widgets
state_label = tk.Label(app, text="State:")
state_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

state_entry = tk.Entry(app)
state_entry.grid(row=0, column=1, padx=10, pady=10)

district_label = tk.Label(app, text="District:")
district_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

district_entry = tk.Entry(app)
district_entry.grid(row=1, column=1, padx=10, pady=10)

month_label = tk.Label(app, text="Month:")
month_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

month_entry = tk.Entry(app)
month_entry.grid(row=2, column=1, padx=10, pady=10)

predict_button = tk.Button(app, text="Predict Crop", command=on_predict_click)
predict_button.grid(row=3, column=0, columnspan=2, pady=10)

result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the main event loop
app.mainloop()
