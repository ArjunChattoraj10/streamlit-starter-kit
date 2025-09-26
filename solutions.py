# Hello App.py solution:
import time

name_plc = st.empty()
out = f"Hello there {name}! Nice to meet you!"
for i in range(len(out)):
    name_plc.write(out[:i+1])
    time.sleep(0.03)
    
# Data Explorer.py solution:
statistic = st.sidebar.selectbox("Select statistic:", ["Mean", "Median", "Max", "Min"])

if statistic == "Mean":
    stats = df.groupby("region")["movies watched"].mean().round(2)
elif statistic == "Median":
    stats = df.groupby("region")["movies watched"].median().round(2)
elif statistic == "Max":
    stats = df.groupby("region")["movies watched"].max().round(2)
else:  # Min
    stats = df.groupby("region")["movies watched"].min().round(2)
    
st.markdown(f"**{statistic} number of movies watched by region:**")
st.dataframe(stats)
