import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="రైతుమిత్ర AI",
    page_icon="🌾",
    layout="wide"
)

# --------------------------------------------------
# CSS
# --------------------------------------------------


st.markdown("""
<style>

    /* ================= PAGE ================= */

    .stApp {
        background-color: #f6faf5;
    }

    .block-container {
    max-width: 1200px;
    padding-top: 55px;
    padding-bottom: 50px;
    } 


    /* ================= TEXT ================= */

    p {
        color: #344238 !important;
        font-size: 17px !important;
        line-height: 1.6 !important;
    }

    h1 {
    color: #176b2c !important;
    font-size: 48px !important;
    text-align: center !important;
    font-weight: 800 !important;
    line-height: 1.2 !important;
    margin-top: 10px !important;
    margin-bottom: 8px !important;
} 
    h2 {
        color: #176b2c !important;
        font-size: 28px !important;
        font-weight: 700 !important;
    }

    h3 {
        color: #245c2c !important;
        font-size: 20px !important;
        font-weight: 700 !important;
    }


    /* ================= ALL BUTTONS ================= */

    /* Normal */
    .stButton > button,
    button[kind="primary"],
    button[kind="secondary"] {
        background-color: #4caf50 !important;
        color: white !important;
        border: 1px solid #4caf50 !important;
        border-radius: 11px !important;
        min-height: 50px !important;
        font-size: 17px !important;
        font-weight: 600 !important;
        box-shadow: none !important;
    }

    /* Hover */
    .stButton > button:hover,
    button[kind="primary"]:hover,
    button[kind="secondary"]:hover {
        background-color: #4caf50 !important;
        color: white !important;
        border-color: #4caf50 !important;
        box-shadow: 0 3px 10px rgba(76, 175, 80, 0.25) !important;
    }

    /* Focus */
    .stButton > button:focus,
    .stButton > button:focus-visible {
        background-color: #4caf50 !important;
        color: white !important;
        border-color: #4caf50 !important;
        outline: none !important;
        box-shadow: 0 0 0 2px rgba(76, 175, 80, 0.25) !important;
    }

    /* Active / clicking */
    .stButton > button:active {
        background-color: #4caf50 !important;
        color: white !important;
        border-color: #4caf50 !important;
    }


    /* ================= TEXT BOX ================= */

    textarea {
        background-color: white !important;
        color: #222222 !important;
        border: 2px solid #d2dfd2 !important;
        border-radius: 12px !important;
        font-size: 17px !important;
    }

    textarea:focus {
        border: 2px solid #4caf50 !important;
        box-shadow: 0 0 0 2px rgba(76, 175, 80, 0.12) !important;
    }

    textarea::placeholder {
        color: #7b867d !important;
        opacity: 1 !important;
    }


    /* ================= CARDS ================= */

    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: white !important;
        border: 1px solid #dfe8df !important;
        border-radius: 18px !important;
        box-shadow: 0 4px 16px rgba(0,0,0,0.04) !important;
    }


    /* ================= PHOTOS ================= */

    [data-testid="stImage"] img {
        opacity: 0.82;
        filter: brightness(1.08) saturate(0.85);
        border-radius: 16px;
    }


    /* ================= SUCCESS MESSAGE ================= */

    [data-testid="stAlert"] {
        border-radius: 12px !important;
    }


    /* ================= DIVIDERS ================= */

    hr {
        border: none !important;
        border-top: 1px solid #dce6dc !important;
        margin: 25px 0 !important;
    }

</style>

""", unsafe_allow_html=True)


# ==================================================
# HEADER
# ==================================================

header1, header2 = st.columns([5, 1])

with header1:

    st.markdown(
        "### 🌾 రైతుమిత్ర AI"
    )

    st.markdown(
        '<div class="header-subtitle">'
        'రైతులకు అండగా • వ్యవసాయానికి మిత్రుడిగా'
        '</div>',
        unsafe_allow_html=True
    )

with header2:

    st.write("")

    st.button("🎧 సహాయం")


st.divider()


# ==================================================
# HERO SECTION
# ==================================================

hero1, hero2 = st.columns([1.05, 1])

with hero1:

    st.markdown("## 🌱 మీ వ్యవసాయానికి AI మిత్రుడు")

    st.write(
        "మీ పంటలు, తెగుళ్లు, పురుగులు, నీటి నిర్వహణ "
        "మరియు ఇతర వ్యవసాయ సమస్యల గురించి "
        "సులభమైన తెలుగులో సహాయం పొందండి."
    )

    st.success(
        "🛡️ సులభమైన సమాచారం  •  ⚡ వేగవంతమైన సహాయం"
    )

    st.write("")

    st.button("✨ ఇప్పుడే ప్రశ్న అడగండి")


with hero2:

    st.image(
        "https://images.unsplash.com/photo-1500382017468-9049fed747ef"
        "?auto=format&fit=crop&w=1200&q=85",
        use_container_width=True
    )


# ==================================================
# FEATURES
# ==================================================

st.write("")
st.markdown("## 🌿 రైతుమిత్ర సేవలు")

f1, f2, f3, f4 = st.columns(4)

with f1:

    with st.container(border=True):

        st.markdown("### 🌱")

        st.markdown("### పంట సమాచారం")

        st.write(
            "పంటల సాగు మరియు సంరక్షణకు సంబంధించిన సమాచారం."
        )


with f2:

    with st.container(border=True):

        st.markdown("### 🐛")

        st.markdown("### తెగుళ్లు")

        st.write(
            "పంటలకు వచ్చే తెగుళ్లు మరియు పురుగుల గురించి సహాయం."
        )


with f3:

    with st.container(border=True):

        st.markdown("### 💧")

        st.markdown("### నీటి నిర్వహణ")

        st.write(
            "సాగునీటి వినియోగంపై ఉపయోగకరమైన సూచనలు."
        )


with f4:

    with st.container(border=True):

        st.markdown("### 📚")

        st.markdown("### వ్యవసాయ సమాచారం")

        st.write(
            "రైతులకు అవసరమైన వ్యవసాయ సమాచారాన్ని పొందండి."
        )


# ==================================================
# ASK RAITHUMITRA
# ==================================================

st.write("")

with st.container(border=True):

    st.markdown("## 💬 రైతుమిత్రను అడగండి")

    st.write(
        "మీ పంట సమస్యను క్రింద వివరించండి."
    )

    question = st.text_area(
        "మీ ప్రశ్న",
        placeholder="ఉదాహరణ: వరి పంట ఆకులు పసుపు రంగులోకి మారుతున్నాయి. ఏం చేయాలి?",
        height=150
    )

    st.write("")

    q1, q2, q3 = st.columns([1, 1, 2])

    with q1:
        st.button("🎤 వాయిస్")

    with q2:
        st.button("📷 ఫోటో")

    with q3:

        ask = st.button(
            "✨ సమాధానం పొందండి"
        )


# ==================================================
# RESPONSE
# ==================================================

if "ask" in locals() and ask:

    if question.strip():

        st.write("")

        with st.container(border=True):

            st.markdown("## 🌾 రైతుమిత్ర సమాధానం")

            st.success(
                "మీ ప్రశ్నను రైతుమిత్ర స్వీకరించింది."
            )

            st.write(
                "మీ ప్రశ్నకు AI ఆధారంగా వ్యవసాయ సంబంధిత "
                "సమాధానం అందించే విధానం తదుపరి దశలో "
                "అనుసంధానం చేయబడుతుంది."
            )

    else:

        st.warning(
            "⚠️ దయచేసి ముందుగా మీ వ్యవసాయ ప్రశ్నను నమోదు చేయండి."
        )


# ==================================================
# FARMING SECTION
# ==================================================

st.write("")
st.markdown("## 🌾 మన వ్యవసాయం")

image1, image2, image3 = st.columns(3)

with image1:

    st.image(
        "https://images.unsplash.com/photo-1499529112087-3cb3b73cec95"
        "?auto=format&fit=crop&w=800&q=80",
        use_container_width=True
    )

    st.caption("🌱 పచ్చని పంట పొలాలు")


with image2:

    st.image(
        "https://images.unsplash.com/photo-1625246333195-78d9c38ad449"
        "?auto=format&fit=crop&w=800&q=80",
        use_container_width=True
    )

    st.caption("👨‍🌾 రైతు మరియు వ్యవసాయం")


with image3:

    st.image(
        "https://images.unsplash.com/photo-1464226184884-fa280b87c399"
        "?auto=format&fit=crop&w=800&q=80",
        use_container_width=True
    )

    st.caption("🌾 ఆధునిక వ్యవసాయం")


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "🌾 రైతుమిత్ర AI  •  రైతు అభివృద్ధి కోసం సాంకేతికత"
)