import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
# from funcion import * # importando todas funções
from objects import Table, TopLevelWindow #objetos como tabela e items
from funcion import create_excel, inputbox


ctk.set_appearance_mode("dark")



ctk.set_default_color_theme("green")

class MainWindow(ctk.CTk):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.dict_serv={} #lista de serviços utizilar em condicionais para nao deixar exportar sem nenhum serviço
        

        self.toplevel_window = None #burocracia pra ter toplevel window
        

        self.title("Custom Tkinter App")
        self.geometry("800x600")

        # Configure color palette

        # Configure dark blue theme

        
        self.create_sidebar()
        self.first_service()
        
        
    def first_service(self):
        self.main_section = ctk.CTkFrame(self.master,)
        self.main_section.pack(expand=True, fill="both", padx=20, pady=10)

        title_label = ctk.CTkLabel(self.main_section, text="Gerenciador de orçamentos", font=("Arial", 20))
        title_label.pack(pady=10)

        self.bt_serv = ctk.CTkButton(self.main_section, text="Novo Serviço", command= lambda:self.create_main_section())
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

        section1_button = ctk.CTkButton(self.sidebar, text="Section 1",command= lambda:create_excel())
        section1_button.pack(pady=5, padx=10, fill="x")

        section2_button = ctk.CTkButton(self.sidebar, text="Section 2", command= lambda:self.first_service()  )
        section2_button.pack(pady=5, padx=10, fill="x")

    def create_main_section(self):

        self.new_service()
        self.bt_serv.destroy()
        dict_serv_keys = list(self.dict_serv.keys())

        self.option_serv = ctk.CTkOptionMenu(self.main_section ,
                                             values=dict_serv_keys,
                                             command=self.switch_service)
        self.option_serv.configure(width=300)
        self.option_serv.pack(anchor="center")


        table_frame = ctk.CTkFrame(self.main_section)
        table_frame.pack(expand=True, fill="both", padx=10, pady=10)
        self.table = Table(table_frame)

        button_frame = ctk.CTkFrame(self.master,)
        button_frame.pack(fill="both",  padx=20, pady=10) #devo adicionar side?

        self.bt_serv = ctk.CTkButton(button_frame, text="Novo Serviço",command=self.new_service)
        self.bt_serv.configure(fg_color="purple",
                                hover_color="blue",
                                width=80,
                                height=80)
        self.bt_serv.pack(side="left", pady=5)

        self.bt_del_serv = ctk.CTkButton(button_frame, text="Deletar Serviço",command=self.delete_service)
        self.bt_del_serv.configure(fg_color="red",
                                hover_color="black",
                                width=80,
                                height=80)
        self.bt_del_serv.pack(side="left", pady=5)

        self.bt_item = ctk.CTkButton(button_frame, text="Novo item",command=self.open_topLevel)
        self.bt_item.configure(fg_color="green",
                                width=80,
                                height=80)
        self.bt_item.pack(side="right",pady=5)



    def open_topLevel(self): #new item
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = TopLevelWindow(self,self.table)
            else:
                self.toplevel_window.focus()
        
    
    def new_service(self): #nome dos serviços so para aparecer no option menu
        
        service_name = inputbox("Novo Serviço",("Digite o nome do Serviço")) # o service é um array do objeto item

        self.dict_serv[service_name] = []
        for serv in self.dict_serv:
            print(serv)
        if len(self.dict_serv)!=1: #BAIANO
                    #sempre que for da update pegar index e lens

            self.option_serv.configure(values=self.dict_serv)
            dict_keys = list(self.dict_serv.keys())
            current_index = dict_keys.index(self.option_serv.get())

            self.update_service(current_index,dict_keys)

    def switch_service(self,choice):
        print(f'trocou por {choice}')

    def delete_service(self):
        #sempre que for da update pegar index e lens
        dict_keys = list(self.dict_serv.keys())
        current_index = dict_keys.index(self.option_serv.get())
        
        if len(self.dict_serv) ==1:
            print("nao da dog so tem um") #MODAL
        else:    
            service_to_dlt= self.option_serv.get()
            del self.dict_serv[service_to_dlt]
            self.update_service(current_index,dict_keys) #dar update
            print('apaguei o ',service_to_dlt) #MODAL
    
    def update_service(self,current_index,dict_keys):
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


def main():

    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
