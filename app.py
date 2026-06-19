import streamlit as st

st.title("📝 Minha Lista de Tarefas")

if "tarefas" not in st.session_state:
    st.session_state.tarefas = []

nova_tarefa = st.text_input("O que você precisa fazer?", placeholder="Digite aqui...")


if st.button("Adicionar Tarefa"):
    if nova_tarefa:
        st.session_state.tarefas.append(nova_tarefa)
        st.rerun() 
st.write("---")

if st.session_state.tarefas:
    st.subheader("Suas Tarefas:")
    
    for index, tarefa in enumerate(st.session_state.tarefas):
        col1, col2 = st.columns([0.8, 0.2])
        
        col1.write(f"🔹 {tarefa}")
        
        if col2.button("Excluir", key=f"btn_{index}"):
            st.session_state.tarefas.pop(index)
            st.rerun()
else:
    st.info("Você não tem nenhuma tarefa pendente! 🎉")
