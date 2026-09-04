# 3 months 🩷

A tiny Streamlit love site.

## Edit this first

Open `content.py` and change the block at the top:

```python
HER_NAME = "Amor"              # her name
MY_NAME  = "Joey"              # your name
START_DATE = date(2026, 6, 4)  # the day you became official
```

Everything else on the site (reasons, milestones, quiz questions, trips, the
letter) is also in `content.py`. Rewrite anything that isn't true — the words
matter more than the code.

## Run it locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Put it online (free, ~5 minutes)

1. Push this folder to a **public** GitHub repo.
2. Go to https://share.streamlit.io and sign in with GitHub.
3. "Create app" → pick the repo → main file path: `streamlit_app.py` → Deploy.
4. You get a `https://<something>.streamlit.app` link. Send her that.

Community Cloud apps sleep after inactivity and wake on the first visit, so the
very first load can take ~30 seconds. Everything after that is instant.
