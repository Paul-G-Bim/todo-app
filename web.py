import streamlit as st
from streamlit import session_state

import r_w_todos as rw

todos = rw.get_todos()

def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    rw.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        rw.write_todos(todos)
        del session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Enter a new todo...", on_change=add_todo, key="new_todo")

# enable below line used to see the session.state object (dictionary)
# st.session_state
