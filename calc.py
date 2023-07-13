import streamlit as st
from PIL import Image
import numpy as np


#Opções sidebar
st.sidebar.title("Menu")


import base64
import streamlit as st


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('./H12PRO.png')

#Plano de fundo sidebar

def set_background_sidebar(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    [data-testid=stSidebar] {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background_sidebar('./mural.png')



#Calculo da Taxa de Aplicação
def calcular_taxa(vazao, velocidade, faixa):
    taxa = (vazao * 10000) / (velocidade * faixa * 60)
    return taxa

#Calculo de vazão
def calcular_vazao(velocidade, faixa):
    vazao = (velocidade * faixa * 60) / 10000
    return vazao


#Caixa seletora
paginaselecionada = st.sidebar.selectbox("Selecione a página", {"Calculadora Taxa de Aplicação", "Calculadora de Vazão"})

#Pagina Taxa de Aplicação 
if paginaselecionada == "Calculadora Taxa de Aplicação":
    st.title("Calculadora Taxa de Aplicação")
    #Definição das variaveis 
    velocidade = st.number_input("Insira a velocidade (m/s):")
    faixa = st.number_input("Insira a faixa (m):")
    vazão = st.number_input("Insira a vazão (L/min):")
    
    #Botões programáveis
    calcular = st.button("Calcular")
    limpar = st.button("Limpar")

    if calcular:
        taxa = calcular_taxa(vazão, velocidade, faixa)
        resultado = st.write(f"Taxa de Aplicação (L/h) é: {taxa}")
    
    if limpar:
        st.experimental_rerun()

elif paginaselecionada == "Calculadora de Vazão":
    st.title("Calculadora de Vazão")
    #Definição das variaveis pag 2
    velocidade = st.number_input("Digite o valor da velocidade: ")
    faixa = st.number_input("Digite o valor da faixa: ")
    

    #Botões programáveis
    calcular = st.button("Calcular")
    limpar = st.button("Limpar")
    

    if calcular:
        vazao = calcular_vazao( velocidade, faixa)
        resultado = st.write(f"Vazão é: {vazao}")
    
    if limpar:
        st.experimental_rerun()
    



