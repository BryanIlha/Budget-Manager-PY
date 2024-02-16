import customtkinter
from CTkTable import *

root = customtkinter.CTk()

value = []

table = CTkTable(master=root, row=5, column=5, values=value)
table.pack(expand=True, fill="both", padx=20, pady=20)

root.mainloop()