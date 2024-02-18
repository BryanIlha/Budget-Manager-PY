from tkinter import ttk
import customtkinter as ctk
from funcion import new_item, add_to_table


class Table():
    def __init__(self, parent):
        columns = ('Nome', 'Unidade', 'Quantidade', 'Valor Unitario', 'Valor Total')
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
    def __init__(self, master,table_instance,*args, **kwargs):
        super().__init__(master,*args, **kwargs)
        self.title("New Window")
        self.resizable(False, False)


        self.table_instance = table_instance


        labels = ["Nome", "Unidade", "Quantidade", "Valor Unitário", "Valor Total"]
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

        add_button = ctk.CTkButton(self, text="Adicionar",command=lambda: self.get_entry_vals()) 
        add_button.grid(row=len(labels)+1, columnspan=2, pady=10,)


    def get_entry_vals(self): #função para pegar os valores da entry e jogar em um objeto
        nome, uni, quant, uni_val, total_val  = [entry.get() for entry in self.entries]
        
   

        if self.switch_var.get()=="on":
            try:
                total_val = int(quant) * int(uni_val)
                
            except:
                print('deu ruim')#adicionar messagebox BRUNO
       
            

        item_carat =nome, uni, quant, uni_val, total_val
        
        new_item(Item,item_carat,self.table_instance) #criando um objeto com os valores obtido
        self.destroy()
    
    def destroy(self):
        super().destroy()

    def switch_event(self):
        if self.switch_var.get() == "on":
            self.entries[-1].grid_remove()  # Remove a entrada de Valor Total
            
            
        else:
            self.entries[-1].grid()  # Reexibe a entrada de Valor Total
            

  