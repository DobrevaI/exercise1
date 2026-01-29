import streamlit as st

ans=st.text_input("Do you like Python?")
if ans==yes or ans==yeah or ans==yep:
  st.success("Amazing! :D")
elif ans==no or ans==nah or ans==nope:
  st.warning("You will like it! >:(")
else:
  st.warning("I don't know what you said")
