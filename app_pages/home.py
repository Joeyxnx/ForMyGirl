from datetime import date

import streamlit as st

import content

today = date.today()
days = (today - content.START_DATE).days
months = days / 30.44

with st.container(horizontal_alignment="center"):
    st.title("Happy 3 months 🩷", text_alignment="center")
    st.subheader(f"to the best thing that's happened to me, {content.HER_NAME}", text_alignment="center")

st.space("small")

cards = [
    ("Days together", f"{days}", "and counting"),
    ("Hours together", f"{days * 24:,}", "not enough"),
    ("Months", f"{months:.1f}", "three whole ones"),
]
for column, (label, value, note) in zip(st.columns(3), cards):
    with column.container(border=True):
        st.metric(label, value)
        st.caption(note)

st.space("small")

with st.container(border=True, horizontal_alignment="center"):
    st.markdown("### Love meter", text_alignment="center")
    st.progress(1.0, text="100% — sensor broke, it kept climbing")

st.space("small")

if st.button("Press me 🎈", type="primary", width="stretch"):
    st.balloons()
    st.toast(f"Te amo, {content.HER_NAME} 🤍", icon="🩷")

with st.container(border=True):
    st.markdown("#### Our completely accurate statistics")
    for label, value, note in content.STATS:
        row = st.container(horizontal=True, vertical_alignment="center")
        row.markdown(f"**{value.format(days=days)}** &nbsp; {label}")
        row.space("stretch")
        row.caption(note)

st.caption("Use the menu on the left. There's more. 👈")
