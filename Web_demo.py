import streamlit as st
import File_read

todos = File_read.F_read()

st.set_page_config(layout="wide")


def add_todo():
    todo = st.session_state.key = 'new_todo'
    todos.append(todo)
    File_read.F_write(todos)


st.title("My First Web")
st.subheader("This Is my App")
st.write("This app is to improve your <b>productivity</b>",
         unsafe_allows_html=True)

for d in todos:
    st.checkbox(d)

st.text_input(label="", placeholder="Enter value..", on_change=add_todo(), key='new_todo')


