import openpyxl

# Carregando o arquivo Excel existente
workbook = openpyxl.load_workbook("base.xlsx")

# Selecionando a planilha desejada (por padrão, será a primeira planilha)
sheet = workbook.active

linha_atual = 78



def definir_cliente(nome_cliente): # input na window principal
    sheet[f"B{str(8)}"] = nome_cliente
    
    

def adicionar_item(unidade,quantidade,
                   nome,valor_uni,valor_total,linha_atual): # receber variavel do botão de adicionar no top level
    
    linha_atual += 1
    
    sheet[f"A{str(linha_atual)}"] = unidade
    sheet[f"B{str(linha_atual)}"] = quantidade
    sheet[f"C{str(linha_atual)}"] = nome
    sheet[f"E{str(linha_atual)}"] = valor_uni
    sheet[f"G{str(linha_atual)}"] = valor_total
    


def definir_data(date): #tk calender
    pass



# nome= input("DIGA SEU NOME")

# definir_cliente(nome)
workbook.save("base.xlsx")

