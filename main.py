import mqtt
import streamlit as st
import style

style.setStyle()

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
            mqtt.publish('teste')
        if st.button('Botão windows'):
            mqtt.publish('teste2')
        if st.button('esc'):
            mqtt.publish('teste3')
        if st.button('alt f4'):
            mqtt.publish('teste4')

        if st.checkbox('teste 5') == True:
            mqtt.publish('teste5')
        else: mqtt.publish('teste6')

    elif option == 'Cena 2':
        st.text('nada aqui')

    else:
        st.text('nada aqui tbm')