import mqtt
import streamlit as st
import style

style.setStyle()
client = mqtt.setup()

cenas = ['Pré-culto', 'Cronômetro', 'Culto', 'Pós-culto', 'Problemas', 'Temporário']
canalTeste = "vitor/teste/canal1"

st.title('Controle OBS')
with st.expander('Cenas', expanded=True):
    option = st.radio(
        'É necessário fazer transição após escolher uma cena',
        cenas)

if st.button('Transição', key='btnTransicao'):
        client.publish("vitor/teste/canal1", 'Transicao')

if  option == cenas[0]:
    client.publish(canalTeste, 'preCulto')

if  option == cenas[1]:
    client.publish(canalTeste, 'Cronometro')

elif option == cenas[2]:
    client.publish(canalTeste, 'CenaCulto')
    with st.expander('Fontes', expanded=True):
        if st.button('Avisos'):
            client.publish(canalTeste, 'Avisos')
        if st.button('Like e sub'):
            client.publish(canalTeste, 'LikeSub')
        if st.button('QR fixo'):
            client.publish(canalTeste, 'QRFixo')
        if st.button('QR ofertas'):
            client.publish(canalTeste, 'QROferta')
        if st.button('Culto presencial'):
            client.publish(canalTeste, 'CultoPresencial')

elif  option == cenas[3]:
    client.publish(canalTeste, 'PosCulto')

elif  option == cenas[4]:
    client.publish(canalTeste, 'Problemas')

elif  option == cenas[5]:
    client.publish(canalTeste, 'Temporario')

