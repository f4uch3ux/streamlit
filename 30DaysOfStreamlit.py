import numpy as np
import pandas as pd
import streamlit as st
import time

st.set_page_config(
    page_title="Intro à Streamlit",
)



st.title("Intro à Streamlit")
st.markdown("[30 Days of Streamlit](https://30days.streamlit.app/)")

st.write("\n")

st.divider()
st.markdown("[Code source](https://github.com/f4uch3ux/streamlit/blob/main/30DaysOfStreamlit.py)")

st.header('progress bar')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.01)
     my_bar.progress(percent_complete + 1)

st.header('slider')
st.subheader('slider 1')

st.slider("slider 1",0,130,25)

st.subheader('slider 2')

st.slider('slider 1',0.0, 100.0, (25.0, 75.0))


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)



st.selectbox("selectbox",(1,2))

st.multiselect("multiselect",(1,2))

un=st.checkbox("1")
deux=st.checkbox("2")

if un: st.write("1 a été choisi")
if deux: st.write("2 a été choisi")

st.subheader("LaTeX")
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)


with st.expander('expander'):
  st.write('expander activé')

st.sidebar.header('sidebar')
user_name=st.sidebar.text_input('tape ton username')


col1, col2 = st.columns(2)



with col1:
  if user_name != '':
    st.write(f'Bonjour {user_name}')
  else:
    st.write(' tape ton username (sidebar) ')


with col2:
  if user_name != '':
    st.write(f'Bonjour {user_name}')
  else:
    st.write(' tape ton username (sidebar) ')


with st.form('my_form'):
    st.subheader('**Order your coffee**')

    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    submitted = st.form_submit_button('Submit')
if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        ''')
else:
    st.write('☝️ Place your order!')


st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)


st.header('données URL')
st.markdown("[http://10.158.34.214:8501/?firstname=Tom&surname=Faucheux](http://10.158.34.214:8501/?firstname=Tom&surname=Faucheux)")

surname = st.query_params.get('surname', 'Inconnu')

firstname = st.query_params.get('firstname', 'Inconnu')

st.write(f'Bonjour **{firstname} {surname}**')


from time import time

st.title('st.cache_data')

# Using cache
a0 = time()
st.subheader('Using st.cache_data')

# Remplacement par st.cache_data
@st.cache_data
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)


# Not using cache
b0 = time()
st.subheader('Not using st.cache_data')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)


st.subheader("session_state")

st.write("sans session_state, le nom est perdu quand on fait suivant et on nous redemande notre nom")

if "etape" not in st.session_state:
    st.session_state.etape = 1
if "nom" not in st.session_state:
    st.session_state.nom = ""
if "projet" not in st.session_state:
    st.session_state.projet = ""

#### Étape 1 : Informations personnelles
if st.session_state.etape == 1:
    st.subheader("Étape 1 : Qui êtes-vous ?")
    st.session_state.nom = st.text_input("Votre nom", value=st.session_state.nom)
    
    if st.button("Suivant"):
        if st.session_state.nom:
            st.session_state.etape = 2
            st.rerun()
        else:
            st.error("Veuillez entrer un nom.")

#### Étape 2 : Détails du projet
elif st.session_state.etape == 2:
    st.subheader("Étape 2 : Votre projet")
    st.session_state.projet = st.text_area("Description du projet", value=st.session_state.projet)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Retour"):
            st.session_state.etape = 1
            st.rerun()
    with col2:
        if st.button("Valider"):
            st.session_state.etape = 3
            st.rerun()

#### Étape 3 : Récapitulatif
elif st.session_state.etape == 3:
    st.subheader("Résumé de votre soumission")
    st.write(f"**Nom :** {st.session_state.nom}")
    st.write(f"**Projet :** {st.session_state.projet}")
    
    if st.button("Recommencer"):
        st.session_state.etape = 1
        st.session_state.nom = ""
        st.session_state.projet = ""
        st.rerun()



