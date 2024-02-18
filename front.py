import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
# from funcion import * # importando todas funções
from objects import Table, TopLevelWindow #objetos como tabela e items
from funcion import create_excel


ctk.set_appearance_mode("dark")



ctk.set_default_color_theme("green")

class MainWindow(ctk.CTk):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        

       
        

        self.title("Custom Tkinter App")
        self.geometry("800x600")

        # Configure color palette

        # Configure dark blue theme

        
        self.create_sidebar()
        self.create_main_section()
        self.toplevel_window = None
        



    def create_sidebar(self):
        self.sidebar = ctk.CTkFrame(self.master, width=200)
        self.sidebar.pack(side="left", fill="y")

        profile_photo = ctk.CTkLabel(self.sidebar, text="Profile Photo",)
        profile_photo.pack(pady=20)

        section1_button = ctk.CTkButton(self.sidebar, text="Section 1",command= lambda:create_excel())
        section1_button.pack(pady=5, padx=10, fill="x")

        section2_button = ctk.CTkButton(self.sidebar, text="Section 2",  )
        section2_button.pack(pady=5, padx=10, fill="x")

    def create_main_section(self):
        self.main_section = ctk.CTkFrame(self.master,)
        self.main_section.pack(expand=True, fill="both", padx=20, pady=20)

        title_label = ctk.CTkLabel(self.main_section, text="Gerenciador de orçamentos", font=("Arial", 20))
        title_label.pack(pady=10)

        table_frame = ctk.CTkFrame(self.main_section)
        table_frame.pack(expand=True, fill="both", padx=10, pady=10)
        self.table = Table(table_frame)

        button_frame = ctk.CTkFrame(self.master,)
        button_frame.pack(side="bottom", anchor="se", padx=20, pady=20)


        self.button = ctk.CTkButton(self, text="Novo item",command=self.open_topLevel)
        self.button.pack(pady=5)
    def open_topLevel(self):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = TopLevelWindow(self,self.table)
            else:
                self.toplevel_window.focus()
        
    

def main():

    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
