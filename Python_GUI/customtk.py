import customtkinter as tk

# Create a tkinter window
root = tk.CTk()
root.title("Medicine Input")

# Create a customtkinter Entry widget for medicine input
medicine_entry = tk.CTkEntry(root)
medicine_entry.pack()

# Function to store the medicine name
def store_medicine():
    medicine_name = medicine_entry.get()
    if medicine_name:
        # You can store the medicine name in a database, file, or any other data structure.
        # For example, you can append it to a list.
        with open("medicine_list.txt", "a") as file:
            file.write(medicine_name + "\n")
        # Optionally, clear the input field after storing the medicine name.
        medicine_entry.delete(0, tk.END)
    else:
        print("Please enter a valid medicine name.")

# Create a button to trigger the storage
store_button = tk.CTkButton(root, text="Store Medicine", command=store_medicine)
store_button.pack()

root.mainloop()
