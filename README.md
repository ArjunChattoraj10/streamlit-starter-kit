# Streamlit Workshop

Welcome! This repo contains exercises appropriate to getting started with **Streamlit**.  
We’ll build a **multi-page Streamlit app** with the following content:

1. **Streamlit Intro** - A start page showing the display of text
2. **Hello App** - An introduction to Streamlit's Inputs and Outputs
3. **Data Explorer** - Working with Dataframes and Charts, and an intro to the Sidebar
4. **Countdown** - A countdown timer

## Streamlit Documentation

Refer to all Streamlit-related documentation here: https://docs.streamlit.io/

---

## Project Structure

```text
streamlit-workshop/
│
├── README.md
├── requirements.txt
│
├── Streamlit_Intro.py             # Landing page / intro
└── pages/
    ├── 1_Hello_App.py            
    ├── 2_Data_Explorer.py        
    └── 3_Countdown.py         

```

`Streamlit_Intro.py`  is the **landing page**, with workshop instructions.  

Within `pages/`, each script becomes a separate page.  

Streamlit automatically creates a **sidebar menu** with these pages, ordered by the numeric prefixes (`1_`, `2_`, `3_`).  

---

## Setup

1. Clone this repo:
```bash
git clone https://github.com/ArjunChattoraj10/streamlit-starter-kit.git
cd streamlit-starter-kit
```

Or you can download this repo as a Zip file and extract the contents to your device.

2. Create a virtual environment (*recommended*):

```bash
python -m venv streamlit_venv
# macOS/Linux
source streamlit_venv/bin/activate
# Windows (Command Prompt)
streamlit_venv\Scripts\activate
```

3. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Run the app
```bash
streamlit run Streamlit_Intro.py
```

This launches the landing page at http://localhost:8501

Use the sidebar to navigate between:

- Streamlit Intro
- Hello App
- Data Explorer
- Countdown

---


