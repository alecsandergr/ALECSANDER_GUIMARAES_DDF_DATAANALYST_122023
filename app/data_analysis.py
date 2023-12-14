import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st


# Function for Data Analysis Page
def data_analysis_page(df: pd.DataFrame):
    # Sidebar with category filter
    st.sidebar.title("Filter Options")
    category_checkbox = st.sidebar.checkbox(
        "All Categories", help="Check this box to select all categories"
    )
    all_categories = sorted(df["category"].dropna().unique())

    if category_checkbox:
        selected_categories = st.sidebar.multiselect(
            "Select Category", all_categories, default=all_categories
        )
    else:
        selected_categories = st.sidebar.multiselect("Select Category", all_categories)

    # Text input for searching
    search_term = st.sidebar.text_input("Search by Title or Description")

    # Display filtered results title
    st.subheader("Filtered Results")

    # Filter data based on category and search term
    filtered_df = df[
        (df["category"].isin(selected_categories))
        & (df["title"].str.contains(search_term, case=False))
        & (df["text"].str.contains(search_term, case=False))
    ]

    # Display filtered results
    st.dataframe(filtered_df)
    sorted_categories = filtered_df["category"].value_counts().index

    # Slider for the number of categories to display
    num_categories_to_display = st.slider(
        "Number of Categories to Display", 5, 10, value=5
    )

    # Plot the number of products for each category
    st.subheader("Number of Products by Category")
    fig, ax = plt.subplots()
    sns.countplot(
        x="category",
        data=filtered_df,
        ax=ax,
        order=sorted_categories[:num_categories_to_display],
    )
    ax.set(
        # title="Number of Products for Each Category",
        xlabel="Category",
        ylabel="Number of Products",
    )

    # Rotate x-axis labels
    plt.xticks(rotation=45, ha="right")

    # Display y-axis ticks as integers
    ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

    st.pyplot(fig, clear_figure=True)
