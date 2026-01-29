import streamlit as st

ans=st.text_input("Do you like Python?")
if ans==Yes or ans==yes or ans==yeah or ans==Yeah or ans==yep or ans==Yepe:
  st.success("Amazing! :D")
elif ans==no or ans==No or ans==nah or ans==Nah or ans==nope or ans==Nope:
  st.warning("You will like it! >:(")
else:
  st.warning("I don't know what you said")
