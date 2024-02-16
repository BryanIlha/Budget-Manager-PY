import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from funcion import * # importando todas funções
from objects import Table, Item #objetos como tabela e items 


ctk.set_appearance_mode("dark")        
 


ctk.set_default_color_theme("green")    

class CustomTkinterApp(ctk.CTk):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Custom Tkinter App")
        self.geometry("800x600")

        # Configure color palette
     
        # Configure dark blue theme


        self.create_sidebar()
        self.create_main_section()

    def create_sidebar(self):
        self.sidebar = ctk.CTkFrame(self.master, width=200)
        self.sidebar.pack(side="left", fill="y")

        profile_photo = ctk.CTkLabel(self.sidebar, text="Profile Photo",)
        profile_photo.pack(pady=20)

        section1_button = ctk.CTkButton(self.sidebar, text="Section 1", )
        section1_button.pack(pady=5, padx=10, fill="x")

        section2_button = ctk.CTkButton(self.sidebar, text="Section 2",  )
        section2_button.pack(pady=5, padx=10, fill="x")

    def create_main_section(self):
        self.main_section = ctk.CTkFrame(self.master,)
        self.main_section.pack(expand=True, fill="both", padx=20, pady=20)

        title_label = ctk.CTkLabel(self.main_section, text="Gerenciador de orçamentos", font=("Arial", 20))
        title_label.pack(pady=10)

        table_frame = ctk.CTkFrame(self.main_section,)
        table_frame.pack(expand=True, fill="both", padx=10, pady=10)
        self.table = Table(table_frame)
        # self.treeview = ttk.Treeview(table_frame, columns=("Unidade", "Quantidade", "Nome", "Valor Unitário", "Valor Total"), show="headings", selectmode="browse")
        # self.treeview.pack(expand=True, fill="both")

        # self.treeview.heading("Unidade", text="Unidade")
        # self.treeview.heading("Quantidade", text="Quantidade")
        # self.treeview.heading("Nome", text="Nome")
        # self.treeview.heading("Valor Unitário", text="Valor Unitário")
        # self.treeview.heading("Valor Total", text="Valor Total")

        # self.treeview.column("Unidade", width=100)
        # self.treeview.column("Quantidade", width=100)
        # self.treeview.column("Nome", width=200)
        # self.treeview.column("Valor Unitário", width=150)
        # self.treeview.column("Valor Total", width=150)

        button_frame = ctk.CTkFrame(self.master,)
        button_frame.pack(side="bottom", anchor="se", padx=20, pady=20)

        self.button = ctk.CTkButton(button_frame, text="Open New Window", command=self.open_new_window, )
        self.button.pack(pady=5)

    def open_new_window(self):
        new_window = tk.Toplevel(self.master)
        new_window.title("New Window")
        new_window.configure(bg=self.bg_color)

        labels = ["Unidade", "Quantidade", "Nome", "Valor Unitário", "Valor Total"]
        entries = []

        for i, label_text in enumerate(labels):
            label = ctk.CTkLabel(new_window, text=label_text + ":",)
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")

            entry = ctk.CTkEntry(new_window, bg="white", fg="black", bd=0)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
            entries.append(entry)

        def calculate_total():
            try:
                quantidade = float(entries[1].get())
                valor_unitario = float(entries[3].get())
                valor_total = quantidade * valor_unitario
                entries[4].delete(0, tk.END)
                entries[4].insert(tk.END, valor_total)
            except ValueError:
                pass

        calculate_button = ctk.CTkButton(new_window, text="Calcular", command=calculate_total, )
        calculate_button.grid(row=len(labels), columnspan=2, pady=10)

        def add_to_list():
            item_values = [entry.get() for entry in entries]
            self.treeview.insert("", "end", values=item_values)

        add_button = ctk.CTkButton(new_window, text="Adicionar", command=add_to_list, )
        add_button.grid(row=len(labels)+1, columnspan=2, pady=10)

def main():
   
    app = CustomTkinterApp()
    app.mainloop()

if __name__ == "__main__":
    main()
