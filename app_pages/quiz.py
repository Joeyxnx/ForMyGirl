import streamlit as st

import content

st.title("How well do you know us?")
st.caption("There are no wrong answers. There are answers that are more correct.")

with st.form("quiz", border=False):
    picks = []
    for i, item in enumerate(content.QUIZ):
        with st.container(border=True):
            picks.append(st.radio(item["q"], item["options"], index=None, key=f"q{i}"))
    submitted = st.form_submit_button("Check my answers", type="primary", icon=":material/check:")

if submitted:
    score = sum(p == item["answer"] for p, item in zip(picks, content.QUIZ))
    st.space("small")
    st.metric("Your score", f"{score} / {len(content.QUIZ)}", border=True)

    for pick, item in zip(picks, content.QUIZ):
        if pick == item["answer"]:
            st.success(item["note"].format(name=content.HER_NAME), icon=":material/favorite:")
        else:
            st.warning(
                f"**{item['q']}** — it was *{item['answer']}*. "
                + item["note"].format(name=content.HER_NAME),
                icon=":material/lightbulb:",
            )

    if score == len(content.QUIZ):
        st.balloons()
        st.markdown("### Perfect score. Obviously. 🏆", text_alignment="center")
    else:
        st.markdown("### Still counts. You get to keep me either way. 🩷", text_alignment="center")
