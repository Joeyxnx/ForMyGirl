import streamlit as st

import content

st.set_page_config(
    page_title=f"3 months with {content.HER_NAME} 🩷",
    page_icon="🩷",
    layout="centered",
    initial_sidebar_state="auto",
)

if "reasons_seen" not in st.session_state:
    st.session_state.reasons_seen = []
if "letter_open" not in st.session_state:
    st.session_state.letter_open = False

pages = [
    st.Page("app_pages/home.py", title="Happy 3 months", icon=":material/favorite:", default=True),
    st.Page("app_pages/reasons.py", title="Reasons", icon=":material/auto_awesome:"),
    st.Page("app_pages/timeline.py", title="Our story", icon=":material/timeline:"),
    st.Page("app_pages/quiz.py", title="Quiz", icon=":material/quiz:"),
    st.Page("app_pages/dreams.py", title="Where we're going", icon=":material/flight_takeoff:"),
    st.Page("app_pages/letter.py", title="A letter for you", icon=":material/mail:"),
]

nav = st.navigation(pages)

with st.sidebar:
    st.caption(f"Made for {content.HER_NAME} {content.HER_EMOJI} by {content.MY_NAME}")

nav.run()
