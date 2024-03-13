
from CTkMessagebox import CTkMessagebox

import xlwings as xw
from customtkinter import CTkInputDialog
import customtkinter as ctk
import objects
import json


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


def new_item(self, Item, service_name):

    # Unpack the list_values into individual arguments

    # Instantiate the Item object
    item = Item(self.nome, self.unidade, self.quantidade,
                self.valor_uni, self.valor_total)
    # parte mega importante para ter uma lista dos objetos
    self.dict_serv[self.service_name].append(item)

    add_to_table(item, self.table_instance)


def new_service(self):  # nome dos serviços so para aparecer no option menu

    # o service é um array do objeto item
    self.service_name = inputbox("Novo Serviço", ("Digite o nome do Serviço"))

    if self.service_name == "":
        print("nome vazio nao pode dog")
        new_service(self)
        return 
    if self.service_name is not None:

        self.dict_serv[self.service_name] = []

        if len(self.dict_serv) != 1:  # BAIANO
            # sempre que for da update pegar index e lens

            self.option_serv.configure(values=self.dict_serv)

            dict_keys = list(self.dict_serv.keys())  # argumentos do update
            current_index = dict_keys.index(
                self.option_serv.get())  # argumentos do update

            self.update_service(current_index, dict_keys)
        return True
    else:
        modal = objects.TopLevelConfirmModal(
            self,
            title="Aviso",
            text="A criação do serviço foi cancelada.",
            button_texts=["OK"],
        )
        modal.buttons[0].configure(command=modal.destroy)
        modal.lift()
        return False


def delete_service(self):
    # sempre que for da update pegar index e lens
    dict_keys = list(self.dict_serv.keys())
    current_index = dict_keys.index(self.option_serv.get())

    if len(self.dict_serv) == 1:
        modal = objects.TopLevelConfirmModal(
            self,
            title="Aviso",
            text="Não é possível apagar o serviço pois só existe 1.",
            button_texts=["OK"],
        )
        modal.buttons[0].configure(command=modal.destroy)
        modal.lift()
    else:
        service_to_dlt = self.option_serv.get()
        modal = objects.TopLevelConfirmModal(
            self,
            title="Apagado com sucesso!",
            text=f"O serviço {service_to_dlt} foi apagado com sucesso.",
            button_texts=["Ok"])

        del self.dict_serv[service_to_dlt]
        self.update_service(current_index, dict_keys)  # dar update
        modal.buttons[0].configure(command=modal.destroy)
        modal.lift()


def change_service(self):
    clear_table(self)

    service_name = self.option_serv.get()
    service_content = self.dict_serv[service_name]

    for item in service_content:
        add_to_table(item, self.table_instance)


def clear_table(self):
    # Limpa todos os itens existentes na tabela
    self.table_instance.treeview.delete(
        *self.table_instance.treeview.get_children())


def add_to_table(item, table_instance):  # use the item object into the table

    values = (item.nome, item.unidade, item.quantidade,
              item.valor_uni, item.valor_total)
    table_instance.treeview.insert('', 'end', values=values)


def create_excel():

    sheet = init_excel()
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


def inputbox(title, text):
    dialog = ctk.CTkInputDialog(text=text, title=title)
    user_input = dialog.get_input()

    return user_input


def servico_para_json(servico):
    return [item.to_dict() for item in servico]


def save_dict(self):
    # Solicita ao usuário que insira o nome do save
    nome_do_save = inputbox("Novo Save", "Digite o nome do save: ")

    # Verifica se o arquivo save.json está vazio
    with open('save.json', 'r') as arquivo:
        conteudo = arquivo.read()
        if conteudo.strip() == "":
            dados_existentes = {}
        else:
            dados_existentes = json.loads(conteudo)

    # Prepara os novos dados a serem salvos
    dicionario_servicos_json = {key: servico_para_json(
        value) for key, value in self.dict_serv.items()}

    # Adiciona os novos dados ao dicionário existente usando o nome do save como chave
    dados_existentes[nome_do_save] = dicionario_servicos_json

    # Salva o dicionário atualizado de volta no arquivo save.json
    with open('save.json', 'w') as arquivo:
        json.dump(dados_existentes, arquivo)


def load_dict(self, Item, Class):
    save_to_load = open_load(self, Class)
    if save_to_load is False:
        return None

    self.clean_frame(self.main_section)
    self.button_frame.destroy()

    with open('save.json', 'r') as arquivo:
        json_data = json.load(arquivo)

        # Limpa o dicionário existente
        self.dict_serv.clear()
        for save, lista_itens_json in json_data.items():
            if save in save_to_load:

                for serv_name, serv_list in lista_itens_json.items():
                    lista_itens = []

                    for item_json in serv_list:
                        item = Item(
                            nome=item_json['nome'],
                            unidade=item_json['unidade'],
                            quantidade=item_json['quantidade'],
                            valor_uni=item_json['valor_uni'],
                            valor_total=item_json['valor_total']
                        )
                        lista_itens.append(item)

                    self.dict_serv[serv_name] = lista_itens

    self.create_main_section()
    change_service(self)


def open_load(self, Class):
    load_window = Class(self)
    load_window.wait_window()  # Aguarda até que a janela seja fechada
    try:
        return load_window.choosed_load
    except:
        print("veio ate aqui ")  ## adicionar messagebox?
        return False


def obter_nomes_saves():
    # Verifica se o arquivo save.json está vazio
    with open('save.json', 'r') as arquivo:
        conteudo = arquivo.read()
        if conteudo.strip() == "":
            return []
        else:
            dados_existentes = json.loads(conteudo)

    # Retorna os nomes dos saves como uma lista
    return list(dados_existentes.keys())
