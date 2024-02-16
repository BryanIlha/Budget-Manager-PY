from tkinter import ttk
import customtkinter as ctk

class Table():
    def __init__(self, parent):
        columns = ('Unidade', 'Quantidade', 'Nome', 'Valor Unitario', 'Valor Total')
        self.treeview = ttk.Treeview(parent, columns=columns, show='headings')
        self.treeview.pack(expand=True, fill="both")

        for col in columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=20)

class Item: #objeto referente aos itens do orçamento
    def __init__(self, nome, unidade, quantidade,
                  valor_uni, switch_total):
        self.nome = nome
        self.unidade = unidade
        self.quantidade = quantidade
        self.valor_uni = valor_uni
        if switch_total == 'ON':
            self.valor_total = quantidade * valor_uni
        else:
            self.valor_total = switch_total


class TopLevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        new_window.title("New Window")

        labels = ["Unidade", "Quantidade", "Nome", "Valor Unitário", "Valor Total"]
        entries = []

        for i, label_text in enumerate(labels):
            label = ctk.CTkLabel(new_window, text=label_text + ":",)
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")

            entry = ctk.CTkEntry(new_window)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
            entries.append(entry)

        add_button = ctk.CTkButton(new_window, text="Adicionar" )
        add_button.grid(row=len(labels)+1, columnspan=2, pady=10)

