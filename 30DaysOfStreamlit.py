import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

# Cette commande définit le titre de l'onglet du navigateur
st.set_page_config(
    page_title="Intro à Streamlit",
)

st.title("Intro à Streamlit") # Ceci est le header (H1) dans la page
st.markdown("[30 Days of Streamlit](https://30days.streamlit.app/)")

st.header('st.slider')
st.subheader('st.slider 1')

st.slider("",0,130,25)


values = st.slider(
     '',
     0.0, 100.0, (25.0, 75.0))
st.write('', values)



chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)