# IMPORTANDO BIBLIOTECAS--------------------------------
import customtkinter as app
from deep_translator import GoogleTranslator as google
#FUNÇÃO-------------------------------------------------
def traduzir():
    texto_Traduzir = entrada.get()
    linguagem = lang_to_var.get()
    saida_Traduzida = google(source='auto',target=linguagem).translate(texto_Traduzir)
    saida.delete(0,"end")
    saida.insert(0,saida_Traduzida)
#CRIANDO JANELA-----------------------------------------
janela = app.CTk()
janela.geometry('600x400')
janela.title('Tradutor Universal')
#APARENCIA DA JANELA------------------------------------
app.set_appearance_mode('dark')
app.set_default_color_theme('green')
app.CTkLabel(janela,text='TRADUTOR UNIVERSAL', font=('Times New Roman',30,'bold'), text_color='green').pack(pady=20)
#ENTRADA------------------------------------------------
entrada = app.CTkEntry(janela, placeholder_text='Digitar Texto para Traduzir', width=400, height=40, text_color='white')
entrada.pack(pady=20)
#TRADUTOR-----------------------------------------------
app.CTkLabel(janela, text='Selecione a Linguagem:', font=('Calibri', 18, 'bold'), text_color='white').pack(pady=0)
lang_to_var = app.StringVar(value='english')
lang_list = google().get_supported_languages()
lang_to = app.CTkOptionMenu(janela,values=lang_list, variable=lang_to_var)
lang_to.set('english')
lang_to.pack(pady=0)
#SAIDA---------------------------------------------------
saida = app.CTkEntry(janela, placeholder_text='Texto Traduzido', width=400, height=60, text_color='white')
saida.pack(pady=20)
#BOTÃO---------------------------------------------------
translated_btn = app.CTkButton(janela, text='Traduzir', font=('arial',18, 'bold'), command=traduzir).pack()
#INICIANDO O PROCESSO------------------------------------
janela.mainloop()