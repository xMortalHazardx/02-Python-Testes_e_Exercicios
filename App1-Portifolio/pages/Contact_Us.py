import streamlit as st

st.header("Contact Us")

with st.form(key="formulario"):
    usuario_email = st.text_input("Digite seu Endereço de Email:")
    message = st.text_area("Digite sua mensagem:")
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        print("Pressionado")