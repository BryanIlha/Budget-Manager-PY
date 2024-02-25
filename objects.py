from tkinter import ttk
import customtkinter as ctk
from funcion import new_item, add_to_table , obter_nomes_saves


class Table():
    def __init__(self, parent):
        columns = ('Nome', 'Unidade', 'Quantidade', 'Valor Unitario', 'Valor Total')
        self.treeview = ttk.Treeview(parent, columns=columns, show='headings')
        self.treeview.pack(expand=True, fill="both")
        style = ttk.Style()
        style.theme_use("default")
    
        style.configure("Treeview",
                            background="#2a2d2e",
                            foreground="white",
                            rowheight=20,
                            fieldbackground="#343638",
                            bordercolor="#343638",
                            borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
    
        style.configure("Treeview.Heading",
                            background="#565b5e",
                            foreground="white",
                            relief="flat",
                            font=("Arial", 12))
        style.map("Treeview.Heading",
                      background=[('active', '#3484F0')])
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

    def to_dict(self): #iterar o objeto para jogar no json depois
        return {
            'nome': self.nome,
            'unidade': self.unidade,
            'quantidade': self.quantidade,
            'valor_uni': self.valor_uni,
            'valor_total': self.valor_total
        }



class TopLevelWindow(ctk.CTkToplevel):
    def __init__(self, master,table_instance,service_name,dict_serv,*args, **kwargs):
        super().__init__(master,*args, **kwargs)
        self.title("New Window")
        self.resizable(False, False)
        self.dict_serv= dict_serv
        self.service_name= service_name
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
        self.nome, self.unidade, self.quantidade, self.valor_uni, self.valor_total  = [entry.get() for entry in self.entries]
        
   

        if self.switch_var.get()=="on":
            try:
                self.valor_total = int(self.quantidade) * int(self.valor_uni)
                
                
            except:
                print('deu ruim')#adicionar messagebox BRUNO
       
            

        
        
        new_item(self,Item,self.service_name) #criando um objeto com os valores obtido
        self.destroy()
    
    def destroy(self):
        super().destroy()

    def switch_event(self):
        if self.switch_var.get() == "on":
            self.entries[-1].grid_remove()  # Remove a entrada de Valor Total
            
            
        else:
            self.entries[-1].grid()  # Reexibe a entrada de Valor Total
            

class LoadWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="Escolha o Save")
        self.label.pack(padx=20, pady=20)

        save = obter_nomes_saves()
        print(save)

        self.load_optmenu = ctk.CTkOptionMenu(self, values=save)
        self.load_optmenu.pack()

        self.get_load_btn= ctk.CTkButton(self,text='CARREGAR',command=self.get_load)
        self.get_load_btn.pack()


    def get_load(self):
        self.choosed_load = self.load_optmenu.get()
        
        self.destroy()  # Destruir o TopLevel
        
