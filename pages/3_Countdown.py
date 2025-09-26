import streamlit as st
import time
from datetime import timedelta, datetime

st.set_page_config(page_icon="⏳")

st.title("⏳ Countdown Timer")

# Input minutes
minutes = st.number_input("Set timer:", min_value=1, max_value=120, value=5, step=1)

# --- Session state initialization ---
if "running" not in st.session_state:
    st.session_state.running = False
if "end_time" not in st.session_state:
    st.session_state.end_time = None
if "paused_remaining" not in st.session_state:
    st.session_state.paused_remaining = None
if "last_minutes" not in st.session_state:
    st.session_state.last_minutes = minutes

# --- Detect change in input box and reset ---
if minutes != st.session_state.last_minutes:
    st.session_state.running = False
    st.session_state.end_time = None
    st.session_state.paused_remaining = timedelta(minutes=minutes)
    st.session_state.last_minutes = minutes

# --- Start button ---
if st.button("▶️ Start"):
    st.session_state.running = True
    if st.session_state.paused_remaining:
        st.session_state.end_time = datetime.now() + st.session_state.paused_remaining
    else:
        st.session_state.end_time = datetime.now() + timedelta(minutes=minutes)
    st.session_state.paused_remaining = None

# --- Stop button ---
if st.button("⏸️ Pause"):
    st.session_state.running = False
    if st.session_state.end_time:
        st.session_state.paused_remaining = st.session_state.end_time - datetime.now()

# --- Reset button ---
if st.button("🔄 Reset"):
    st.session_state.running = False
    st.session_state.end_time = None
    st.session_state.paused_remaining = timedelta(minutes=minutes)

# --- Display timer ---
placeholder = st.empty()

if st.session_state.running and st.session_state.end_time:
    while datetime.now() < st.session_state.end_time:
        if not st.session_state.running:
            break
        remaining = st.session_state.end_time - datetime.now()
        mins, secs = divmod(int(remaining.total_seconds()), 60)
        placeholder.markdown(f"<h1 style='font-size:100px'>{mins:02d}:{secs:02d}</h1>", unsafe_allow_html=True)
        time.sleep(1)
    else:
        placeholder.markdown("## 🎉 Time’s up!")
elif st.session_state.paused_remaining:
    mins, secs = divmod(int(st.session_state.paused_remaining.total_seconds()), 60)
    placeholder.markdown(f"<h1 style='font-size:100px'>{mins:02d}:{secs:02d}</h1>", unsafe_allow_html=True)
else:
    placeholder.markdown(f"## ⏰ Ready: {minutes:02d}:00")
