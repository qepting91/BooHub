import streamlit as st
import home as home
import movie_suggester as movie_suggester
import story_generator as story_generator
import decoration_scraper as decoration_scraper

# If 'page' is not in the session_state, set it to 'Home'
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

PAGES = {
    "Home": home,
    "History/Recipes/DIY": decoration_scraper,
    "Halloween Movie Suggester": movie_suggester,
    "Spooky Story Generator": story_generator,
}

def main():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Creepster&display=swap');
    body {
        font-family: 'Creepster', cursive;
    }
    </style>
    """, unsafe_allow_html=True)
    st.sidebar.title('Navigation')
    st.session_state.page = st.sidebar.radio("Go to", list(PAGES.keys()), index=list(PAGES.keys()).index(st.session_state.page))
    page = PAGES[st.session_state.page]

    with st.spinner(f"Loading {st.session_state.page} ..."):
        page.app()

if __name__ == "__main__":
    main()
