import streamlit as st
import pandas as pd
import time
import datetime
import random

date = datetime.date

datetime = time.time
questions = pd.read_csv(
    "questions.csv",
    sep=";",
)
rand = random.randint(0, len(questions) - 1)

st.title(f"Smalltalk-O-Mat")
n_questions = st.sidebar.slider("Anzahl Fragen",1,10)
catgeory = st.sidebar.selectbox("Kategorie", questions["tag"].unique())

random_questions  = questions.sample(n_questions)

# display each as markdown item 
for i in range(n_questions):
    st.header(random_questions["question"].iloc[i])



random_selection = st.button("Random new")
if random_selection:
    rand = random.randint(0, len(questions) - 1)

st.divider( )
with st.expander("Explore all questions"):
    edited = st.data_editor(questions, hide_index=True, num_rows="dynamic")
    edited.to_csv("questions.csv", index=False, sep=";")
