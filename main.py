import mqtt
import streamlit as st
import style

style.setStyle()
client = mqtt.setup()

st.title('Controle OBS')
with st.expander('Cenas', expanded=True):
    option = st.radio(
        'É necessário fazer transição após escolher uma cena',
        ('Cena 1', 'Cena 2', 'Cena 3', 'Teste'))

if st.button('Transição', key='btnTransicao'):
        client.publish("vitor/teste/canal1", 'Transição')

canalTeste = "vitor/teste/canal1"

with st.expander('Fontes', expanded=True):
    if option == 'Cena 1':
        client.publish(canalTeste, 'cena1')
        if st.button('Fonte 1'):
            client.publish(canalTeste, '')
        if st.button('Fonte 2'):
            client.publish(canalTeste, '')
        if st.button('Fonte 3'):
            client.publish(canalTeste, '')
        if st.button('Fonte 4'):
            client.publish(canalTeste, '')

    elif option == 'Cena 2':
        client.publish(canalTeste, 'cena2')
        st.text('nada aqui')

    elif option == 'Cena 3':
        client.publish(canalTeste, 'cena3')
        st.text('nada aqui tbm')

    if option == 'Teste':
        client.publish(canalTeste, 'cenaTeste')
        if st.button('Gerenciador de tarefas'):
            client.publish(canalTeste, 'teste1')
        if st.button('Botão windows'):
            client.publish(canalTeste, 'teste2')
        if st.button('esc'):
            client.publish(canalTeste, 'teste3')
        if st.button('alt f4'):
            client.publish(canalTeste, 'teste4')

