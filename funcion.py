
from CTkMessagebox import CTkMessagebox

import openpyxl
workbook = openpyxl.load_workbook("base.xlsx")
sheet = workbook.active

items_list = []
index_counter = 0








            
def new_item(object,list_values):


    # Unpack the list_values into individual arguments
    nome, unidade, quantidade, valor_uni, valor_total = list_values

    # Instantiate the Item object
    item = object(nome, unidade, quantidade, valor_uni, valor_total)
    items_list.append(item) #parte mega importante para ter uma lista dos objetos


#     values = (item.unidade, item.quantidade, item.nome, item.valor_uni, item.valor_total)
#     for value in values:
#             print(value)
            



def add_to_excel(self,unidade,quantidade,
                   nome,valor_uni,valor_total,linha_atual): # receber variavel do botão de adicionar no top level
    
                self.linha_atual += 1
                
                
                sheet[f"A{str(linha_atual)}"] = unidade
                sheet[f"B{str(linha_atual)}"] = quantidade
                sheet[f"C{str(linha_atual)}"] = nome
                sheet[f"E{str(linha_atual)}"] = valor_uni
                sheet[f"G{str(linha_atual)}"] = valor_total


                workbook.save("base.xlsx") ##para salvar

def create_excel(self):
               itens = self.tabela.treeview.get_children()
               for item in itens:
                        unidade, quantidade, nome, valor_uni, valor_total = self.tabela.treeview.item(item, 'values')
                        add_to_excel(unidade,quantidade,
                   nome,valor_uni,valor_total,self.linha_atual)
                        
               
def remover_item(self,index): # receber variavel do botão de adicionar no top level
    
                self.linha_atual -= 1
                
                


                workbook.save("base.xlsx") ##para salvar

def get_entry_vals(self): #função para pegar os valores da entry e jogar em um objeto
        nome, uni, quant, uni_val, total_val  = [entry.get() for entry in self.entries]
        
        

        if self.switch_var.get()=="on":
            try:
                total_val = int(quant) * int(uni_val)
                
            except:
                print('deu ruim')#adicionar messagebox BRUNO
       
            

        item_carat =nome, uni, quant, uni_val, total_val
        
        new_item(Item, item_carat) #criando um objeto com os valores obtido

def switch_event(self):
        if self.switch_var.get() == "on":
            self.entries[-1].grid_remove()  # Remove a entrada de Valor Total
            print('ON')
            
        else:
            self.entries[-1].grid()  # Reexibe a entrada de Valor Total
            print('OFF')


def modal_confirmação(entry):
    # get yes/no answers
    msg = CTkMessagebox(title="Adicionar item?", message="Deseja adicionar este item a lista?",
                        icon="question", option_1="Cancel", option_2="Não", option_3="Sim")
    response = msg.get()
    
    if response=="Yes":
        lambda: entry.get_entry_vals()

        app.destroy()       
    else:
        print("Click 'Yes' to exit!")
