from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd



def create_table(pdfwindow,self):

                   

    pdfwindow.destroy()
    # Criando o arquivo PDF
    lista_formatada = []
    doc = SimpleDocTemplate("table.pdf", pagesize=letter)
    colunas = ['Nome', 'Unidade', 'Quantidade', 'Valor Unitário', 'Valor Total']
    service_name = self.option_serv.get()
    print(service_name)
    client_email ="bryansalgueiro@gmail.com"  

    
    service_list = self.dict_serv.get(service_name, [])

    for obj in service_list:
        lista_formatada.append((obj.nome, obj.unidade, obj.quantidade, obj.valor_uni, obj.valor_total))

    
    data = pd.DataFrame(lista_formatada, columns=colunas)

    
    table_data = [colunas] + lista_formatada  
    table = Table(table_data)

   
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ])

    # Aplicando o estilo à tabela
    table.setStyle(style)

    # Estilo de parágrafos
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    normal_style = styles['Normal']

    # Criando os elementos para o PDF
    elements = []

    # Adicionando título
    title = Paragraph("Relatório de Serviços", title_style)
    elements.append(title)

    # Adicionando espaço
    elements.append(Spacer(1, 12))

    # Adicionando email do cliente
    email_paragraph = Paragraph(f"E-mail do Cliente: {client_email}", normal_style)
    elements.append(email_paragraph)

    # Adicionando espaço
    elements.append(Spacer(1, 12))

    # Adicionando a tabela
    elements.append(table)

    # Construindo o PDF
    doc.build(elements)

# Certifique-se de que `self.client_email.get()` retorna o e-mail do cliente.
