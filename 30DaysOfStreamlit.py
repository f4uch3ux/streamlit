import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Intro à Streamlit",
)

st.title("Intro à Streamlit")
st.markdown("[30 Days of Streamlit](https://30days.streamlit.app/)")

st.header('slider')
st.subheader('slider 1')

st.slider("",0,130,25)

st.subheader('slider 2')

st.slider('',0.0, 100.0, (25.0, 75.0))


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


st.selectbox("selectbox",(1,2))

st.multiselect("multiselect",(1,2))