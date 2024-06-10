import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
url = 'https://github.com/githubmhd/movie_recommendations/blob/main/App/movie_final_ML.csv'
st.title('Build and shared data application!')
with st.container():
    st.write("This is inside the first container")
    df_cars = pd.read_csv(url)
    df_cars
st.write("This is outside the container")