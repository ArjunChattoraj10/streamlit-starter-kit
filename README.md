# Streamlit Workshop

Welcome! This repo contains exercises appropriate to getting started with **Streamlit**.  
We’ll build a **multi-page Streamlit app** with three exercises plus an additional try-it-yourself exercise:

1. **Hello App** - your first Streamlit UI with slider, checkbox, and text input  
2. **Data Explorer** - interactive DataFrame filtering and charting  
3. **File Uploader** - upload your own CSV and inspect it
4. **Build Your Own Chart** - an exercise to build your own chart

---

## Project Structure

```text
streamlit-workshop/
│
├── README.md
├── requirements.txt
│
├── app.py                         # Landing page / intro
└── pages/
    ├── 1_Hello_App.py             # Exercise 1
    ├── 2_Data_Explorer.py         # Exercise 2
    ├── 3_File_Uploader.py         # Exercise 3
    └── 4_Build_Your_Own_Chart.py  # Bonus exercise

```

`app.py`  is the **landing page**, with workshop instructions.  

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

2. Create a virtual environment (recommended):

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
streamlit run app.py
```

This launches the landing page at http://localhost:8501

Use the sidebar to navigate between:

- Hello App
- Data Explorer
- File Uploader
- Bonus Build-Your-Own Chart

---


