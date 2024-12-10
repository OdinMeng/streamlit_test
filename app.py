import streamlit as st

class Gun():
    def __init__(self):
        self.rounds = 6
    
    def shoot(self):
        n = rnd.randint(1, self.rounds)
        if n == 1:
            return 'Died'
        else:
            self.rounds -= 1
            return f'Alive... {self.rounds} rounds left' # Alive

st.title('button clicker')
'''look at this cool app!'''

if 'num' not in st.session_state:
    st.session_state['num'] = 0

'---'
st.latex(st.session_state.num)

x = st.button('Click me')

if x:
    st.session_state.num += 1
