
import xlwings as xw
from customtkinter import CTkInputDialog
import customtkinter as ctk


items_list = []
index_counter = 0




def init_excel():
    try:
        # Abrir um arquivo Excel existente
            wb = xw.Book("base.xlsx")
            # Ativar a planilha desejada
            sheet = wb.sheets.active
        
            return sheet
        
    except Exception as e:
        print("Não conseguiu abrir o arquivo Excel:", e)

            
def new_item(self,Item):


    # Unpack the list_values into individual arguments
    

    # Instantiate the Item object
    item = Item(self.nome, self.unidade, self.quantidade, self.valor_uni, self.valor_total)
    items_list.append(item) #parte mega importante para ter uma lista dos objetos
    add_to_table(item,self.table_instance)

def new_service(self): #nome dos serviços so para aparecer no option menu
        
        service_name = inputbox("Novo Serviço",("Digite o nome do Serviço")) # o service é um array do objeto item
        
        self.dict_serv[service_name] = []

        if len(self.dict_serv)!=1: #BAIANO
                    #sempre que for da update pegar index e lens

            self.option_serv.configure(values=self.dict_serv)

            
            dict_keys = list(self.dict_serv.keys())# argumentos do update
            current_index = dict_keys.index(self.option_serv.get())# argumentos do update

            self.update_service(current_index,dict_keys)
        else:
             print('botar modal aqui para falar que so tem um')
            
def delete_service(self):
        #sempre que for da update pegar index e lens
        dict_keys = list(self.dict_serv.keys())
        current_index = dict_keys.index(self.option_serv.get())
        
        if len(self.dict_serv) ==1:
            print("nao da dog so tem um") #MODAL
        else:    
            service_to_dlt= self.option_serv.get()
            del self.dict_serv[service_to_dlt]
            self.update_service(current_index,dict_keys) #dar update
            print('apaguei o ',service_to_dlt) #MODAL




def add_to_table(item, table_instance): #use the item object into the table
    
    values = (item.nome, item.unidade, item.quantidade, item.valor_uni, item.valor_total)
    table_instance.treeview.insert('', 'end', values=values)

def create_excel():

    sheet= init_excel()
    linha_atual = 8
    
    for obj in items_list: 
                
            sheet.range(f"A{str(linha_atual)}").value = obj.unidade
            sheet.range(f"B{str(linha_atual)}").value = obj.quantidade
            sheet.range(f"C{str(linha_atual)}").value = obj.nome
            sheet.range(f"E{str(linha_atual)}").value = obj.valor_uni
            sheet.range(f"G{str(linha_atual)}").value = obj.valor_total
            linha_atual += 1
    sheet.book.save()
    sheet.book.close()

def inputbox(title,text):
    dialog = ctk.CTkInputDialog(text=text, title=title)
    
    return dialog.get_input()