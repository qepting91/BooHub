from datetime import datetime
import os
import random
import string
import openai
import streamlit as st
from dotenv import load_dotenv 
import toml

# Parse the TOML file
config = toml.load("secrets.toml")

# Access the keys
openai_key = config["api_keys"]["openai_key"]



def load_env():
    """
    Load environment variables
    """
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_story(starting_phrase, length=1000, artist_role='Dark Romanticism'):
    """
    Generate a story based on the user's starting phrase and selected style
    """
    role_prompt = {
        'Dark Romanticism': "You are an encapsulating storyteller, weaving captivating tales of dark romanticism, akin to Edgar Allan Poe.",
        'Horror': "You are the king of horror, skilled in crafting tales of dark fantasy, science fiction, psychological suspense, and horror, in the style of Stephen King."
    }

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": role_prompt[artist_role]},
            {"role": "user", "content": starting_phrase},
        ],
        max_tokens=length,
    )

    return response.choices[0].message['content']

def app():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Creepster&display=swap');
    body {
        font-family: 'Creepster', cursive;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title('Spooky Story Generator')
    starting_phrase = st.text_input('Enter a starting phrase for your story')
    artist_role = st.selectbox('Choose a style for your story', ['Dark Romanticism', 'Horror'])

    if st.button('Generate'):
        # Use your story generation model here
        st.write("Generating your spooky story. Please wait...")
        story = generate_story(starting_phrase, artist_role=artist_role)
        st.write(f"Your story starts with '{starting_phrase}'. Here is how it unfolds...")
        st.write(story)

if __name__ == "__main__":
    load_env()
    app()
