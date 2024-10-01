import streamlit as st
import pandas as pd

# Lendo o arquivo CSV
df = pd.read_csv('encomendas.csv')

# Configurando o título da aplicação
st.title('Visualização de Clientes')

# Exibindo os cards de clientes existentes
st.header('Clientes Cadastrados')
for index, row in df.iterrows():
    with st.container():
        st.subheader(row['cliente'])
        st.write(f'Tema: {row["tema"]}')
        st.write(f'Prazo de Entrega: {row["prazo_entrega"]}')
        st.write(f'Valor: R$ {row["valor"]:.2f}')
        st.markdown("---")  # Linha horizontal para separar os cards

# Formulário para cadastrar novo cliente
st.header('Cadastrar Novo Cliente')
with st.form(key='new_client_form'):
    cliente = st.text_input('Nome do Cliente')
    tema = st.text_input('Tema')
    prazo_entrega = st.date_input('Prazo de Entrega')
    valor = st.number_input('Valor', min_value=0.0, format="%.2f")
    
    submit_button = st.form_submit_button(label='Cadastrar')

    if submit_button:
        # Adiciona o novo cliente ao DataFrame
        novo_cliente = pd.DataFrame({
            'cliente': [cliente],
            'tema': [tema],
            'prazo_entrega': [prazo_entrega],
            'valor': [valor]
        })

        # Concatena o novo cliente ao DataFrame existente
        df = pd.concat([df, novo_cliente], ignore_index=True)

        # Salva o DataFrame atualizado no arquivo CSV
        df.to_csv('encomendas.csv', index=False)

        st.success(f'Cliente {cliente} cadastrado com sucesso!')

# Executando o Streamlit
if __name__ == '__main__':
    st.write("Acesse este app em: `streamlit run app.py`")
