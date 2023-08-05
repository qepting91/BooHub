import streamlit as st
import home
import movie_suggester
import story_generator
import decoration_scraper

PAGES = {
    "🏠 Home Sweet Haunted Home": home,
    "👻 History/Recipes/DIY": decoration_scraper,
    "🎬 Spooky Movie Suggester": movie_suggester,
    "📚 Spooky Story Generator": story_generator
}

def main():
    st.sidebar.title('🎃 Navigation')
    page_selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[page_selection]
    page.app()

if __name__ == "__main__":
    main()
