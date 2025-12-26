import streamlit as st
import functions

def add_todo():
    newItem = st.session_state["new_todo"] + '\n'
    functions.addNewItem(newItem)

st.title("Todos")

list = functions.getListFromFile()

for l in list:
    checkbox = st.checkbox(l, key = l)
    if checkbox:
        print(f"Completing {l}")
        functions.removeItemByName(l)
        st.rerun()


st.text_input(label="", placeholder="Add new todo ",
              on_change=add_todo, key="new_todo")


