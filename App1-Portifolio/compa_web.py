import streamlit as st
import pandas 

df = pandas.read_csv("data.csv", sep=",")

col1 = st.set_page_config(layout="wide")

col1 , col2 = st.columns(2)


with col1:
    st.title("Alguem Sulce")
    content = """ What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type 
specimen book. It has survived not only five centuries, but also the leap into
 electronic typesetting, remaining essentially unchanged. It was popularised in 
 the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
 and more recently with desktop publishing software like Aldus PageMaker including 
 versions of Lorem Ipsum
    """
    st.write(content)

with col2:
    for i , row in df.iterrows():
        st.header(row["last name"]+"\n")

