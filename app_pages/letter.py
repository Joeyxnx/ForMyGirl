import streamlit as st

import content

st.title("A letter for you")

if not st.session_state.letter_open:
    with st.container(border=True, horizontal_alignment="center"):
        st.markdown("### 💌", text_alignment="center")
        st.markdown("I wrote this out properly. Open it when you have a minute.", text_alignment="center")
        if st.button("Open it", type="primary", icon=":material/mail:"):
            st.session_state.letter_open = True
            st.rerun()
else:
    with st.container(border=True):
        st.markdown(
            content.LETTER.format(
                name=content.HER_NAME,
                her=content.HER_NAME,
                me=content.MY_NAME,
            )
        )
    if st.button("Close it", icon=":material/mail_lock:"):
        st.session_state.letter_open = False
        st.rerun()
    st.snow()
