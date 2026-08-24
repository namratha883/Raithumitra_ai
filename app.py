import streamlit as st
from google import genai
from pathlib import Path

# ============================================================
# RAITHUMITRA AI — FINAL MERGED PROFESSIONAL UI
# Keeps the original project sections/functionality while
# replacing the prototype layout with a clean professional UI.
# ============================================================

st.set_page_config(
    page_title="రైతుమిత్ర AI",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).parent
HERO_IMAGE = BASE_DIR / "assets" / "farmer_hero.jpg"

# ============================================================
# PROFESSIONAL STYLES
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Telugu:wght@400;500;600;700;800&display=swap');

.stApp {
    background: #f7faf7;
}

.block-container {
    max-width: 1420px;
    padding: 22px 34px 55px 34px;
}

#MainMenu, footer {
    visibility: hidden;
}

[data-testid="stHeader"] {
    background: transparent;
}

html, body, [class*="css"], button, textarea {
    font-family: "Noto Sans Telugu", "Nirmala UI", sans-serif !important;
}

h1, h2, h3 {
    color: #17632d !important;
    font-family: "Noto Sans Telugu", "Nirmala UI", sans-serif !important;
}

p {
    color: #66736a !important;
    font-size: 16px !important;
    line-height: 1.75 !important;
}

/* Header */
.header-card {
    background: #ffffff;
    border: 1px solid #dfe9df;
    border-radius: 24px;
    padding: 20px 28px;
    box-shadow: 0 7px 24px rgba(25,70,35,.055);
    margin-bottom: 22px;
}

.brand {
    color: #17632d;
    font-size: 31px;
    font-weight: 800;
    line-height: 1.1;
}

.brand-sub {
    color: #7a877e;
    font-size: 14px;
    margin-top: 6px;
}

.nav-pills {
    text-align: right;
    padding-top: 12px;
}

.nav-pill {
    display: inline-block;
    color: #205f30;
    background: #f3faf3;
    border: 1px solid #cfe3d1;
    border-radius: 999px;
    padding: 9px 14px;
    margin-left: 6px;
    font-size: 12px;
    font-weight: 700;

    cursor: pointer;

    transition: all 0.25s ease;
    box-shadow: 0 2px 7px rgba(47, 127, 62, 0.06);
}

/* Glowing hover effect */
.nav-pill:hover {
    background: #dff3e1;
    color: #145c28;
    border-color: #8bc995;

    transform: translateY(-2px);

    box-shadow:
        0 0 8px rgba(76, 175, 80, 0.25),
        0 5px 15px rgba(47, 127, 62, 0.15);
}
.hero-card .stButton > button {
    background: #dff3e3 !important;
    color: #145c28 !important;
    border: 1px solid #a8d5ae !important;
    border-radius: 12px !important;
    font-weight: 750 !important;
    box-shadow: 0 4px 12px rgba(47,127,62,.10) !important;
    transition: all 0.25s ease !important;
}

.hero-card .stButton > button:hover {
    background: #ccebd1 !important;
    color: #104d22 !important;
    border-color: #7fc48a !important;
    transform: translateY(-2px) !important;
    box-shadow:
        0 0 12px rgba(76,175,80,.30),
        0 7px 18px rgba(47,127,62,.15) !important;
}

/* Hero */
.hero-card {
    background: linear-gradient(135deg, #eef8ee 0%, #fbfdfb 58%, #edf7ed 100%);
    border: 1px solid #dce9dc;
    border-radius: 27px;
    overflow: hidden;
    box-shadow: 0 10px 32px rgba(30,75,38,.055);
    padding: 38px 42px 36px 42px;
}

.badge {
    display: inline-block;
    background: #dff2df;
    color: #205f30;
    border-radius: 999px;
    padding: 9px 15px;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: .2px;
}

.hero-title {
    color: #17632d;
    font-size: 51px;
    font-weight: 800;
    line-height: 1.28;
    margin: 24px 0 15px 0;
}

.hero-title span {
    color: #2f8141;
}

.hero-text {
    color: #68756c;
    font-size: 16px;
    line-height: 1.9;
    max-width: 620px;
    margin-bottom: 18px;
}

.checks {
    display: flex;
    flex-wrap: wrap;
    gap: 9px;
    margin: 15px 0 23px 0;
}

.check {
    background: #ffffff;
    border: 1px solid #dce7dc;
    border-radius: 999px;
    color: #2d6638;
    padding: 8px 13px;
    font-size: 12px;
    font-weight: 650;
}

.hero-image {
    border-radius: 20px;
    overflow: hidden;
    border: 1px solid #d6e4d6;
    box-shadow: 0 7px 20px rgba(25,70,35,.08);
}

.hero-image img {
    width: 100%;
    height: 390px;
    object-fit: cover;
}

/* ================= BUTTON STYLE ================= */

div.stButton > button {
    background: #e8f5e9 !important;
    color: #195c2b !important;
    border: 1px solid #b9dcbc !important;
    border-radius: 11px !important;
    min-height: 43px !important;
    font-weight: 750 !important;

    transition: all 0.25s ease !important;

    box-shadow:
        0 3px 10px rgba(47, 127, 62, 0.08) !important;
}

div.stButton > button:hover {
    background: #d4efd7 !important;
    color: #124d22 !important;
    border-color: #7fc88a !important;

    box-shadow:
        0 0 12px rgba(76, 175, 80, 0.30),
        0 6px 18px rgba(47, 127, 62, 0.14) !important;

    transform: translateY(-2px) !important;
}

div.stButton > button:active {
    transform: translateY(0px) !important;
}

div.stButton > button:focus {
    background: #dff2e1 !important;
    color: #164f26 !important;
    border-color: #6fbd7b !important;
    outline: none !important;
}



/* Section headings */
.section-title {
    color: #17632d;
    font-size: 28px;
    font-weight: 800;
    margin: 30px 0 4px 0;
}

.section-sub {
    color: #7b877e;
    font-size: 13px;
    margin-bottom: 17px;
}

/* Cards */
[data-testid="stVerticalBlockBorderWrapper"] {
    background: #ffffff !important;
    border: 1px solid #dfe9df !important;
    border-radius: 18px !important;
    box-shadow: 0 5px 18px rgba(25,70,35,.045) !important;
}

.feature-icon {
    font-size: 25px;
    margin-bottom: 5px;
}

.feature-title {
    color: #215f30;
    font-size: 18px;
    font-weight: 750;
}

.feature-text {
    color: #758078;
    font-size: 13px;
    line-height: 1.7;
    margin-top: 5px;
}

/* Ask box */
.ask-box {
    background: linear-gradient(135deg,#eef8ed,#ffffff);
    border: 1px solid #dbe8dc;
    border-radius: 22px;
    padding: 25px 28px 20px 28px;
    margin-top: 25px;
}

.ask-title {
    color: #17632d;
    font-size: 25px;
    font-weight: 800;
}

.ask-sub {
    color: #748078;
    font-size: 13px;
    margin-top: 4px;
}

textarea {
    background: #ffffff !important;
    color: #222222 !important;
    border: 1px solid #d3e0d3 !important;
    border-radius: 12px !important;
    font-size: 15px !important;
}

[data-testid="stImage"] img {
    border-radius: 17px;
    border: 1px solid #dfe8df;
}

hr {
    border: none !important;
    border-top: 1px solid #dfe8df !important;
    margin: 30px 0 !important;
}

.footer {
    text-align: center;
    color: #849087;
    font-size: 12px;
    padding-top: 4px;
}

@media (max-width: 900px) {
    .block-container {
        padding: 16px 18px 40px 18px;
    }
    .header-card {
        padding: 18px;
    }
    .nav-pills {
        text-align: left;
        margin-top: 12px;
    }
    .nav-pill {
        margin: 3px 4px 3px 0;
    }
    .hero-card {
        padding: 28px 23px;
    }
    .hero-title {
        font-size: 38px;
    }
    .hero-image img {
        height: 300px;
    }
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# HEADER
# ============================================================
h1, h2 = st.columns([1.25, 1], gap="large")

with h1:
    st.markdown(
        """
        <div class="header-card">
            <div class="brand">🌾 రైతుమిత్ర AI</div>
            <div class="brand-sub">రైతులకు అండగా • వ్యవసాయానికి మిత్రుడిగా</div>
            <div class="brand-sub">పంటలు • తెగుళ్లు • నీటి నిర్వహణ • AI సహాయం</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with h2:
    st.markdown(
        """
        <div class="header-card">
            <div class="nav-pills">
                <span class="nav-pill">⌂ హోమ్</span>
                <span class="nav-pill">◈ సేవలు</span>
                <span class="nav-pill">? AI సహాయం</span>
                <span class="nav-pill">☎ సంప్రదించండి</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# HERO — native Streamlit columns, so HTML cannot accidentally
# appear as source code in the UI.
# ============================================================
left, right = st.columns([1.02, 0.98], gap="large")

with left:
    st.markdown('<div class="hero-card">', unsafe_allow_html=True)
    st.markdown(
        '<div class="badge">🌱 &nbsp; SMART FARMING ASSISTANT</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="hero-title">మీ వ్యవసాయానికి<br><span>AI మిత్రుడు</span></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="hero-text">
        మీ పంటలు, తెగుళ్లు, పురుగులు, నీటి నిర్వహణ మరియు ఇతర
        వ్యవసాయ సమస్యల గురించి సులభమైన తెలుగులో సహాయం పొందండి.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="checks">
            <span class="check">✓ సులభమైన సమాచారం</span>
            <span class="check">✓ వేగవంతమైన సహాయం</span>
            <span class="check">✓ రైతు కేంద్రిత సేవలు</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("✨ ఇప్పుడే ప్రశ్న అడగండి", key="hero_ask"):
        st.session_state["scroll_to_ask"] = True
    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown('<div class="hero-card">', unsafe_allow_html=True)
    if HERO_IMAGE.exists():
        st.markdown('<div class="hero-image">', unsafe_allow_html=True)
        st.image(HERO_IMAGE, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("వ్యవసాయ చిత్రం అందుబాటులో లేదు.")
    st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# FEATURES — original four service areas retained
# ============================================================
st.markdown(
    """
    <div class="section-title">🌿 రైతుమిత్ర సేవలు</div>
    <div class="section-sub">రైతుల కోసం ముఖ్యమైన వ్యవసాయ సహాయ విభాగాలు</div>
    """,
    unsafe_allow_html=True,
)

f1, f2, f3, f4 = st.columns(4, gap="medium")

features = [
    ("🌱", "పంట సమాచారం", "పంటల సాగు మరియు సంరక్షణకు సంబంధించిన ఉపయోగకరమైన సమాచారం."),
    ("🐛", "తెగుళ్లు", "పంటలకు వచ్చే తెగుళ్లు మరియు పురుగుల గురించి సహాయం."),
    ("💧", "నీటి నిర్వహణ", "సాగునీటి వినియోగాన్ని సమర్థంగా నిర్వహించేందుకు సూచనలు."),
    ("📚", "వ్యవసాయ సమాచారం", "రైతులకు అవసరమైన వ్యవసాయ సమాచారాన్ని ఒకే చోట పొందండి."),
]

for col, (icon, title, text) in zip((f1, f2, f3, f4), features):
    with col:
        with st.container(border=True):
            st.markdown(f'<div class="feature-icon">{icon}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="feature-title">{title}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="feature-text">{text}</div>', unsafe_allow_html=True)

# ============================================================
# ASK RAITHUMITRA — original controls retained
# ============================================================
st.markdown('<div id="ask-raithumitra"></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="ask-box">
        <div class="ask-title">💬 రైతుమిత్రను అడగండి</div>
        <div class="ask-sub">మీ పంట సమస్యను తెలుగులో వివరించండి.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

question = st.text_area(
    "మీ ప్రశ్న",
    placeholder="ఉదాహరణ: వరి పంట ఆకులు పసుపు రంగులోకి మారుతున్నాయి. ఏం చేయాలి?",
    height=130,
    label_visibility="collapsed",
)

q1, q2, q3 = st.columns([1, 1, 2], gap="small")

with q1:
    st.button("🎤 వాయిస్", key="voice_btn")

with q2:
    st.button("📷 ఫోటో", key="photo_btn")

with q3:
    ask = st.button("✨ సమాధానం పొందండి", key="ask_btn")

# ============================================================
# RESPONSE — original behavior retained
# ============================================================
if ask:
    if question.strip():
        with st.container(border=True):
            st.markdown("## 🌾 రైతుమిత్ర సమాధానం")
            st.success("మీ ప్రశ్నను రైతుమిత్ర స్వీకరించింది.")
            st.write(
                "మీ ప్రశ్నకు AI ఆధారంగా వ్యవసాయ సంబంధిత సమాధానం అందించే విధానం "
                "తదుపరి దశలో అనుసంధానం చేయబడుతుంది."
            )
    else:
        st.warning("⚠️ దయచేసి ముందుగా మీ వ్యవసాయ ప్రశ్నను నమోదు చేయండి.")

# ============================================================
# FARMING GALLERY — original section retained
# ============================================================
st.markdown(
    """
    <div class="section-title">🌾 మన వ్యవసాయం</div>
    <div class="section-sub">వ్యవసాయం మరియు రైతుల జీవితాన్ని ప్రతిబింబించే దృశ్యాలు</div>
    """,
    unsafe_allow_html=True,
)

image1, image2, image3 = st.columns(3, gap="medium")

gallery = [
    (
        "https://images.unsplash.com/photo-1499529112087-3cb3b73cec95?auto=format&fit=crop&w=900&q=85",
        "🌱 పచ్చని పంట పొలాలు",
    ),
    (
        "https://images.unsplash.com/photo-1625246333195-78d9c38ad449?auto=format&fit=crop&w=900&q=85",
        "👨‍🌾 రైతు మరియు వ్యవసాయం",
    ),
    (
        "https://images.unsplash.com/photo-1464226184884-fa280b87c399?auto=format&fit=crop&w=900&q=85",
        "🌾 ఆధునిక వ్యవసాయం",
    ),
]

for col, (url, caption) in zip((image1, image2, image3), gallery):
    with col:
        st.image(url, use_container_width=True)
        st.caption(caption)

# ============================================================
# FOOTER
# ============================================================
st.divider()
st.markdown(
    '<div class="footer">🌾 రైతుమిత్ర AI • రైతు అభివృద్ధి కోసం సాంకేతికత</div>',
    unsafe_allow_html=True,
)
