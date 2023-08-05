import os
import streamlit as st
import tmdbsimple as tmdb
from dotenv import load_dotenv

# Fetch the API keys from secrets
api_key = st.secrets["tmdb_api_key"]
tmdb.API_KEY = api_key


def app():
    # Create a Streamlit UI with Halloween theme and drop-down list
    st.title('Spooky Movie Suggester 🎃')

    st.header('Search for a movie')
    search_query = st.text_input('Enter a search query')

    if st.button('Search by movie name'):
        search = tmdb.Search()
        response = search.movie(query=search_query)
        if response['results']:
            for result in response['results']:
                st.write(f"{result['title']} ({result['release_date']})")
                st.image(f"https://image.tmdb.org/t/p/w500{result['poster_path']}")
                st.write(f"Rating: {result['vote_average']}")
                st.write(f"Popularity: {result['popularity']}")
                st.write(f"Overview: {result['overview']}")
        else:
            st.write("No results found.")

    st.header('Discover movies by genre')
    genre_options = {
        'Horror': 27,
        'Mystery': 9648,
        'Thriller': 53,
    }

    selected_genre = st.selectbox('Select a genre', list(genre_options.keys()))

    sort_options = {
        'Popularity Descending': 'popularity.desc',
        'Popularity Ascending': 'popularity.asc',
        'Rating Descending': 'vote_average.desc',
        'Rating Ascending': 'vote_average.asc',
        'Release Date Descending': 'release_date.desc',
        'Release Date Ascending': 'release_date.asc',
    }

    selected_sort = st.selectbox('Sort by', list(sort_options.keys()))

    if st.button('Discover by genre'):
        # Make the API call and display the results
        discover = tmdb.Discover()
        response = discover.movie(with_genres=genre_options[selected_genre], sort_by=selected_sort)
        if response['results']:
            for result in response['results']:
                st.write(f"{result['title']} ({result['release_date']})")
                st.image(f"https://image.tmdb.org/t/p/w500{result['poster_path']}")
                st.write(f"Rating: {result['vote_average']}")
                st.write(f"Popularity: {result['popularity']}")
                st.write(f"Overview: {result['overview']}")
        else:
            st.write("No results found.")

app()
