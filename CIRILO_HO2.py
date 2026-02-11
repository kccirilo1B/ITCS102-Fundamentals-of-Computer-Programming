import tkinter as kc

window = kc.Tk()

window.title("Krisha Camille's Profile")
window.geometry("600x600")
window.resizable(False,True)
window.configure(bg = "lavender",cursor = "arrow")

label = kc.Label(window, text = "Student Profile",font=("Shrikhand",35,"italic"),fg = "black", bg="lavender",anchor="center")
label.pack()
label = kc.Label(window, text = "Name: Krisha Camille H. Cirilo", font=("Shrikhand",20,"bold"),fg = "black", bg="lavender")
label.pack(pady=20, anchor="sw")
label = kc.Label(window, text = "Age: 19 years old", font=("Shrikhand",20,"bold"),fg = "black", bg="lavender")
label.pack(pady=20, anchor="sw")
label = kc.Label(window, text = "Course: BSIT", font=("Shrikhand",20,"bold"),fg = "black", bg="lavender")
label.pack(pady=20, anchor="sw")
label = kc.Label(window, text = "Birthday: February 9, 2007", font=("Shrikhand",20,"bold"),fg = "black", bg="lavender")
label.pack(pady=20, anchor="sw")
label = kc.Label(window, text = "Motto:", font=("Shrikhand",20,"bold"),fg = "black", bg="lavender")
label.pack(pady=20, anchor="sw")
label = kc.Label(window, text = "Hangga't may baon, babangon.", font=("shrikhand",20,"italic"),fg = "black", bg="lavender")
label.pack()
window.mainloop()
