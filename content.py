"""All the personal stuff lives here. Edit this file, nothing else."""

from datetime import date

# ---------------------------------------------------------------------------
# EDIT ME
# ---------------------------------------------------------------------------
HER_NAME = "Olivia"
MY_NAME = "Joey"
START_DATE = date(2026, 6, 4)   # the day you became official
MET_LABEL = "February 2026"     # when you first met / first date
HER_EMOJI = "🇵🇹"
# ---------------------------------------------------------------------------

REASONS = [
    "You're the first person I want to tell things to.",
    "You listen properly. Not waiting-for-your-turn listening. Actual listening.",
    "You make ordinary days feel like something.",
    "You laugh at my jokes. Including the bad ones. Especially the bad ones.",
    "You're kind to people who can't do anything for you.",
    "You care about what you're studying, and it shows every time you talk about it.",
    "Time goes strange around you. Hours feel like minutes.",
    "You make plans with me in them.",
    "You're easy to be around. That sounds like a small thing. It isn't.",
    "Three months in and my phone lighting up with your name is still the best part of my day.",
    "I like who I am when I'm with you.",
    "You've never once made me feel like too much, or not enough.",
    "The more I get to know you, the more I like you. That keeps happening.",
    "You feel like the easiest decision I've ever made.",
]

MILESTONES = [
    (MET_LABEL, "The day we met", "Our first date. Everything else started here."),
    ("June 4, 2026", "Official", "The day we stopped calling it anything else."),
    ("Today", "Three months", "Three months of you. I'd like a lot more of them."),
]

# Values can use {days}, {months}, and {met}.
STATS = [
    ("Days together", "{days}", "since June 4"),
    ("Months official", "{months}", "and counting"),
    ("Known you since", "{met}", "our first date"),
    ("Places on our list", "6", "see the travel page"),
    ("Days I'd do again", "{days}", "all of them"),
]

DREAM_TRIPS = [
    ("Lisbon", "🇵🇹", "Where you're from. Top of the list, obviously."),
    ("Porto", "🍷", "The tiles, the bridge, the river. And the port wine."),
    ("Madeira", "⚽", "Beautiful island. Also Ronaldo's. Both good reasons."),
    ("Mexico City", "🌮", "For the food alone. We'd eat our way across it."),
    ("Puerto Rico", "🐰", "Beaches, and the right soundtrack for them."),
    ("Tulum", "🏝️", "Cenotes, warm water, nothing on the schedule."),
]

MENU = [
    ("Birria tacos", "The one with the dip."),
    ("Al pastor", "Never a bad call."),
    ("Elote", "Messy in the best way."),
    ("Churros", "Dessert, sorted."),
    ("Pastéis de nata", "Portugal's entry. Cinnamon on top."),
    ("Francesinha", "Porto's finest. On the list to try."),
]

QUIZ = [
    {
        "q": "How long have we been together today?",
        "options": ["3 weeks", "3 months", "3 years", "Time is a construct"],
        "answer": "3 months",
        "note": "Correct. Happy 3 months, {name}.",
    },
    {
        "q": "When did we first meet?",
        "options": ["February", "April", "June", "Feels like forever ago"],
        "answer": "February",
        "note": "February. Officially June, but February is where it started.",
    },
    {
        "q": "Who's the greatest of all time?",
        "options": ["Messi", "Cristiano Ronaldo", "No comment", "Do we have to"],
        "answer": "Cristiano Ronaldo",
        "note": "I know the correct answer. I've learned.",
    },
    {
        "q": "Best food on earth?",
        "options": ["Mexican", "Italian", "Portuguese", "Whatever's closest"],
        "answer": "Mexican",
        "note": "Tacos. Every time.",
    },
    {
        "q": "Which country am I most excited to see with you?",
        "options": ["Portugal", "Mexico", "Spain", "All of them"],
        "answer": "Portugal",
        "note": "I want to see where you're from.",
    },
    {
        "q": "Where are we going first?",
        "options": ["Lisbon", "Mexico City", "Puerto Rico", "Anywhere, as long as it's us"],
        "answer": "Anywhere, as long as it's us",
        "note": "Right answer. Though Lisbon is winning.",
    },
]

LETTER = """
{name},

Three months today. We actually met back in February, so it's been longer than
that really, but June 4th is the one we count.

Here's the honest version. You're the best part of my day, and you don't have to
do anything for that to be true. I like telling you things. I like hearing about
your day and your classes and whatever you're overthinking this week. I like that
everything is better when you're in it.

I don't have anything clever to add. Three months in, and I'm still glad every
single time my phone lights up and it's you.

Here's to a lot more of them.

— {me}
"""
