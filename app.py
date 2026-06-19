import streamlit as st

# Configura o título do aplicativo
st.title("📝 Minha Lista de Tarefas")

# Cria a lista de tarefas na memória se ela não existir
if "tarefas" not in st.session_state:
    st.session_state.tarefas = []

# Campo para o usuário digitar uma nova tarefa
nova_tarefa = st.text_input("O que você precisa fazer?", placeholder="Digite aqui...")

# Botão para adicionar a tarefa
if st.button("Adicionar Tarefa"):
    if nova_tarefa:
        st.session_state.tarefas.append(nova_tarefa)
        st.rerun()  # Atualiza a tela imediatamente

st.write("---")

# Mostra as tarefas salvas com um botão para remover
if st.session_state.tarefas:
    st.subheader("Suas Tarefas:")
    
    # Lista as tarefas de trás para frente (mais novas no topo)
    for index, tarefa in enumerate(st.session_state.tarefas):
        col1, col2 = st.columns([0.8, 0.2])
        
        # Mostra o texto da tarefa
        col1.write(f"🔹 {tarefa}")
        
        # Botão para apagar a tarefa
        if col2.button("Excluir", key=f"btn_{index}"):
            st.session_state.tarefas.pop(index)
            st.rerun()
else:
    st.info("Você não tem nenhuma tarefa pendente! 🎉")
