import streamlit as st
import ast  # To safely evaluate the string as a dictionary

from scrape import url_constructor, web_scrape_divs
from gpt import generate_response
from preprocess import preprocess_text

# Define the options for the dropdowns
options1 = ['bg']
options2 = list(range(1, 14))  # List 1 to 13
options3 = list(range(1, 100))  # List 1 to 99

# Create the Streamlit UI
st.title('Bhagwat Gita Question Generator')

# Dropdowns
dropdown2 = st.selectbox('Select Chapter', options2)
dropdown3 = st.selectbox('Select Verse', options3)

true_false = st.selectbox('Select number of T/F questions', list(range(1, 6)))
fills = st.selectbox('Select number of fill in the blank questions', list(range(1, 6)))
multipleOps = st.selectbox('Select number of MCQ questions', list(range(1, 6)))
long = st.selectbox('Select number of long questions', list(range(1, 6)))

# Generate button
if st.button('Generate'):
    # Display the scraped text
    data = web_scrape_divs(url_constructor("bg", dropdown2, dropdown3))
    
    prompt = f"Generate {true_false} True/False questions, {fills} fill in the blank questions, {multipleOps} MCQ questions, and {long} long questions about the text given below. (with answers) your questions must be a python list of dictionaries with the following format: {{ 'true_false': [ {{'question': 'Is the sky blue?', 'answer': 'True'}}, {{'question': 'Is fire cold?', 'answer': 'False'}} ], 'MCQ': [ {{'question': 'What is the capital of France?', 'options': ['Berlin', 'Paris', 'Rome', 'Madrid'], 'answer': 'Paris'}}, {{'question': 'Which planet is known as the Red Planet?', 'options': ['Earth', 'Mars', 'Jupiter', 'Venus'], 'answer': 'Mars'}} ]}}"

    data = preprocess_text(data)
    print(data)
    st.header('Questions')
    
    # Call the function to generate the questions
    response = generate_response(prompt, data)
    print(response)

    # Convert the string response to a list of dictionaries
    try:
        # Use `ast.literal_eval` to safely evaluate the string into a list
        questions_list = ast.literal_eval(response)
    except Exception as e:
        st.error(f"Error parsing response: {e}")
        questions_list = []

    st.write(questions_list)
    
