import streamlit as st
from motor import gerar_jogos

st.set_page_config(page_title="Máquina da Quina", layout="centered")

st.title("🎰 Máquina da Quina")
st.write("Gerador automático de jogos da Quina – versão fechada")

quantidade = st.slider("Quantidade de jogos", 1, 20, 5)

if st.button("Gerar jogos"):
    jogos = gerar_jogos(quantidade)
    st.success("Jogos gerados com sucesso")
    for i, jogo in enumerate(jogos, 1):
        st.write(f"Jogo {i}: {jogo}")