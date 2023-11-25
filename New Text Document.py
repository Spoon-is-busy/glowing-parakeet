import tkinter as tk
from tkinter import Label, Button
import random

# Create the main window
root = tk.Tk()
root.title("Picnic Packing Game")
root.geometry("400x300")  # Set the window size

# Create two Label elements
items_label = Label(root, text="", font=("Helvetica", 12))
items_label.place(relx=0.5, rely=0.3, anchor="center")  # Place in the center

random_number_label = Label(root, text="", font=("Helvetica", 12))
random_number_label.place(relx=0.5, rely=0.5, anchor="center")  # Place in the center

# Create a list of items
picnic_items = ["PEN", "ID CARD", "CHIPS", "WATER BOTTLE", "SANDWICH", "SUNGLASSES", "BLANKET"]

# Update the text parameter of the first label with the list
items_label["text"] = "Items to Pack:\n" + "\n".join(picnic_items)

# Function to generate a random number and update the second label
def generate_random_number():
    random_index = random.randint(0, len(picnic_items) - 1)
    random_number_label["text"] = "Random Number: " + str(random_index)

# Create a button to call the function
button = Button(root, text="Generate Random Number", command=generate_random_number, bg="lightblue", fg="black")
button.place(relx=0.5, rely=0.7, anchor="center")  # Place in the center

# Run the Tkinter event loop
root.mainloop()
