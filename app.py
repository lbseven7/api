import streamlit as st
import pandas as pd

# Lendo o arquivo CSV
df = pd.read_csv('encomendas.csv')

# Configurando o título da aplicação
st.title('Visualização de Clientes')

# Loop para criar cards para cada cliente
for index, row in df.iterrows():
    # Criando um card para cada cliente
    with st.container():
        st.subheader(row['cliente'])
        st.write(f'Tema: {row["tema"]}')
        st.write(f'Prazo de Entrega: {row["prazo_entrega"]}')
        st.write(f'Valor: R$ {row["valor"]:.2f}')
        st.markdown("---")  # Linha horizontal para separar os cards

# Executando o Streamlit
if __name__ == '__main__':
    st.write("Acesse este app em: `streamlit run app.py`")
