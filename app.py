
# import streamlit as st
# from langchain.prompts import PromptTemplate
# from langchain.llms import CTransformers

# # Function to get response from Llama 2 model
# def get_llama_response(input_text, no_words, blog_style):
#     try:
#         # Initialize the Llama model
#         llm = CTransformers(
#             model='meta-llama/Llama-2-13b-chat',
#             model_type='llama',
#             config={
                
#                 'temperature': 0.01
#             }
#         )
        
#         # Define the prompt template
#         template = """
#         Write a blog for {blog_style} job profile for a topic {input_text}
#         within {no_words} words.
#         """
        
#         prompt = PromptTemplate(
#             input_variables=["blog_style", "input_text", 'no_words'],
#             template=template
#         )
        
#         # Generate the response from the Llama 2 model
#         formatted_prompt = prompt.format(
#             blog_style=blog_style,
#             input_text=input_text,
#             no_words=no_words
#         )
#         response = llm(formatted_prompt)
        
#         return response

#     except Exception as e:
#         return f"An error occurred: {e}"

# # Streamlit app configuration
# st.set_page_config(
#     page_title="Generate Blogs",
#     page_icon='🤖',
#     layout='centered',
#     initial_sidebar_state='collapsed'
# )

# st.header("Generate Blogs 🤖")

# input_text = st.text_input("Enter the Blog Topic")

# # Creating two columns for additional fields
# col1, col2 = st.columns([5, 5])

# with col1:
#     no_words = st.text_input('No of Words')
# with col2:
#     blog_style = st.selectbox('Writing the blog for',
#                               ('Researchers', 'Data Scientist', 'Common People'), index=0)

# submit = st.button("Generate")

# # Final response
# if submit:
#     if not input_text or not no_words.isdigit():
#         st.error("Please provide valid input text and number of words.")
#     else:
#         st.write(get_llama_response(input_text, int(no_words), blog_style))


api = 'cGfPNELkmpnwy4F3ixEsmhISszNi9Xj0'

import streamlit as st
from langchain.prompts import PromptTemplate
from mistralai import Mistral

# Replace 'your_api_key_here' with your actual API key
api_key = api 
mistral_model = Mistral(api_key=api_key)

# Function to get response from Mistral model
def get_mistral_response(input_text, no_words, blog_style):
    try:
        # Define the prompt template
        template = """
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
        """
        
        prompt = PromptTemplate(
            input_variables=["blog_style", "input_text", "no_words"],
            template=template
        )
        
        # Generate the formatted prompt
        formatted_prompt = prompt.format(
            blog_style=blog_style,
            input_text=input_text,
            no_words=no_words
        )
        
        messages = [{"role": "user", "content": formatted_prompt}]
        
        # Generate the response from the Mistral model
        response = mistral_model.chat.complete(
            model="mistral-large-latest", 
            messages=messages
        )

        # Access the content from the response
        reply = response.choices[0].message.content  # Correctly access the content attribute

        return reply

    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit app configuration
# st.set_page_config(
#     page_title="Generate Blogs",
#     page_icon='🤖',
#     layout='centered',
#     initial_sidebar_state='collapsed'
# )

# st.header("Generate Blogs 🤖")

# input_text = st.text_input("Enter the Blog Topic")

# # Creating two columns for additional fields
# col1, col2 = st.columns([5, 5])

# with col1:
#     no_words = st.text_input('No of Words')
# with col2:
#     blog_style = st.selectbox('Writing the blog for',
#                               ('Researchers', 'Data Scientist', 'Common People'), index=0)

# submit = st.button("Generate")

# # Final response
# if submit:
#     if not input_text or not no_words.isdigit():
#         st.error("Please provide valid input text and number of words.")
#     else:
#         st.write(get_mistral_response(input_text, int(no_words), blog_style))

import streamlit as st
from langchain.prompts import PromptTemplate
from mistralai import Mistral

# Set page configuration
st.set_page_config(
    page_title="Generate Blogs",
    page_icon='🤖',
    layout='centered',
    initial_sidebar_state='collapsed'
)

# Create a centered title using Markdown
st.markdown("<h1 style='text-align: center;'>Generate Blogs 🤖</h1>", unsafe_allow_html=True)

# Continue with the rest of your code
input_text = st.text_input("Enter the Blog Topic")

# Creating two columns for additional fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Researchers', 'Data Scientist', 'Common People'))

submit = st.button("Generate")

# Final response logic...

if submit:
    if not input_text or not no_words.isdigit():
        st.error("Please provide valid input text and number of words.")
    else:
        st.write(get_mistral_response(input_text, int(no_words), blog_style))

    # Final response logic...
