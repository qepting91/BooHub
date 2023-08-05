# BooHub
BooHub is a one-stop application for all your Halloween needs, built with Streamlit. It provides a variety of features to get you into the Halloween spirit, including a Halloween movie suggester, a spooky story generator, and a section for Halloween history, recipes, and DIY decoration ideas.

## Features
Home: The landing page of the application that sets the mood with a Halloween theme.

Halloween Movie Suggester: This page uses The Movie Database (TMDB) API to suggest Halloween-themed movies based on user-selected genre and sorting options.

Spooky Story Generator: This page uses OpenAI's GPT-3 model to generate spooky stories based on a user-provided starting phrase and the chosen story style.

History/Recipes/DIY: This page provides a history of Halloween, along with recipes and DIY decoration ideas. It uses the Streamlit Session State feature to store user interactions across reruns of the application.

## Getting Started
### Prerequisites
Python 3.6 or higher
Streamlit
An API key for The Movie Database (TMDB) API
An API key for OpenAI
### Installation
Clone the repo
sh
'''
git clone https://github.com/your_username_/BooHub.git
'''
Install Python packages
'''
sh
pip install -r requirements.txt
''' 
Create a .env file in the root directory and enter your TMDB and OpenAI API keys:
'''
sh
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'
TMDB_API_KEY = 'YOUR_TMDB_API_KEY'
'''

### Usage
Run the following command in your terminal:
'''
sh
streamlit run app.py
'''

Then navigate to localhost:8501 in your web browser to view the application.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgements
Streamlit
OpenAI
TMDB
