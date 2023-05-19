import streamlit as st
import functions

checkBox = functions.ReadFunction()

st.title('Welcome to Todo ')
st.subheader('Add things To Do')
st.write('Whenever  Ideas come to mind ,Use TO dO')

# for box in checkBox:
#     st.checkbox(box, key=box)

st.text_input(label='type', placeholder='Add new Todo...')
print('hi there')
