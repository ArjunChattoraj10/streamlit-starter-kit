import streamlit as st

st.set_page_config(page_title="Streamlit Hands-On Workshop", page_icon=":rocket:")

st.title("Streamlit Hands-On Workshop")

st.write(
    """
    Welcome to the **Hands-On Streamlit workshop**!  
    Use the sidebar to navigate through the exercises:
    
    1. **Hello App** -- your first interactive UI  
    2. **Data Explorer** -- filter & chart a dataset  
    3. **File Uploader** -- upload your own CSV and explore  
    
    Have fun exploring!
    
    ---
    """
)

"There are many ways to write with Streamlit. You can just write text directly like this!"

"You can also just put numbers here."

24601

st.markdown("#### Write and format text with Markdown")

st.write(
    """
    Streamlit also supports Markdown, which is a simple way to format text.
    You can use `st.write()` or `st.markdown()` to use Markdown formatting.
    """
)

st.write(
    """    
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text
    """
)

st.write(
    """
    ## Code Blocks
    
    You can also write code snippets with syntax highlighting. Use `st.code()` or Markdown backticks: \```

    This is a *Python* code snippet:
    """
)

st.code(
"""
import pandas as pd
import numpy as np

# Basic variables
x = 42
y = [1, 2, 3, 4, 5]
z = {"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]}

for i in y:
    print(i)

print(x)
print(np.mean(y))
print(pd.DataFrame(z))
""", language="python"
)

st.write("This is one that uses *R*:")

st.code(
"""
install.packages("tidyverse")   # for data wrangling & visualization
install.packages("data.table")  # for fast data manipulation

library(tidyverse)
library(data.table)

# Basic variables
x <- 42
y <- c(1, 2, 3, 4, 5)
z <- data.frame(id = 1:3, name = c("Alice", "Bob", "Charlie"))

for (val in y) {
  print(val)
}

print(x)
summary(y)
View(z)
""", language="r"
)
    
"---"

st.write("> ##### EXERCISE 1: Write an introduction for yourself and show it on your app!")







