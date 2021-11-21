import mqtt
import streamlit as st
import style

style.setStyle()
client = mqtt.setup()

st.title('Teste')
with st.expander('expander 1', expanded=True):
    option = st.radio(
        "What's your favorite movie genre",
        ('Cena 1', 'Cena 2', 'Cena 3'))

if st.button('Botão'):
    mqtt.publish(mqtt.client, 'teste0')

with st.expander('expander 2', expanded=True):
    if option == 'Cena 1':
        if st.button('Gerenciador de tarefas'):
            client.publish("vitor/teste/canal1", 'teste1')
        if st.button('Botão windows'):
            client.publish("vitor/teste/canal1", 'teste2')
        if st.button('esc'):
            client.publish("vitor/teste/canal1", 'teste3')
        if st.button('alt f4'):
            client.publish("vitor/teste/canal1", 'teste4')

        if st.checkbox('teste 5') == True:
            client.publish("vitor/teste/canal1", 'teste5')
        else:
            client.publish("vitor/teste/canal1", 'teste6')

    elif option == 'Cena 2':
        st.text('nada aqui')

    else:
        st.text('nada aqui tbm')