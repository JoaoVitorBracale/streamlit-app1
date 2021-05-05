#Bibliotecas padrão
#Aplicação
import streamlit as st

#Pagina incial - Fixo
st.sidebar.write("""
#### A.M.D.G
Ad maiorem Dei glorie
""")

st.sidebar.header('Menu de navegação:')

st.sidebar.markdown("""Escolha uma das opções abaixo para continuar""")
opcoes = ["Home", "Ação de Graças", "Ação de Graças Personalizada","News Letter"]

nav = st.sidebar.radio("Opções:", opcoes)

#Separação Menu
if nav == "Home":
    st.title("Lirios de São José")
    st.subheader("São José, rogai por nós!")
    
    st.title("Home")
    st.image("imagens/saojose.png", width=None)

    st.markdown('''
    A igreja Cátolica é uma igreja fundada a mais de 2 mil anos atrás.

    A maior devoção(não idolatria) é ao Santissimo Sacramento.
    No qual a igreja, desde os apóstulos e os santos padres afirmam verdadeiramente que é o Próprio Jesus Cristo!
    Seu Corpo, Sague, Alma e Divindade.

    Um nomedo como Apostolo da Eucaristia é São Pedro Julião Eymard.
    
    ''')

elif nav == "Ação de Graças":
    st.title("Ação de Graças com São Pedro Julião Eymard")

    meditacao_do_dia = ''' 
    Meditação...
    '''

    st.subheader('Medição do dia')
    st.markdown(meditacao_do_dia)

    if st.checkbox('Oração'):
        st.subheader('Escrever')

    if st.checkbox('Flor'):
        st.subheader('Oferecimento...')
    
    if st.checkbox('Imagem'):
        #st.image
        pass

elif nav == "Ação de Graças Personalizada":
    st.text_area('Escreva...')

    st.subheader('Similaridade com as meditações salvas dele')

elif nav == "Ação de Graças com análise de sentimentos":
    st.text_area('Sentimento')

elif nav == "News Letter":
    email = st.text_input('Digite seu melhor e-mail:')
