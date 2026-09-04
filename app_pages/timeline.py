from datetime import date

import streamlit as st

import content

st.title("Our story so far")
st.caption("Short book. Very good book.")

days = (date.today() - content.START_DATE).days

for marker, title, blurb in content.MILESTONES:
    with st.container(border=True):
        row = st.container(horizontal=True, vertical_alignment="center")
        row.markdown(f":primary-badge[{marker}]")
        row.markdown(f"**{title}**")
        st.write(blurb)

st.space("small")

with st.container(border=True):
    st.markdown("#### What happens next")
    st.write(
        f"Month 4, month 12, month 60. I'm not in a rush, I just want the whole list. "
        f"Day {days} was pretty great though."
    )
