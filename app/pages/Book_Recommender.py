import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

df=pd.read_csv("c:/raktim/Book_Recommender_Project/app/pages/app_data.csv")
df=df.drop(["Unnamed: 0"],axis="columns")
pt=df.pivot_table(index="Book-Title",columns="User-ID",values="Book-Rating")
pt=pt.fillna(0)
similarity=cosine_similarity(pt)

def recommend(book_name):
    # finding the index number of the given book
    index=np.where(pt.index==book_name)[0][0]

    # finding the distances of all other books to the given book
    distances=similarity[index]

    # similar books
    similar_books=sorted(list(enumerate(distances)),key=lambda x: x[1],reverse=True)[1:6]

    # recommendations
    recommended_books=[]
    for i in  similar_books:
        recommended_books.append(pt.index[i[0]])
    return recommended_books
    
def main():
    st.set_page_config(page_title="Book Recommender")
    st.title("Book Recommender")
    book=st.text_input(label="Enter Book Title:")
    if st.button(label="Recommendations"):
        st.text("\n")
        st.text("\n")
        try:
            for n in recommend(book):
                df1=df[df['Book-Title']==n]
                df1=df1.reset_index()
                st.image(df1.loc[0,'Image-URL-L'])
                st.text(f"{df1.loc[0,'Book-Title']}\nAuthor: {df1.loc[0,'Book-Author']}")
                st.text("\n")
                st.text("\n")
        except Exception as exp:
            st.text("oops! Book is either not present in database or please check the\nspelling or case of the specified book.")

if __name__=="__main__":
    main()
