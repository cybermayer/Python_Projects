
import tkinter


END = "end"  # Used for positioning the cursor at the end of the entry widget
mile = 0  # Initial value for miles

#Initializing windows
window = tkinter.Tk()
window.title("Mile to Km Converter")  
window.minsize(width=300, height=200) 

# Create an entry widget for user input
entry = tkinter.Entry(width=13)
entry.insert(END, string=f"{mile}")  # Insert the initial value of mile into the entry widget
entry.place(x=150, y=50)  # Place the entry widget at a specific position

# Calculate the initial conversion from miles to kilometers
mile = float(entry.get())  
km = round((mile * 1.609), 2)  

# Create labels for miles and kilometers
label_miles = tkinter.Label(text="Miles")
label_miles.place(x=225, y=50)  

label_equal = tkinter.Label(text="is equal to")
label_equal.place(x=80, y=75) 

label_km = tkinter.Label(text="Kilometer")
label_km.place(x=225, y=75)  

# Create a label to display the conversion result
label_result = tkinter.Label(text="???")
label_result.place(x=170, y=75)  

# Define the function to calculate the conversion when the button is pressed
def calculate():
    miles = float(entry.get())  
    km = round(miles * 1.609, 2)  
    label_result.config(text=km)  

# Create a button to trigger the calculate function
button = tkinter.Button(text="Calculate", width=9, command=calculate)
button.place(x=150, y=100)  

window.mainloop()
