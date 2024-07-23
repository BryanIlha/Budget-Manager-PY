from tkinter import ttk
import tkinter as tk
import customtkinter as ctk
from funcion import new_item, add_to_table, obter_nomes_saves, get_total
from tkcalendar import Calendar, DateEntry
from pdffuncion import create_table


class Table():
    def __init__(self, parent,main):
        columns = ('Nome', 'Unidade', 'Quantidade', 'Valor Unitario', 'Valor Total')
        self.treeview = ttk.Treeview(parent, columns=columns, show='headings')
        self.treeview.pack(expand=True, fill="both")
        self.main = main
        
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


        
        self.treeview.bind("<Button-3>", self.show_context_menu)
        self.context_menu = tk.Menu(self.treeview, tearoff=0)
        self.context_menu.add_command(label="Remover", command=self.remove_item)
        for col in columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=20)
        
        # Vincula o evento de clique duplo na tabela à função 'on_double_click'
        self.treeview.bind('<Double-1>', self.on_double_click)

    def on_double_click(self, event):
        item = self.treeview.selection()
        if item:
            # Obtem o índice numérico da coluna onde o clique duplo ocorreu
            col_id = int(self.treeview.identify_column(event.x).split("#")[-1]) - 1
            row_id = self.treeview.identify_row(event.y)
            
            # Verifica se a coluna clicada é editável (por exemplo, todas as colunas são editáveis neste exemplo)
            if col_id in range(len(self.treeview["columns"])):
                self.edit_cell(item, col_id)
    def edit_cell(self, item, col_id):
        # Obtém o valor atual da célula
        current_value = self.treeview.set(item, self.treeview["columns"][col_id])

        # Obtém o nome do serviço selecionado
        service_name = self.main.option_serv.get()

        # Obtém a lista de objetos correspondente ao serviço selecionado
        service_list = self.main.dict_serv.get(service_name, [])

        # Obtém o índice da linha selecionada
        row_id = int(self.treeview.index(item))

        # Verifica se o índice da linha está dentro do intervalo da lista
        if 0 <= row_id < len(service_list):
            # Obtém o objeto correspondente à linha da tabela na lista de serviço
            obj = service_list[row_id]

            # Remove qualquer widget de edição existente na célula
            for child in self.treeview.get_children(item):
                self.treeview.delete(child)

            # Cria um widget Entry para edição
            entry = tk.Entry(self.treeview, bd=1, relief='solid')
            entry.insert(0, current_value)

            # Define os eventos para finalizar ou cancelar a edição
            def end_editing(event=None):
                new_value = entry.get()
                self.treeview.set(item, self.treeview["columns"][col_id], new_value)
                # Atualiza o atributo correspondente do objeto
                if col_id == 0:
                    obj.nome = new_value
                elif col_id == 1:
                    obj.unidade = new_value
                elif col_id == 2:
                    obj.quantidade = new_value
                elif col_id == 3:
                    obj.valor_uni = new_value
                elif col_id == 4:
                    
                    try:
                        obj.valor_total = float(new_value)
                        get_total(self.main)
                    except:
                        self.treeview.set(item, self.treeview["columns"][col_id], obj.valor_total)
                        print("valor total so pode ser numero")
                entry.destroy()

            def cancel_editing(event=None):
                entry.destroy()

            entry.bind('<Return>', end_editing)
            entry.bind('<Escape>', cancel_editing)

            # Insere o Entry na célula para edição
            cell_bbox = self.treeview.bbox(item, column=self.treeview["columns"][col_id])
            if cell_bbox:
                x, y, width, height = cell_bbox
                entry.place(x=x, y=y, width=width, height=height)
                entry.focus_set()


    def show_context_menu(self, event):
            # Seleciona o item clicado
            item = self.treeview.identify_row(event.y)
            if item:
                self.treeview.selection_set(item)
                self.context_menu.post(event.x_root, event.y_root)

    def remove_item(self):
        # Verifica se há um item selecionado
        selected_items = self.treeview.selection()
        if not selected_items:
            print("Nenhum item selecionado para remover.")
            return

        # Obtém o ID do item selecionado
        item_id = selected_items[0]
        item_values = self.treeview.item(item_id)
        item_name = item_values['values'][0]  # Supondo que o nome do item esteja na primeira posição

        service_name = self.main.option_serv.get()

        # Obtém a lista de objetos correspondente ao serviço selecionado
        service_list = self.main.dict_serv.get(service_name, [])

        # Encontra o objeto correspondente ao item selecionado na lista
        for obj in service_list:
            if str(obj.nome) == str(item_name):  # Supondo que o atributo 'nome' seja usado para identificar o objeto
                print("são iguais")
                print(str(obj.nome))
                service_list.remove(obj)  # Remove o objeto da lista
                break  # Sai do loop após remover o objeto
            else:
                print("nao sao iguais")

        # Remove o item da tabela
        self.treeview.delete(item_id)

        print("Nome do item removido:", item_name) # Add modal here
        get_total(self.main)






class Item:  # objeto referente aos itens do orçamento
    def __init__(self, nome, unidade, quantidade,
                 valor_uni, valor_total):
        self.nome = nome
        self.unidade = unidade
        self.quantidade = quantidade
        self.valor_uni = valor_uni
        self.valor_total = valor_total

    def to_dict(self):  # iterar o objeto para jogar no json depois
        return {
            'nome': self.nome,
            'unidade': self.unidade,
            'quantidade': self.quantidade,
            'valor_uni': self.valor_uni,
            'valor_total': self.valor_total
        }


class TopLevelConfirmModal(ctk.CTkToplevel):
    def __init__(self, master, title, text, button_texts):
        super().__init__(master)
        self.title(title)
        self.label = ctk.CTkLabel(self, text=text)
        self.label.pack(padx=10, pady=10)
        self.buttons = []
        for button_text in button_texts:
            button = ctk.CTkButton(self, text=button_text)
            button.pack(padx=10, pady=10)
            self.buttons.append(button)
        self.grab_set()
        

class PdfGeneratorWindow(ctk.CTkToplevel):
    def __init__(self,master,*args,**kwargs):
        super().__init__(master,*args,**kwargs)
        self.title("PDF GENERATOR")
        self.resizable(False,False)
        self.grab_set()
        labels= ["Date","Client"]
        self.entries= []
        self.switch_var= ctk.StringVar(value="on")
        self.master=master

        for i, label_text in enumerate(labels):

            label = ctk.CTkLabel(self,text=label_text + ":")
            label.grid(row=i,column=0,padx=5,pady=5,sticky="w")
            if label_text !="Date":
                entry= ctk.CTkEntry(self)
                entry.grid(row=i,column=1,padx=5,pady=5,sticky="ew")
                self.entries.append(entry)
            else:
                entry=DateEntry(self, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
                entry.grid(row=i,column=1,padx=5,pady=5,sticky="ew")
                self.entries.append(entry)
        switch = ctk.CTkSwitch(self, text="ENVIAR EMAIL?", command=self.switch_email,
        onvalue="on", offvalue="off",variable=self.switch_var)
        switch.grid(row=len(labels), columnspan=2, pady=10, padx=5, sticky="e")



        self.generate_btn= ctk.CTkButton(self,command=lambda:self.get_entries())
        self.generate_btn.grid(row=5,column=0,columnspan=2)
        self.switch_email()

    def switch_email(self):
            print(self.switch_var.get())
           
            if self.switch_var.get() == "on":
                self.email_label=ctk.CTkLabel(self,text="Email adress" + ":")
                self.email_label.grid(row=4,column=0,padx=5,pady=5,sticky="w")

                self.email_entry=ctk.CTkEntry(self)
                self.email_entry.grid(row=4,column=1,padx=5,pady=5,sticky="ew")
                self.entries.append(self.email_entry)

            else:
                self.email_label.destroy()
                self.email_entry.destroy()
    def get_entries(self):
        entries_data = [entry.get() for entry in self.entries]
        create_table(self,self.master, entries_data)
        self.destroy()
       
        

            


class TopLevelWindow(ctk.CTkToplevel):
    def __init__(self, master,table_instance,service_name,dict_serv,*args, **kwargs):
        super().__init__(master,*args, **kwargs)
        self.title("New Item")
        self.resizable(False, False)
        self.dict_serv = dict_serv
        self.service_name = service_name
        self.table_instance = table_instance
        
        labels = ["Nome", "Unidade", "Quantidade",
                  "Valor Unitário", "Valor Total"]
        
        unidades = ["unidade", "quilograma",
                     "grama", "metro", "centímetro", 
                     "milímetro", "litro", 
                     "mililitro", "hora", "minuto", "segundo"]
 
        self.entries = []

        for i, label_text in enumerate(labels):
            
                
                
            label = ctk.CTkLabel(self, text=label_text + ":",)
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
            if label_text != "Unidade":
                entry = ctk.CTkEntry(self)
                entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
                self.entries.append(entry)
            else:
                entry= ctk.CTkOptionMenu(self,values=unidades )
                entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
                self.entries.append(entry)

        self.switch_var = ctk.StringVar(value="off")
        switch = ctk.CTkSwitch(self, text="Calcular Valor Total", variable=self.switch_var,
                               command=self.switch_event, onvalue="on", offvalue="off")
        switch.grid(row=len(labels), columnspan=2, pady=10, padx=5, sticky="e")

        add_button = ctk.CTkButton(
            self, text="Adicionar", command=lambda: self.send_entry_var(master))
        add_button.grid(row=len(labels)+1, columnspan=2, pady=10,)
        self.grab_set()

        self.entries[2].bind("<KeyRelease>", self.atualizar_label)
        self.entries[3].bind("<KeyRelease>", self.atualizar_label)
    def atualizar_label(self,event=None):
        
        if self.switch_var.get() == "on":
            try:
                
                unidade= float(self.entries[2].get())
                valor_uni= float(self.entries[3].get())
                valor_total = unidade*valor_uni
                valor_formatado = f'R${valor_total:.2f}'
                
                self.labe_ltotal.configure(text=valor_formatado)
                
            except:
                self.labe_ltotal.configure(text="R$ 0,00")
                
        

    def get_entry_var(self):
        entry_values = [entry.get() for entry in self.entries]
        

        
        self.nome, self.unidade, self.quantidade, self.valor_uni, self.valor_total = entry_values
        if self.switch_var.get() == "on":

            try:
                self.valor_total = int(self.quantidade) * int(self.valor_uni)
                
                
                
            except:
                print("deu merda aqui ")
                pass

        if "" in entry_values and self.valor_total == "":
             print("Tem campo vazio") # adicionar modal aqui
             return False
        
        else:
            return True
        
    def send_entry_var(self,master):  # função para pegar os valores da entry e jogar em um objeto
        
        if self.get_entry_var() is True:

        # criando um objeto com os valores obtido
            new_item(self,master, Item, self.service_name)
            self.destroy()

    def destroy(self):
        super().destroy()

    def switch_event(self):
        
        
        if self.switch_var.get() == "on":
            self.entries[-1].grid_remove()  # Remove a entrada de Valor Total
            self.labe_ltotal= ctk.CTkLabel(self,text="0")
            self.labe_ltotal.grid(row=len(self.entries) - 1, column=1, padx=5, pady=5, sticky="ew")

            self.atualizar_label()

        else:
            self.entries[-1].grid()
            if self.labe_ltotal:
                self.labe_ltotal.destroy()




class LoadWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("250x150")

        self.label = ctk.CTkLabel(self, text="Choose The Load")
        self.label.pack(padx=20, pady=20)

        saves = obter_nomes_saves()
        if len(saves) == 0:
            print("ta vazio essa merda")
            self.destroy()

        self.load_optmenu = ctk.CTkOptionMenu(self, values=saves)
        self.load_optmenu.pack()

        self.get_load_btn = ctk.CTkButton(
            self, text='CARREGAR', command=self.get_load)
        self.get_load_btn.pack()
        self.grab_set()

    def get_load(self):
        self.choosed_load = self.load_optmenu.get()

        self.destroy()  # Destruir o TopLevel


