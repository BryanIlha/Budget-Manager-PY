from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import pandas as pd



def create_table(self):
    # Criando o arquivo PDF
    lista_formatada=[]
    doc = SimpleDocTemplate("table.pdf", pagesize=letter)
    colunas = ['Nome', 'Unidade', 'Quantidade', 'Valor Unitario', 'Valor Total']
    service_name = self.option_serv.get()

    # Obtém a lista de objetos correspondente ao serviço selecionado
    service_list = self.dict_serv.get(service_name, [])

    for obj in service_list:
        lista_formatada.append((obj.nome,obj.unidade,obj.quantidade,obj.valor_uni,obj.valor_total))
        
    print(lista_formatada)

   

    # Criando o DataFrame
    data = pd.DataFrame(lista_formatada, columns=colunas)

    print(data)

    # Criando a tabela
    table_data = [colunas] + lista_formatada  # Adicionando o cabeçalho das colunas
    table = Table(table_data)

    # Estilo da tabela
    style = TableStyle([('BACKGROUND', (0,0), (-1,0), colors.grey),
                        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
                        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0,0), (-1,0), 12),
                        ('BACKGROUND', (0,1), (-1,-1), colors.beige),
                        ('GRID', (0,0), (-1,-1), 1, colors.black)])

    # Aplicando o estilo à tabela
    table.setStyle(style)
    doc.build([table])