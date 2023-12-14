import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def prediction_page(df: pd.DataFrame):
    st.subheader("Prediction Page")
    st.write(
        "Welcome to the Prediction Page! Select a product from the sidebar, and we will find similar products based on their descriptions."
    )

    # Siderbar for product selection
    selected_product = st.sidebar.selectbox("Select a Product", df["title"])

    # Display selected product
    st.subheader("Selected Product: ")
    st.write(selected_product)
    st.write(f'Description: {df[df["title"] == selected_product]["text"].values[0]}')

    # Similarity analysis
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df["text"])
    cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Get the index of the selected product
    selected_index = df.index[df["title"] == selected_product].to_list()[0]

    # Get the most similar products
    similar_products = list(enumerate(cosine_similarities[selected_index]))
    similar_products = sorted(similar_products, key=lambda x: x[1], reverse=True)[
        1:6
    ]  # Exclude the selected product itself

    # Display similar products
    st.subheader("Similar products: ")
    for i, (index, similarity) in enumerate(similar_products):
        st.write(f'{i + 1}. {df.iloc[index]["title"]} (Similarity: {similarity: .2f})')
