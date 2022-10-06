import streamlit as st
import pandas as pd
import numpy as np

# Parte 1

df = pd.DataFrame({
  'primeira coluna': [1, 2, 3, 4],
  'segunda coluna': [10, 20, 30, 40]
})
df

# Parte 2

st.write("Esta é a nossa primeira tentativa de usar dados para criar uma tabela:")
st.write(pd.DataFrame({
    'primeira coluna': [1, 2, 3, 4],
    'segunda coluna': [10, 20, 30, 40]
}))

# Parte 3

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

# Parte 4

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns = (f'col{i}' for i in range(20))
)
st.dataframe(dataframe.style.highlight_max(axis=0))

# Parte 5

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns = (f'col{i}' for i in range(20))
)
st.table(dataframe)

# Parte 6

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['a', 'b', 'c']
)
st.line_chart(chart_data)

# Parte 7

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns = ['lat', 'lon']
)
st.map(map_data)

# Parte 8

x = st.slider('x')
st.write(x, 'ao quadrado é', x * x)

# Parte 9

st.text_input("Seu nome", key='nome')
st.session_state.nome

# Parte 10

if st.checkbox('Mostrar dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns = ['a', 'b', 'c']
    )
    chart_data

# Parte 11

df = pd.DataFrame({
    'primeira coluna': [1, 2, 3, 4],
    'segunda coluna': [10, 20, 30, 40]
})
option = st.selectbox(
    'Qual dos números você gosta mais?',
    df['primeira coluna']
)
f'Você selecionou: {option}'

# Parte 12

sidebar_selectbox = st.sidebar.selectbox(
    'Como você gostaria de ser contactado?',
    ('Email', 'Telefone fixo', 'Celular')
)
sidebar_slider = st.sidebar.slider(
    'Selecione um intervalo de valores:',
    0.0, 100.0, (25.0, 75.0)
)
st.sidebar.write(sidebar_slider)

# Parte 13

left_column, right_column = st.columns(2)
left_column.button('Pressione-me!')

with right_column:
    chosen = st.radio(
        'Chapéu seletor',
        ('Grifinória', 'Corvinal', 'Lufa-lufa', 'Sonserina')
    )
    st.write(f'Você está na casa {chosen}')

# Parte 14

import time

'Iniciando uma longa computação...'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteração {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'...e agora, terminamos!'

# Parte 15

st.markdown("# Página principal 🎈")
st.sidebar.markdown("# Página principal 🎈")