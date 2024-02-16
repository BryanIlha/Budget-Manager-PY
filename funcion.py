from objects import Item



# lista= [1,2,3,4,'ON']


def turn_into_int(quantidade,valor_uni):
    try:
            int_quant = int(quantidade)
            int_valor_uni = int(valor_uni)
            return int_quant, int_valor_uni
    except:
            print("Não foi possivel transformar em numero")
            
def new_item(list_values):


    # Unpack the list_values into individual arguments
    nome, unidade, quantidade, valor_uni, switch_total = list_values
    if switch_total is not "blue":
            pass
    # Instantiate the Item object
    item = Item(nome, unidade, quantidade, valor_uni, switch_total)

    # Now you can access its attributes
    values = (item.unidade, item.quantidade, item.nome, item.valor_uni, item.valor_total)
    print(values)
            
# new_item(lista)


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
