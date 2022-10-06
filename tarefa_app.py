from tkinter.tix import COLUMN
import streamlit as st
import pandas as pd
import numpy as np

# Parte 18

st.title('Corridas de Uber em Nova Yorque')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

# Parte 19

st.subheader('Dados brutos')
st.write(data)

# Parte 20

st.subheader('Número de corridas por hora')

hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]

st.bar_chart(hist_values)

# Parte 21

st.subheader('Mapa das corridas.')
st.map(data)