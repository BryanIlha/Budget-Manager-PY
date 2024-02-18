from tkinter import ttk
import customtkinter as ctk
from funcion import *

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
                  valor_uni, valor_total):
        self.nome = nome
        self.unidade = unidade
        self.quantidade = quantidade
        self.valor_uni = valor_uni
        self.valor_total = valor_total


class TopLevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("New Window")
        self.resizable(False, False)

        labels = ["Nome", "Quantidade", "Unidade", "Valor Unitário", "Valor Total"]
        self.entries = []

        for i, label_text in enumerate(labels):
            label = ctk.CTkLabel(self, text=label_text + ":",)
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")

            entry = ctk.CTkEntry(self)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
            self.entries.append(entry)

        self.switch_var = ctk.StringVar(value="off")
        switch = ctk.CTkSwitch(self, text="Calcular Valor Total", variable=self.switch_var, command=self.switch_event,onvalue="on", offvalue="off")
        switch.grid(row=len(labels), columnspan=2, pady=10, padx=5, sticky="e")

        add_button = ctk.CTkButton(self, text="Adicionar",command=modal_confirmação(entry)) 
        add_button.grid(row=len(labels)+1, columnspan=2, pady=10,)

  