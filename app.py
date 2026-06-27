import random
import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(page_title="Rock Paper Scissors", page_icon="✊", layout="centered")

# ── Inject CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Space+Mono:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
    background-color: #0d0d0d;
    color: #f0f0f0;
}

.stApp {
    background: #0d0d0d;
}

h1, h2, h3 {
    font-family: 'Space Mono', monospace;
    letter-spacing: -0.03em;
}

/* Title */
.title-block {
    text-align: center;
    padding: 2rem 0 1rem 0;
}
.title-block h1 {
    font-size: 2.6rem;
    color: #ffffff;
    margin-bottom: 0.2rem;
}
.title-block p {
    color: #888;
    font-size: 1rem;
    margin: 0;
}

/* Score board */
.score-board {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    margin: 1.5rem 0;
}
.score-card {
    background: #1a1a1a;
    border: 1px solid #2a2a2a;
    border-radius: 12px;
    padding: 1rem 1.6rem;
    text-align: center;
    min-width: 80px;
}
.score-card .label {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #666;
    margin-bottom: 0.3rem;
}
.score-card .value {
    font-family: 'Space Mono', monospace;
    font-size: 2rem;
    font-weight: 700;
    line-height: 1;
}
.wins   .value { color: #4ade80; }
.losses .value { color: #f87171; }
.ties   .value { color: #facc15; }

/* Choice buttons */
.choice-row {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin: 1.5rem 0;
}

/* Result banner */
.result-banner {
    text-align: center;
    padding: 1.2rem;
    border-radius: 14px;
    margin: 1rem 0;
    font-family: 'Space Mono', monospace;
    font-size: 1.4rem;
    font-weight: 700;
    letter-spacing: -0.02em;
}
.result-win  { background: #14532d; color: #4ade80; border: 1px solid #4ade80; }
.result-lose { background: #450a0a; color: #f87171; border: 1px solid #f87171; }
.result-tie  { background: #422006; color: #facc15; border: 1px solid #facc15; }

/* Battle display */
.battle {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 2rem;
    font-size: 5rem;
    margin: 1rem 0;
    text-align: center;
}
.battle-label {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #555;
    text-align: center;
}
.vs-badge {
    font-family: 'Space Mono', monospace;
    font-size: 1rem;
    color: #444;
    padding: 0.4rem 0.8rem;
    border: 1px solid #333;
    border-radius: 6px;
}

/* Reset button */
div[data-testid="stButton"] button {
    background: #1a1a1a;
    color: #aaa;
    border: 1px solid #333;
    border-radius: 8px;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.85rem;
    padding: 0.4rem 1rem;
    transition: all 0.15s;
}
div[data-testid="stButton"] button:hover {
    background: #252525;
    color: #fff;
    border-color: #555;
}

/* Choice buttons override */
.choice-btn button {
    background: #1a1a1a !important;
    border: 2px solid #333 !important;
    border-radius: 16px !important;
    font-size: 3.5rem !important;
    padding: 1rem 1.4rem !important;
    transition: all 0.15s !important;
    line-height: 1 !important;
}
.choice-btn button:hover {
    border-color: #fff !important;
    background: #222 !important;
    transform: scale(1.08);
}

hr {
    border-color: #222;
    margin: 1.5rem 0;
}
</style>
""", unsafe_allow_html=True)

# ── Session state init ──────────────────────────────────────────────────────────
for key, default in [("wins", 0), ("losses", 0), ("ties", 0),
                     ("last_player", None), ("last_computer", None), ("last_result", None)]:
    if key not in st.session_state:
        st.session_state[key] = default

# ── Core game logic (your original logic, unchanged) ───────────────────────────
CHOICES = ["rock", "paper", "scissors"]
EMOJI   = {"rock": "✊", "paper": "🖐️", "scissors": "✌️"}

def play(player: str) -> str:
    computer = random.choice(CHOICES)
    if player == computer:
        st.session_state.ties += 1
        result = "tie"
    elif player == "rock":
        if computer == "scissors":
            st.session_state.wins += 1;  result = "win"
        else:
            st.session_state.losses += 1; result = "lose"
    elif player == "scissors":
        if computer == "rock":
            st.session_state.losses += 1; result = "lose"
        else:
            st.session_state.wins += 1;  result = "win"
    elif player == "paper":
        if computer == "rock":
            st.session_state.wins += 1;  result = "win"
        else:
            st.session_state.losses += 1; result = "lose"
    st.session_state.last_player   = player
    st.session_state.last_computer = computer
    st.session_state.last_result   = result

# ── UI ─────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="title-block">
    <h1>✊ 🖐️ ✌️</h1>
    <h1>Rock Paper Scissors</h1>
    <p>Pick your move — the machine never blinks.</p>
</div>
""", unsafe_allow_html=True)

# Score board
st.markdown(f"""
<div class="score-board">
    <div class="score-card wins">
        <div class="label">Wins</div>
        <div class="value">{st.session_state.wins}</div>
    </div>
    <div class="score-card losses">
        <div class="label">Losses</div>
        <div class="value">{st.session_state.losses}</div>
    </div>
    <div class="score-card ties">
        <div class="label">Ties</div>
        <div class="value">{st.session_state.ties}</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Choice buttons
st.markdown("<p style='text-align:center;color:#666;font-size:0.85rem;letter-spacing:0.08em;text-transform:uppercase;'>Your move</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="choice-btn">', unsafe_allow_html=True)
    if st.button("✊\n\nRock", use_container_width=True):
        play("rock")
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="choice-btn">', unsafe_allow_html=True)
    if st.button("🖐️\n\nPaper", use_container_width=True):
        play("paper")
    st.markdown('</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="choice-btn">', unsafe_allow_html=True)
    if st.button("✌️\n\nScissors", use_container_width=True):
        play("scissors")
    st.markdown('</div>', unsafe_allow_html=True)

# Result display
if st.session_state.last_result:
    st.markdown("<hr>", unsafe_allow_html=True)

    p = st.session_state.last_player
    c = st.session_state.last_computer
    r = st.session_state.last_result

    # Battle emojis
    st.markdown(f"""
    <div>
        <div style="display:flex;justify-content:center;gap:3rem;margin-bottom:0.3rem;">
            <div class="battle-label">You</div>
            <div class="battle-label"></div>
            <div class="battle-label">Computer</div>
        </div>
        <div class="battle">
            <span>{EMOJI[p]}</span>
            <span class="vs-badge">VS</span>
            <span>{EMOJI[c]}</span>
        </div>
        <div style="display:flex;justify-content:center;gap:3rem;margin-top:0.3rem;">
            <div class="battle-label">{p.capitalize()}</div>
            <div class="battle-label"></div>
            <div class="battle-label">{c.capitalize()}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Result banner
    css_class = {"win": "result-win", "lose": "result-lose", "tie": "result-tie"}[r]
    text      = {"win": "🏆 You Won!", "lose": "💀 You Lost!", "tie": "🤝 It's a Tie!"}[r]
    st.markdown(f'<div class="result-banner {css_class}">{text}</div>', unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

# Reset button
col_a, col_b, col_c = st.columns([2, 1, 2])
with col_b:
    if st.button("Reset Score", use_container_width=True):
        for k in ["wins", "losses", "ties", "last_player", "last_computer", "last_result"]:
            st.session_state[k] = 0 if k in ["wins","losses","ties"] else None
        st.rerun()
