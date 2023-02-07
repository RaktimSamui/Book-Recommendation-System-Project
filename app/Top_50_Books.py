import streamlit as st
import pandas as pd

def main():
    df=pd.read_csv("top_50.csv")
    df=df.drop(["Unnamed: 0"],axis="columns")
    st.set_page_config(page_title="Top 50 Books")
    st.title("Top 50 Books")
    st.write("\n\n")
    for i in range(len(df)):
        st.text(f"Book {i+1}")
        st.image(df.loc[i,"Image-URL-M"])
        st.text(f"{df.loc[i,'Book-Title']}\nAuthor: {df.loc[i,'Book-Author']}\nNo. of Ratings: {df.loc[i,'num_of_ratings']}\nAverage Rating: {round(df.loc[i,'average_rating'],2)}")
        st.text("\n")
        st.text("\n")
if __name__=="__main__":
    main()

