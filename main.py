import streamlit as st
import functions

checkBox = functions.ReadFunction()


def Add_tod():
    todo = st.session_state['input_todo'] + '\n'
    checkBox.append(todo)
    functions.WriteFunction(checkBox)


st.title('Welcome to Todo ')
st.subheader('Add things To Do')
st.write('Whenever  Ideas come to mind ,Use TO dO')

for index, box in enumerate(checkBox):
    result = st.checkbox(box, key=box)
    if result:
        checkBox.pop(index)
        functions.WriteFunction(checkBox)
        del st.session_state[box] # delete console date as well
        st.experimental_rerun() #this will refresh after deleting


st.text_input(label='type', on_change=Add_tod, placeholder='Add new Todo...',
              key='input_todo', )


