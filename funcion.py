

import openpyxl
# workbook = openpyxl.load_workbook("base.xlsx")
# sheet = workbook.active

items_list = []
index_counter = 0








            
def new_item(Item,list_values,table_instance):


    # Unpack the list_values into individual arguments
    nome, unidade, quantidade, valor_uni, valor_total = list_values

    # Instantiate the Item object
    item = Item(nome, unidade, quantidade, valor_uni, valor_total)
    items_list.append(item) #parte mega importante para ter uma lista dos objetos
    add_to_table(item,table_instance)







def add_to_table(item, table): #use the item object into the table
    
    values = (item.unidade, item.quantidade, item.nome, item.valor_uni, item.valor_total)
    table.treeview.insert('', 'end', values=values)

# def add_to_excel(self,unidade,quantidade,
#                    nome,valor_uni,valor_total,linha_atual): # receber variavel do botão de adicionar no top level
    
#                 self.linha_atual += 1
                
                
#                 sheet[f"A{str(linha_atual)}"] = unidade
#                 sheet[f"B{str(linha_atual)}"] = quantidade
#                 sheet[f"C{str(linha_atual)}"] = nome
#                 sheet[f"E{str(linha_atual)}"] = valor_uni
#                 sheet[f"G{str(linha_atual)}"] = valor_total


#                 workbook.save("base.xlsx") ##para salvar

# def create_excel(self):
#                itens = self.tabela.treeview.get_children()
#                for item in itens:
#                         unidade, quantidade, nome, valor_uni, valor_total = self.tabela.treeview.item(item, 'values')
#                         add_to_excel(unidade,quantidade,
#                    nome,valor_uni,valor_total,self.linha_atual)
                        
               
# def remover_item(self,index): # receber variavel do botão de adicionar no top level
    
#                 self.linha_atual -= 1
                
                


#                 workbook.save("base.xlsx") ##para salvar
