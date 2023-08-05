import streamlit as st
import textwrap
from streamlit_extras.let_it_rain import rain
from streamlit_extras.badges import badge
from markdownlit import mdlit

def app():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Creepster&display=swap');
    body {
        font-family: 'Creepster', cursive;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    # 🎃 Welcome to the Halloween Hub!
    This is a special application dedicated to Halloween lovers! Especially my beautiful wife!
    """)

    st.markdown("""
    <div style="width:100%;height:0;padding-bottom:68%;position:relative;">
    <iframe src="https://giphy.com/embed/xT9IgvEOwRzUcZDRiU" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
    </div>
    <p><a href="https://giphy.com/gifs/pennywise-it-movie-scary-clown-xT9IgvEOwRzUcZDRiU">via GIPHY</a></p>
    """, unsafe_allow_html=True)

    st.markdown("## You'll float too 🎈")

    st.markdown("""
    ### Here's what you can do:
    - Get Halloween movie suggestions based on your preferences.
    - Generate a spooky Halloween-themed story.
    - Find the best Halloween DIY/Recipes and Halloween History.
    """)

    # Raining Emojis
    rain(
        emoji="🎃👻💀🕷️🕸️🦇🧛‍♂️🧟‍♀️",
        font_size=12,
        falling_speed=5,
        animation_length="infinite",
    )

    # Buy Me A Coffee Badge
    badge(type="buymeacoffee", name="qepting")

    # Collapsible content
    mdlit(
        textwrap.dedent(
            """
            ??? Bonus
                @(💀)(A very spooooky surprise!)(https://www.youtube.com/watch?v=2mKN6PDZTmc)
            """
        )
    )
