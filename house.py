#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import tkinter as tk
from tkinter import ttk

# Load your dataset into a DataFrame
data = pd.read_csv("C:\\Users\\tusha\\Documents\\House Price Kolkata.csv")   # Replace with your dataset file path

# Define the features and target variable
features = [
    'Area', 'Location', 'Resale', 'MaintenanceStaff',
    'ATM', '24X7Security', 'PowerBackup',
    'CarParking','Hospital']

target = 'Price'  # Replace with the actual target column name

# Encode categorical features using Label Encoding
label_encoder = LabelEncoder()
data['Location'] = label_encoder.fit_transform(data['Location'])

# Create and train a Linear Regression model
X = data[features]
y = data[target]
model = LinearRegression()
model.fit(X, y)

# Function to make predictions
def predict_price():
    area = area_entry.get()
    
    # Validate if location is selected
    location = location_var.get()
    if not location:
        result_label.config(text="Please select a location.")
        return
    
    resale = resale_var.get()  
    maintenance = maintenance_var.get()     
    atm = atm_var.get()  
    security = security_var.get()  
    powerbackup = powerbackup_var.get()  
    carparking = carparking_var.get() 
    hospital = hospital_var.get() 
    
    new_data = {
                'Area': area,
                'Location': label_encoder.transform([location])[0],
                'Resale': resale,
                'MaintenanceStaff': maintenance,
                'ATM': atm,
                '24X7Security': security,
                'PowerBackup': powerbackup,
                'CarParking': carparking,
                'Hospital': hospital
    }
        
    predicted_price = model.predict(pd.DataFrame([new_data]))
    
    if predicted_price <= 0:
        result_label.config(text="Not Fond", font=("Helvetica", 16))
    else:
        rounded_price = round(float(predicted_price))
        result_label.config(text=f"Predicted Price: {rounded_price}", font=("Helvetica", 16))

location = [
    "Action Area III",
    "Airport",
    "Alipore",
    "Anil Maitra Road",
    "Ariadaha",
    "Atabagan",
    "Bablatala",
    "Bagmari",
    "Ballygunge Place East",
    "Bansdroni",
    "Bansdroni Metro Station Road",
    "Baranagar",
    "Barsundara",
    "Behala",
    "Belgharia",
    "Belghoria Expressway",
    "Belda",
    "Beniapukur",
    "Bhadreswar",
    "Bhawanipur",
    "Bidhannagar",
    "Biren Roy Road",
    "Birati",
    "Bonhooghly on BT Road",
    "Bramhapur",
    "Brahmapur Road",
    "Bramhapur",
    "Bramhapur",
    "Bramhapur",
    "Bramhapur",
    "Cossipore",
    "Dakhuria Station Road",
    "Dakshineswar",
    "Diamond Park",
    "Dum Dum",
    "Dum Dum",
    "Dum Dum Cantonment Kolkata",
    "Dumdum Italgacha",
    "Durganagar",
    "Elgin",
    "Entally",
    "Garia",
    "Garia",
    "Gariahat",
    "Habra",
    "Hatpara",
    "Haltu",
    "Howrah",
    "Howrah",
    "Howrah Railway Station",
    "International Airport",
    "Jadavpur",
    "Jatragachi Flyover",
    "Jessore Road",
    "Joginder Garden Lane",
    "Kabardanga",
    "Kaikhali",
    "Kakipur",
    "Kamarhati on BT Road",
    "Kamduni",
    "Kamardanga",
    "Kamardanga",
    "Kankurgachi",
    "Kankurgachi",
    "Kasba",
    "Kasba",
    "Kashipur",
    "Keshtopur",
    "Keshtopur",
    "Kestopur",
    "Khoyrasol",
    "Krishnagar",
    "Krishnanagar",
    "Kustia",
    "Lake Gardens",
    "Lake Town",
    "Lake Town",
    "Madhyamgram",
    "Madurdaha",
    "Madurdaha Hussainpur",
    "Mahamayatala",
    "Maheshtala",
    "Maniktala",
    "Mukundapur",
    "Mukundapur",
    "N S C Bose Road",
    "N S C Bose Road",
    "Nadia",
    "Naktala",
    "Naktala Road",
    "Narendrapur",
    "Narendrapur",
    "Narendrapur",
    "Netaji Nagar",
    "Netaji Nagar",
    "New Alipore",
    "New Alipore",
    "New Town",
    "New Town",
    "New Town",
    "New Town Action Area I",
    "New Town Action Area II",
    "Paikpara",
    "Park Circus Road",
    "Patuli",
    "Patuli",
    "Phool Bagan",
    "Phulia",
    "Picnic Garden",
    "Prince Anwar Shah Connector",
    "Prince Anwar Shah Rd",
    "Purbalok",
    "Raiganj",
    "Raja Ram Mohan Roy Road",
    "Rajbari",
    "Rajpur",
    "Rajpur Sonarpur",
    "Rajpur Sonarpur",
    "Ramchandrapur",
    "Ramchandrapur",
    "Regent Park",
    "Ropebag",
    "Ropebag",
    "Santoshpur",
    "Santoshpur",
    "Salt Lake City",
    "Sarbah",
    "Sector II Salt Lake",
    "Shankarpur",
    "Shibpur",
    "Shyamnagar",
    "Shyamnagar",
    "Simurali",
    "Sodepur",
    "Sodepur",
    "Sodepur",
    "Sonarpur",
    "Sonarpur",
    "South Dumdum",
    "Tagore Park",
    "Tagore Park",
    "Taki",
    "Tangra",
    "Tangra",
    "Taratala",
    "Taratala",
    "Thakurpukur",
    "Tollygunge",
    "Tollygunge",
    "Topsia",
    "Uttar Panchanna Gram",
    "Uttarpara",
    "Uttarpara",
    "Uttarpara Kotrung",
    "Uttarpara Kotrung",
    "Ultadanga",
    "Ultadanga",
    "Wood Street"
]

    
# Create a Tkinter window
window = tk.Tk()
window.title("House Price Prediction")

# Create a Canvas widget to hold the content
canvas = tk.Canvas(window)
canvas.pack(side="left", fill="both", expand=True)

# Create a Vertical Scrollbar and attach it to the Canvas
vertical_scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
vertical_scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=vertical_scrollbar.set)

# Create a frame to hold your content (input fields, labels, etc.)
content_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Add your input fields and labels to the content frame

label = tk.Label(content_frame, text="House Features:")
label.pack()

area_label = tk.Label(content_frame, text="Area (sq. ft):")
area_label.pack()
area_entry = tk.Entry(content_frame)
area_entry.pack()

# Replace location_combobox with encoded values
location_label = tk.Label(content_frame, text="Location:")
location_label.pack()
location_var = tk.StringVar()
location_combobox = ttk.Combobox(content_frame, textvariable=location_var, values=location)
location_combobox.pack()

resale_label = tk.Label(content_frame, text="Resale (Yes or No):")
resale_label.pack()
resale_var = tk.IntVar()
resale_checkbox = tk.Checkbutton(content_frame, variable=resale_var)
resale_checkbox.pack()

# Add more input fields and labels for other features

maintenance_label = tk.Label(content_frame, text="Maintenance Staff (Yes or No):")
maintenance_label.pack()
maintenance_var = tk.IntVar()
maintenance_checkbox = tk.Checkbutton(content_frame, variable=maintenance_var)
maintenance_checkbox.pack()

atm_label = tk.Label(content_frame, text="ATM (Yes or No):")
atm_label.pack()
atm_var = tk.IntVar()
atm_checkbox = tk.Checkbutton(content_frame, variable=atm_var)
atm_checkbox.pack()

security_label = tk.Label(content_frame, text="24X7 Security (Yes or No):")
security_label.pack()
security_var = tk.IntVar()
security_checkbox = tk.Checkbutton(content_frame, variable=security_var)
security_checkbox.pack()

powerbackup_label = tk.Label(content_frame, text="Power Backup (Yes or No):")
powerbackup_label.pack()
powerbackup_var = tk.IntVar()
powerbackup_checkbox = tk.Checkbutton(content_frame, variable=powerbackup_var)
powerbackup_checkbox.pack()

carparking_label = tk.Label(content_frame, text="Car Parking (Yes or No):")
carparking_label.pack()
carparking_var = tk.IntVar()
carparking_checkbox = tk.Checkbutton(content_frame, variable=carparking_var)
carparking_checkbox.pack()

hospital_label = tk.Label(content_frame, text="Hospital (Yes or No):")
hospital_label.pack()
hospital_var = tk.IntVar()
hospital_checkbox = tk.Checkbutton(content_frame, variable=hospital_var)
hospital_checkbox.pack()

result_label = tk.Label(content_frame, text="")
result_label.pack()

# Create prediction button
predict_button = tk.Button(content_frame, text="Predict Price", command=predict_price)
predict_button.pack()

# Function to make predictions
def predict_price():
    # Replace this with your prediction logic
    result_label.config(text="Predicted Price: $100,000", font=("Helvetica, 16"))
    
# Configure the canvas to update its scrolling region when the content frame changes
content_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))


window.mainloop()


# In[1]:


pip install nbconvert


# In[3]:


jupyter nbconvert --to script your_notebook.ipynb


# In[ ]:





# In[ ]:





# In[ ]:




