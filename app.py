import streamlit as st
from scrape import url_constructor, web_scrape_divs
# Define custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f2d3a3; /* Background color */
    }
    .css-ffhzg2 {
        background-color: #e7bd83; /* Buttons and dropdowns */
    }
    .css-14xtw13 {
        color: black; /* Text color */
    }
    .css-18e3c1e {
        color: #9b6a55; /* Headings color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define the options for the dropdowns
options1 = ['bg']
options2 = list(range(1, 14))
# list 1 to 13
options3 = list(range(1, 100))

# Create the Streamlit UI
st.title('Streamlit Dropdown Example')

# Dropdowns
dropdown1 = st.selectbox('Select Book', options1)
dropdown2 = st.selectbox('Select Chapter', options2)
dropdown3 = st.selectbox('Select Verse', options3)

# Generate button
if st.button('Generate'):
    # Display the scraped text
    st.write(web_scrape_divs(url_constructor(dropdown1, dropdown2, dropdown3)))