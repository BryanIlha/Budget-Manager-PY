from tkinter import ttk



class Table():
    def __init__(self, parent):
        columns = ('Unidade', 'Quantidade', 'Nome', 'Valor Unitario', 'Valor Total')
        self.treeview = ttk.Treeview(parent, columns=columns, show='headings')
        self.treeview.pack(expand=True, fill="both")

        for col in columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=20)
