import streamlit as st

ans=st.text_input("Do you like Python?")
if ans==Yes || ans==yes || ans==yeah || ans==Yeah || ans==yep || ans==Yepe:
  st.success("Amazing! :D")
elif ans==no || ans==No || ans==nah || ans==Nah || ans==nope || ans==Nope:
  st.warning("You will like it! >:(")
else:
  st.warning("I don't know what you said")
