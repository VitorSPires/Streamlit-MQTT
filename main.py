import mqtt
import streamlit as st
import style

style.setStyle()

st.title('Teste')
with st.expander('expander 1', expanded=True):
    option = st.radio(
        "What's your favorite movie genre",
        ('Comedy', 'Drama', 'Documentary'))

if st.button('Botão'):
    mqtt.publish(mqtt.client, 'teste0')

with st.expander('expander 2', expanded=True):
    if option == 'Comedy':
        if st.button('Gerenciador de tarefas'):
            mqtt.publish(mqtt.client, 'teste')
        if st.button('Botão windows'):
            mqtt.publish(mqtt.client, 'teste2')
        if st.button('esc'):
            mqtt.publish(mqtt.client, 'teste3')
        if st.button('alt f4'):
            mqtt.publish(mqtt.client, 'teste4')

        if st.checkbox('teste 5') == True:
            mqtt.publish(mqtt.client, 'teste5')
        else: mqtt.publish(mqtt.client, 'teste6')

    elif option == 'Drama':
        st.text('nada aqui')

    else:
        st.text('nada aqui tbm')