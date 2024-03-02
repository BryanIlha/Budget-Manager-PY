import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
# from funcion import * # importando todas funções
# objetos como tabela e items
from objects import Table, TopLevelWindow, Item, LoadWindow
from funcion import create_excel, new_service, delete_service, clear_table, change_service, save_dict, load_dict


ctk.set_appearance_mode("dark")


ctk.set_default_color_theme("green")

# root = tk.Tk()


class MainWindow(ctk.CTk):
    def __init__(self,  *args, **kwargs):
        # global root
        # self.root = root
        super().__init__(*args, **kwargs)

        self.simple_counter = 0  # revisar first time counter
        # lista de serviços utizilar em condicionais para nao deixar exportar sem nenhum serviço
        self.dict_serv = {}

        # self.self.button_frame= None
        self.toplevel_window = None  # burocracia pra ter toplevel window

        self.title("Custom Tkinter App")
        self.geometry("800x600")

        # Configure color palette

        # Configure dark blue theme

        self.create_sidebar()
        self.first_service()

    def first_service(self):
        self.main_section = ctk.CTkFrame(self.master,)
        self.main_section.pack(expand=True, fill="both", padx=20, pady=10)

        title_label = ctk.CTkLabel(
            self.main_section, text="Gerenciador de orçamentos", font=("Arial", 20))
        title_label.pack(pady=10)

        self.bt_serv = ctk.CTkButton(
            self.main_section, text="Novo Serviço", command=lambda: self.first_serv())
        self.bt_serv.configure(fg_color="purple",
                               hover_color="blue",
                               width=80,
                               height=80)
        self.bt_serv.pack(side="top", pady=5)

    def create_sidebar(self):
        self.sidebar = ctk.CTkFrame(self.master, width=200)
        self.sidebar.pack(side="left", fill="y")

        profile_photo = ctk.CTkLabel(self.sidebar, text="Profile Photo",)
        profile_photo.pack(pady=20)

        section1_button = ctk.CTkButton(
            self.sidebar, text="Section 1", command=lambda: create_excel())  # nao funciona
        section1_button.pack(pady=5, padx=10, fill="x")

        save_btn = ctk.CTkButton(self.sidebar, text="Salvar", command=lambda: save_dict(
            self))  # tirar daqui depois
        save_btn.pack(pady=5, padx=10, fill="x")

        load_btn = ctk.CTkButton(self.sidebar, text="Carregar", command=lambda: load_dict(
            self, Item, LoadWindow))  # tirar daqui depois
        load_btn.pack(pady=5, padx=10, fill="x")
        self.button_frame = ctk.CTkFrame(self.master,)

    def first_serv(self):

        if new_service(self) is True or self.dict_serv != {}:
            self.create_main_section()

    def create_main_section(self):
        self.bt_serv.destroy()
        dict_serv_keys = list(self.dict_serv.keys())

        self.option_serv = ctk.CTkOptionMenu(self.main_section,
                                             values=dict_serv_keys,
                                             command=self.switch_service)
        self.option_serv.configure(width=300)
        self.option_serv.pack(anchor="center")

        table_frame = ctk.CTkFrame(self.main_section)
        table_frame.pack(expand=True, fill="both", padx=10, pady=10)
        self.table_instance = Table(table_frame)

<<<<<<< HEAD
            table_frame = ctk.CTkFrame(self.main_section)
            table_frame.pack(expand=True, fill="both", padx=10, pady=10)
            self.table_instance = Table(table_frame,self)
=======
        self.button_frame = ctk.CTkFrame(self.master,)
        self.button_frame.pack(fill="both",  padx=20,
                               pady=10)  # devo adicionar side?
>>>>>>> TopLevel/GUI

        self.bt_serv = ctk.CTkButton(
            self.button_frame, text="Novo Serviço", command=lambda: new_service(self))
        self.bt_serv.configure(fg_color="purple",
                               hover_color="blue",
                               width=80,
                               height=80)
        self.bt_serv.pack(side="left", pady=5)

        self.bt_del_serv = ctk.CTkButton(
            self.button_frame, text="Deletar Serviço", command=lambda: delete_service(self))
        self.bt_del_serv.configure(fg_color="red",
                                   hover_color="black",
                                   width=80,
                                   height=80)
        self.bt_del_serv.pack(side="left", pady=5)

        self.bt_item = ctk.CTkButton(
            self.button_frame, text="Novo item", command=self.open_topLevel)
        self.bt_item.configure(fg_color="green",
                               width=80,
                               height=80)
        self.bt_item.pack(side="right", pady=5)

<<<<<<< HEAD
            self.bt_new_item = ctk.CTkButton(self.button_frame, text="Novo item",command=self.open_topLevel)
            self.bt_new_item.configure(fg_color="green",
                                    width=80,
                                    height=80)
            self.bt_new_item.pack(side="right",pady=5)


=======
    def open_topLevel(self):  # new item
        service_name = self.option_serv.get()
>>>>>>> TopLevel/GUI

        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = TopLevelWindow(
                self, self.table_instance, service_name, self.dict_serv)
            self.toplevel_window.grab_set()
        else:
            self.toplevel_window.focus()

    def switch_service(self, choice):  # precisa?
        change_service(self)

    def update_service(self, current_index, dict_keys):
        # Obtém as chaves atualizadas do dicionário

        # Limpa o valor selecionado no OptionMenu
        self.option_serv.set('')
        # Verifica se há chaves no dicionário
        # Encontra a posição da chave atualmente selecionada no OptionMenu

        # Calcula o índice da próxima chave no OptionMenu
        next_index = (current_index + 1) % len(dict_keys)

        # Seleciona a próxima chave no OptionMenu
        self.option_serv.set(dict_keys[next_index])
        self.option_serv.configure(values=self.dict_serv)
        change_service(self)

    def clean_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()


def main():

    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
