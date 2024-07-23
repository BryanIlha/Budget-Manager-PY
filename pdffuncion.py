from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd

def create_table(pdfwindow, self,entries):
    date, client = entries[:2]
    email = entries[2] if len(entries) > 2 else "No Email Provided"
    # pdfwindow.destroy()
    
    # Criando o arquivo PDF
    doc = SimpleDocTemplate("table.pdf", pagesize=letter)
    colunas = ['Nome', 'Unidade', 'Quantidade', 'Valor Unitário', 'Valor Total']
    

    # Estilos de parágrafos
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    subtitle_style = styles['Heading2']
    normal_style = styles['Normal']

    # Criando os elementos para o PDF
    elements = []

    # Adicionando título principal
    title = Paragraph("Service Report", title_style)
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Adicionando email do cliente
    email_paragraph = Paragraph(f" {email}", normal_style)
    elements.append(email_paragraph)
    elements.append(Spacer(1, 12))

    # Iterando sobre cada serviço
    for service_name, service_list in self.dict_serv.items():
        # Adicionando subtítulo com o nome do serviço
        subtitle = Paragraph(f"Serviço: {service_name}", subtitle_style)
        elements.append(subtitle)
        elements.append(Spacer(1, 12))

        # Formatando a lista de serviços
        lista_formatada = [(obj.nome, obj.unidade, obj.quantidade, obj.valor_uni, obj.valor_total) for obj in service_list]

        # Criando a tabela de dados
        table_data = [colunas] + lista_formatada
        table = Table(table_data, colWidths=[doc.width/5.0]*5)  # Ajuste para a tabela ocupar toda a largura da página

        # Estilo da tabela
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
        table.setStyle(style)

        # Adicionando a tabela ao PDF
        elements.append(table)
        elements.append(Spacer(1, 24))  # Adiciona espaço entre tabelas

    # Construindo o PDF
    doc.build(elements)
