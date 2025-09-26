import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_icon="📊")
st.title("📊 Mini Data Explorer")

seed = st.sidebar.number_input("Set Seed", value=42)
np.random.seed(seed)
df = pd.DataFrame({
    "quarter": ["Q1","Q2","Q3","Q4"] * 4,
    "region": ["Northeast"]*4 + ["South"]*4 + ["Midwest"]*4 + ["West"]*4,
    "movies watched": (np.random.rand(16) * 10 + 10).round(0),
})

st.markdown("**Dataset (sample):**")
st.dataframe(df)

region = st.selectbox("Choose region to filter", options=["All"] + sorted(df["region"].unique()))
df_filtered = df if region == "All" else df[df["region"] == region]

st.markdown("**Filtered dataset:**")
st.dataframe(df_filtered)

grouped = df_filtered.groupby("quarter", as_index=True)["movies watched"].sum()
st.line_chart(grouped, y="movies watched")

st.sidebar.header("Region Comparison")
selected_region1 = st.sidebar.selectbox("Choose X-Axis:", df["region"].unique())
selected_region2 = st.sidebar.selectbox("Choose Y-Axis:", df["region"].unique())
chart_type = st.sidebar.radio("Chart type:", ["Bar", "Line", "Scatter"])

st.write("---")

st.markdown("### Comparison Chart")

## Build comparison chart
df_pivot = df.pivot(index="quarter", columns="region", values="movies watched").reset_index()

if chart_type == "Bar":
    chart1 = alt.Chart(df_pivot).mark_bar().encode(x="quarter", y=selected_region1, tooltip=["quarter", selected_region1]).properties(width=300).interactive()
    chart2 = alt.Chart(df_pivot).mark_bar().encode(x="quarter", y=selected_region2, color=alt.value("orange"), tooltip=["quarter", selected_region2]).properties(width=300).interactive()
    comparison_chart = alt.hconcat(
        chart1,
        chart2
    ).resolve_scale(y="shared")
elif chart_type == "Line":
    comparison_chart = (alt.Chart(df_pivot).mark_line(point=True).encode(x="quarter", y=selected_region1, tooltip=["quarter", selected_region1]).properties(width=300).interactive() +
                        alt.Chart(df_pivot).mark_line(point=True).encode(x="quarter", y=selected_region2, color=alt.value("orange"), tooltip=["quarter", selected_region2]).properties(width=300).interactive())
else:  # Scatter
    comparison_chart = alt.Chart(df_pivot).mark_circle(size=100).encode(x=selected_region1, y=selected_region2, color=alt.value("purple"), tooltip=["quarter", selected_region1, selected_region2]).properties(width=300).interactive()

st.altair_chart(comparison_chart, use_container_width=True)

"---"

st.write("> ##### EXERCISE 3: Let's get stats! Add a sidebar widget to select a statistic (mean, median, max, min) to calculate the values for each region.")

st.sidebar.write("---")

if st.sidebar.checkbox("Show code", value=False):
    st.write("---")
    st.code(
"""
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_icon="📊")
st.title("📊 Mini Data Explorer")

seed = st.sidebar.number_input("Set Seed", value=42)
np.random.seed(seed)
df = pd.DataFrame({
    "quarter": ["Q1","Q2","Q3","Q4"] * 4,
    "region": ["Northeast"]*4 + ["South"]*4 + ["Midwest"]*4 + ["West"]*4,
    "movies watched": (np.random.rand(16) * 10 + 10).round(0),
})

st.markdown("**Dataset (sample):**")
st.dataframe(df)

region = st.selectbox("Choose region to filter", options=["All"] + sorted(df["region"].unique()))
df_filtered = df if region == "All" else df[df["region"] == region]

st.markdown("**Filtered dataset:**")
st.dataframe(df_filtered)

grouped = df_filtered.groupby("quarter", as_index=True)["movies watched"].sum()
st.line_chart(grouped, y="movies watched")

st.sidebar.header("Region Comparison")
selected_region1 = st.sidebar.selectbox("Choose X-Axis:", df["region"].unique())
selected_region2 = st.sidebar.selectbox("Choose Y-Axis:", df["region"].unique())
chart_type = st.sidebar.radio("Chart type:", ["Bar", "Line", "Scatter"])

st.write("---")

st.markdown("### Comparison Chart")

## Build comparison chart
df_pivot = df.pivot(index="quarter", columns="region", values="movies watched").reset_index()

if chart_type == "Bar":
    chart1 = alt.Chart(df_pivot).mark_bar().encode(x="quarter", y=selected_region1, tooltip=["quarter", selected_region1]).properties(width=300).interactive()
    chart2 = alt.Chart(df_pivot).mark_bar().encode(x="quarter", y=selected_region2, color=alt.value("orange"), tooltip=["quarter", selected_region2]).properties(width=300).interactive()
    comparison_chart = alt.hconcat(
        chart1,
        chart2
    ).resolve_scale(y="shared")
elif chart_type == "Line":
    comparison_chart = (alt.Chart(df_pivot).mark_line(point=True).encode(x="quarter", y=selected_region1, tooltip=["quarter", selected_region1]).properties(width=300).interactive() +
                        alt.Chart(df_pivot).mark_line(point=True).encode(x="quarter", y=selected_region2, color=alt.value("orange"), tooltip=["quarter", selected_region2]).properties(width=300).interactive())
else:  # Scatter
    comparison_chart = alt.Chart(df_pivot).mark_circle(size=100).encode(x=selected_region1, y=selected_region2, color=alt.value("purple"), tooltip=["quarter", selected_region1, selected_region2]).properties(width=300).interactive()

st.altair_chart(comparison_chart, use_container_width=True)
"""
    )

