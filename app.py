# THIS IS THE SAMPLE OF PLAYLIST IN WHICH (SONG A AND SONG B ) SHOWN :- 
# import streamlit as st
# import pandas as pd 
# import numpy as np
# import plotly.express as px
# # import matplotlip.pyplot as plt
# # import seaborn as sns 

# # Page Title :-
# st.title("France Top 50 Music Dashboard")

# # Load Dataset :-
# df = pd.read_csv("france_top50.csv")

# # Show Dataset:-
# st.subheader("Dataset Preview")
# st.dataframe(df)

# # Basic Information :-
# st.subheader("Dataset Information")

# st.write("Total Rows:", df.shape[0])
# st.write("Total Coloumns:", df.shape[1])

# # Top 50 Songs By Popularity 
# st.subheader("Top 50 Songs By Popularity")

# top_songs= df.sort_values(by="popularity" , ascending=False).head(10)

# fig = px.bar(
#     top_songs,
#     x="song",
#     y="popularity",
#     color="artist",
#     title="Top 50 Popular Songs"
# )
# st.plotly_chart(fig)

# #Explicit_Content Count :-

# st.subheader("Explicit Vs Non-Explicit Songs ")

# explicit_count = df["is_explicit"].value_counts()

# fig2 = px.pie(
#     values = explicit_count.values,
#     names= explicit_count.index,
#     title= "Explicit Content Distribution"
# )
# st.plotly_chart(fig2)

#NOW WE WRITE MAIN CODE BEACUSE OUR COLLECT_DATA.PY DASHBOARD WORKS PROPERLY:-

import streamlit as st
import pandas as pd

st.set_page_config(page_title="France Top 50 Music Dashboard", layout="wide")

st.title("France Top 50 Music Dashboard")

# CSV load
df = pd.read_csv("france_top50.csv")

# Clean column names
df.columns = [col.strip().lower() for col in df.columns]

st.subheader("Dataset Preview")
st.dataframe(df)

st.subheader("Dataset Information")
col1, col2 = st.columns(2)
col1.metric("Total Rows", len(df))
col2.metric("Total Columns", len(df.columns))

# Basic checks
if "song" in df.columns and "popularity" in df.columns:
    st.subheader("Top Songs by Popularity")
    top_songs = df.sort_values("popularity", ascending=False).head(10)
    st.bar_chart(top_songs.set_index("song")["popularity"])

if "artist" in df.columns:
    st.subheader("Top Artists")
    artist_counts = df["artist"].value_counts().head(10)
    st.bar_chart(artist_counts)

if "popularity" in df.columns:
    st.subheader("Popularity Summary")
    st.write(df["popularity"].describe())

st.success("Dashboard loaded successfully!")
