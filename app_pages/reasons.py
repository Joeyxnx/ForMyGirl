import random

import streamlit as st

import content

st.title("Reasons I'm into you")
st.caption("There are more than this. These are the ones that fit on a screen.")

seen = st.session_state.reasons_seen
remaining = [r for r in content.REASONS if r not in seen]

controls = st.container(horizontal=True)
if controls.button("Give me a reason", icon=":material/favorite:", type="primary"):
    if remaining:
        seen.append(random.choice(remaining))
    else:
        st.session_state.reasons_seen = [random.choice(content.REASONS)]
        st.balloons()
if controls.button("Start over", icon=":material/refresh:"):
    st.session_state.reasons_seen = []
    st.rerun()

st.space("small")

if not st.session_state.reasons_seen:
    st.info("Tap the button. I wrote these down so I wouldn't forget any of them.", icon=":material/touch_app:")

for reason in reversed(st.session_state.reasons_seen):
    with st.container(border=True):
        st.markdown(f"### {reason}")

if st.session_state.reasons_seen:
    st.caption(f"{len(st.session_state.reasons_seen)} of {len(content.REASONS)} unlocked")
