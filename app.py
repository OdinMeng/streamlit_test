import streamlit as st

st.title('button clicker')
'''look at this cool app!'''

if 'num' not in st.session_state:
    st.session_state['num'] = 0

'---'
st.latex(st.session_state.num)

x = st.button('Click me')

if x:
    st.session_state.num += 1
