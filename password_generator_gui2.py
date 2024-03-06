from tkinter import *
from random import randint

root = Tk()
root.title('Strong Password Generator')
#root.iconbitmap('file_path.ico')
root.geometry("500x300")

my_password = chr(randint(33,126))

# Generate Random Strong Password
def new_rand():
    # Clear entry box
    pw_entry.delete(0, END)

    # Get PW length and convert to integer
    pw_length = int(my_entry.get())

    # Create a variable to hold our password
    my_password = ''

    # Loop through password length
    for x in range(pw_length):
        my_password += chr(randint(33,126))

    # Output password to the screen
    pw_entry.insert(0, my_password)

# Copy to Clipboard
def clipper():
    # Clear the clipboard
    root.clipboard_clear()
    # Copy to clipboard
    root.clipboard_append(pw_entry.get())

# Label Frame
lf = LabelFrame(root, text="How Many Characters?")
lf.pack(pady=20)

# Create Entry Box To Designate Number of Characters
my_entry = Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

# Create Enrty Box For Our Returned Password
pw_entry = Entry(root, text='', font=("Helvetica", 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

# Create A Frame For Our Buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create Our Buttons
my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy To Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)
root.mainloop()