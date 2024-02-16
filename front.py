import tkinter as tk
from tkinter import ttk

class CustomTkinterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Custom Tkinter App")
        self.master.geometry("800x600")

        # Configure color palette
        self.bg_color = "#084B83"
        self.text_color = "black"
        self.button_color = "#61988E"
        self.highlight_color = "#3f6075"
        self.active_color = "#2d475d"

        # Configure dark blue theme
        self.master.configure(bg=self.bg_color)
        self.master.option_add("*Font", "Arial 10")
        self.master.option_add("*background", self.bg_color)
        self.master.option_add("*foreground", self.text_color)
        self.master.option_add("*selectBackground", self.highlight_color)
        self.master.option_add("*selectForeground", self.text_color)

        self.create_sidebar()
        self.create_main_section()

    def create_sidebar(self):
        self.sidebar = tk.Frame(self.master, bg=self.bg_color, width=200)
        self.sidebar.pack(side="left", fill="y")

        profile_photo = tk.Label(self.sidebar, text="Profile Photo", bg=self.bg_color, fg=self.text_color)
        profile_photo.pack(pady=20)

        section1_button = tk.Button(self.sidebar, text="Section 1", bg=self.button_color, fg=self.text_color, relief="flat", activebackground=self.active_color)
        section1_button.pack(pady=5, padx=10, fill="x")

        section2_button = tk.Button(self.sidebar, text="Section 2", bg=self.button_color, fg=self.text_color, relief="flat", activebackground=self.active_color)
        section2_button.pack(pady=5, padx=10, fill="x")

    def create_main_section(self):
        self.main_section = tk.Frame(self.master, bg=self.bg_color)
        self.main_section.pack(expand=True, fill="both", padx=20, pady=20)

        title_label = tk.Label(self.main_section, text="Gerenciador de orçamentos", bg=self.bg_color, fg=self.text_color, font=("Arial", 20))
        title_label.pack(pady=10)

        table_frame = tk.Frame(self.main_section, bg=self.bg_color)
        table_frame.pack(expand=True, fill="both", padx=10, pady=10)

        self.treeview = ttk.Treeview(table_frame, columns=("Unidade", "Quantidade", "Nome", "Valor Unitário", "Valor Total"), show="headings", selectmode="browse")
        self.treeview.pack(expand=True, fill="both")

        self.treeview.heading("Unidade", text="Unidade")
        self.treeview.heading("Quantidade", text="Quantidade")
        self.treeview.heading("Nome", text="Nome")
        self.treeview.heading("Valor Unitário", text="Valor Unitário")
        self.treeview.heading("Valor Total", text="Valor Total")

        self.treeview.column("Unidade", width=100)
        self.treeview.column("Quantidade", width=100)
        self.treeview.column("Nome", width=200)
        self.treeview.column("Valor Unitário", width=150)
        self.treeview.column("Valor Total", width=150)

        button_frame = tk.Frame(self.master, bg=self.bg_color)
        button_frame.pack(side="bottom", anchor="se", padx=20, pady=20)

        self.button = tk.Button(button_frame, text="Open New Window", command=self.open_new_window, bg=self.button_color, fg=self.text_color, relief="flat", activebackground=self.active_color)
        self.button.pack(pady=5)

    def open_new_window(self):
        new_window = tk.Toplevel(self.master)
        new_window.title("New Window")
        new_window.configure(bg=self.bg_color)

        labels = ["Unidade", "Quantidade", "Nome", "Valor Unitário", "Valor Total"]
        entries = []

        for i, label_text in enumerate(labels):
            label = tk.Label(new_window, text=label_text + ":", bg=self.bg_color, fg=self.text_color)
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")

            entry = tk.Entry(new_window, bg="white", fg="black", bd=0)
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

        calculate_button = tk.Button(new_window, text="Calcular", command=calculate_total, bg=self.button_color, fg=self.text_color, relief="flat", activebackground=self.active_color)
        calculate_button.grid(row=len(labels), columnspan=2, pady=10)

        def add_to_list():
            item_values = [entry.get() for entry in entries]
            self.treeview.insert("", "end", values=item_values)

        add_button = tk.Button(new_window, text="Adicionar", command=add_to_list, bg=self.button_color, fg=self.text_color, relief="flat", activebackground=self.active_color)
        add_button.grid(row=len(labels)+1, columnspan=2, pady=10)

def main():
    root = tk.Tk()
    app = CustomTkinterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
