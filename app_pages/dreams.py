import streamlit as st

import content

st.title("Where we're going")
st.caption("Pick one. I'll start looking at flights tonight, I'm serious.")

choice = st.segmented_control(
    "Next trip",
    [f"{emoji} {city}" for city, emoji, _ in content.DREAM_TRIPS],
    default=None,
    label_visibility="collapsed",
    width="stretch",
)

if choice:
    for city, emoji, blurb in content.DREAM_TRIPS:
        if choice == f"{emoji} {city}":
            with st.container(border=True):
                st.markdown(f"### {emoji} {city}")
                st.write(blurb)
            st.toast(f"{city} it is 🧳", icon="✈️")
else:
    st.info("Tap a place.", icon=":material/touch_app:")

st.space("medium")

st.header("The menu when we get there")
st.caption("Non-negotiable order of operations.")

cols = st.columns(2)
for i, (dish, note) in enumerate(content.MENU):
    with cols[i % 2].container(border=True):
        st.markdown(f"**{dish}**")
        st.caption(note)

st.space("medium")

st.header("The soundtrack")
st.caption("You made me like this.")
st.iframe(
    "https://open.spotify.com/embed/artist/4q3ewBCX7sLwd24euuV69X?utm_source=generator",
    height=352,
)
