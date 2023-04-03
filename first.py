import pandas as pd
import numpy as np
import streamlit as st

st.title('This is my first StreamLit App')

## ways to add text into our app

st.header('Header')
st.subheader('Sub Header')
st.text('This is my text i can write long paragraph')
st.markdown("""
# Header 1
## Header 2
### Header 3
This is my **third** line
- 1
- 2

## To pass imoji🤞

:joy:<br>
:smile:

""",unsafe_allow_html=True)

st.latex("""
a^2 + b^2 +2ab
""")
movies=pd.read_csv('movies.csv')
movies=movies[:50]
myList =[1,2,3,4,5,6,7,8,9,10]
arr = np.array(myList)
dim = arr.reshape(2,5)

st.header('--------------------------------------------------------------')
st.write('This is my movies data',movies)
st.write('This is my list',myList)
st.write('This is my arr',dim)

st.write('Data stats description',movies.describe())

