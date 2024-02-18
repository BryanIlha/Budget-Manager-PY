
import xlwings as xw

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

            
def new_item(Item,list_values,table_instance):


    # Unpack the list_values into individual arguments
    nome, unidade, quantidade, valor_uni, valor_total = list_values

    # Instantiate the Item object
    item = Item(nome, unidade, quantidade, valor_uni, valor_total)
    items_list.append(item) #parte mega importante para ter uma lista dos objetos
    add_to_table(item,table_instance)







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

