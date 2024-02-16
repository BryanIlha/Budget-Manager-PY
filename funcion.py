from main import *


def adicionar_item(self,unidade,quantidade,
                   nome,valor_uni,valor_total,linha_atual): # receber variavel do botão de adicionar no top level
    
                self.linha_atual += 1
                
                
                sheet[f"A{str(linha_atual)}"] = unidade
                sheet[f"B{str(linha_atual)}"] = quantidade
                sheet[f"C{str(linha_atual)}"] = nome
                sheet[f"E{str(linha_atual)}"] = valor_uni
                sheet[f"G{str(linha_atual)}"] = valor_total


                workbook.save("base.xlsx") ##para salvar

def gerar_excel(self):
               itens = self.tabela.treeview.get_children()
               for item in itens:
                        unidade, quantidade, nome, valor_uni, valor_total = self.tabela.treeview.item(item, 'values')
                        self.adicionar_item(unidade,quantidade,
                   nome,valor_uni,valor_total,self.linha_atual)
                        
               
def adicionar_item(self,unidade,quantidade,
                   nome,valor_uni,valor_total,linha_atual): # receber variavel do botão de adicionar no top level
    
                self.linha_atual += 1
                
                
                sheet[f"A{str(linha_atual)}"] = unidade
                sheet[f"B{str(linha_atual)}"] = quantidade
                sheet[f"C{str(linha_atual)}"] = nome
                sheet[f"E{str(linha_atual)}"] = valor_uni
                sheet[f"G{str(linha_atual)}"] = valor_total


                workbook.save("base.xlsx") ##para salvar
