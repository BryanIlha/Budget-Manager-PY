# Import customtkinter module
import customtkinter as ctk
from tkinter import ttk
import xlwings as xw
 


ctk.set_appearance_mode("dark")        
 


ctk.set_default_color_theme("green")    
 
# Create App class

class Item: #objeto referente aos itens do orçamento
    def __init__(self, nome, unidade, quantidade, valor_uni):
        self.nome = nome
        self.unidade = unidade
        self.quantidade = quantidade
        self.valor_uni = valor_uni
        self.valor_total = quantidade * valor_uni

class Janela(ctk.CTk): #objeto referente a interface grafica

        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.linha_atual = 7

                self.title("App")    

                self.geometry("200x200")    
                columns = ('Unidade', 'Quantidade','Nome','Valor Unitario','Valor Total')
                self.tabela = ttk.Treeview(self, columns=columns, show='headings')
                self.tabela.grid(row=0, column=0,sticky='n')

                for col in columns:
                        self.tabela.heading(col, text=col)
                        self.tabela.column(col, width=20)

                self.botao_adicionar = ctk.CTkButton(self, text='RANDOM',
                                                fg_color='red', width=100, height=100,command=self.aleatorio
                                                )
                self.botao_adicionar.grid(row=8,column=0,padx=1,pady=2)

                self.botao_adicionar = ctk.CTkButton(self, text='Gerar excel',
                                                fg_color='red', width=100, height=100,command=self.gerar_excel
                                                )
                self.botao_adicionar.grid(row=9,column=0,padx=1,pady=2)



        def aleatorio(self,):
                item = Item(nome="Camiseta", unidade="peça", quantidade=2, valor_uni=25.0)
                values = (item.unidade, item.quantidade, item.nome, item.valor_uni, item.valor_total)
                self.tabela.insert('', 'end', values=values)

        def gerar_excel(self):
    # Abrir o arquivo Excel existente
            wb = xw.Book("base.xlsx")
            # Ativar a planilha desejada
            sheet = wb.sheets.active

            itens = self.tabela.get_children()
            for item in itens:
                unidade, quantidade, nome, valor_uni, valor_total = self.tabela.item(item, 'values')
                self.adicionar_item(sheet, unidade, quantidade, nome, valor_uni, valor_total, self.linha_atual)

            # Salvar as alterações no arquivo Excel
            wb.save("base.xlsx")
            # Fechar o arquivo Excel
            wb.close()
                        
               
        def adicionar_item(self,sheet,unidade,quantidade,
                   nome,valor_uni,valor_total,linha_atual): # receber variavel do botão de adicionar no top level
    
                self.linha_atual += 1
                            
                sheet.range(f"A{str(linha_atual)}").value = unidade
                sheet.range(f"B{str(linha_atual)}").value = quantidade
                sheet.range(f"C{str(linha_atual)}").value = nome
                sheet.range(f"E{str(linha_atual)}").value = valor_uni
                sheet.range(f"G{str(linha_atual)}").value = valor_total


                

                                
               


 
 
if __name__ == "__main__":
    app = Janela()
    # Runs the app
    app.mainloop()    