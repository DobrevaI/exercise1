import streamlit as st

ans=st.text_input("Do you like Python?")
if ans=="yes" or ans=="yeah" or ans=="yep":
  st.success("Amazing! :D")
elif ans=="no" or ans=="nah" or ans=="nope":
  st.error("You will like it! >:(")
else:
  st.error("I don't know what you said")

num=st.number_input("Please put a number... any number...")
if num==10:
  st.success("That number is big")
elif num>10:
  st.error("that number is too big")
else:
  st.warning("that number is too small")

number=st.number_input("What is 5*5?")
if st.button("Check"):
  if number==25:
    st.success("That is correct")
  else:
    st.error("Ohhhh that would be incorrect")
