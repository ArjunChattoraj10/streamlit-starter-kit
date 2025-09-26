import streamlit as st
import time

st.set_page_config(page_icon="👋")

st.title("👋 Hello World!")

name = st.text_input("What's your name?")
if name == "Obi-Wan Kenobi":
    st.warning("General Kenobi! You are a bold one.")
elif name:
    st.write(f"Hello there {name}! Nice to meet you!")
    
st.expander("✨ Reveal Code ✨").code(
"""
import streamlit as st

name = st.text_input("What's your name?")
if name == "Obi-Wan Kenobi":
    st.warning("General Kenobi! You are a bold one.")
elif name:
    st.write(f"Hello there {name}! Nice to meet you!")
""", language="python"
)
    
"---"

n = st.slider("Pick a number", min_value=0, max_value=100)
st.write("You picked:", n)

wave_placeholder = st.empty()
for i in range(n):
    wave_placeholder.write("👋"*(i+1))
    time.sleep(0.03)
    
with st.expander("✨ Reveal Code ✨"):
    st.write("Use `st.empty()` to create a placeholder that you can update.")
    st.code(
"""
import streamlit as st

wave_placeholder = st.empty()
for i in range(n):
    wave_placeholder.write("👋"*(i+1))
    time.sleep(0.03)
"""
)

"---"

st.write("You can use buttons and other widgets to make your app interactive.")

if st.button("Show a surprise!", type="primary"):
    st.balloons()
    st.success("Balloons deployed! Great success 👍👍", icon = "🎈")
    
st.write(">NOTE: The way Streamlit works is that it reruns your script from top to bottom every time you interact with a widget.")

st.expander("✨ Reveal Code ✨").code(
"""
import streamlit as st

if st.button("Show a surprise!", type="primary"):
    st.balloons()
    st.success("Balloons deployed! Great success 👍👍", icon = "🎈")
""", language="python"
)
    
"---"

"> ##### EXERCISE 2: Make the output text in the top section appear one letter at a time, like a typewriter effect."


