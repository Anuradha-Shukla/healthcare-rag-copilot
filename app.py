# import streamlit as st
# import time
# import PyPDF2
# from datetime import datetime

# st.set_page_config(
#     page_title="Healthcare RAG Copilot",
#     page_icon="🏥",
#     layout="wide"
# )

# # -----------------------------
# # STATE
# # -----------------------------
# if "page" not in st.session_state:
#     st.session_state.page = "signup"

# if "user" not in st.session_state:
#     st.session_state.user = None

# if "pdf_text" not in st.session_state:
#     st.session_state.pdf_text = ""

# if "history" not in st.session_state:
#     st.session_state.history = []


# # -----------------------------
# # UI STYLE
# # -----------------------------
# st.markdown("""
# <style>

# .stApp{
# background:
# radial-gradient(circle at top left,#152A52 0%,#08111E 45%,#030611 100%);
# }

# [data-testid="stHeader"]{
# background:transparent;
# }

# .block-container{
# padding-top:2rem;
# max-width:1350px;
# }

# .title{
# text-align:center;
# font-size:60px;
# font-weight:900;
# background:linear-gradient(90deg,#fff,#79AFFF,#63F2FF);
# -webkit-background-clip:text;
# -webkit-text-fill-color:transparent;
# }

# .card{
# background:rgba(255,255,255,.05);
# backdrop-filter:blur(18px);
# border:1px solid rgba(255,255,255,.10);
# padding:20px;
# border-radius:18px;
# color:white;
# box-shadow:0 0 30px rgba(0,150,255,.20);
# }

# .stButton button{
# width:100%;
# height:55px;
# border:none;
# border-radius:16px;
# font-size:16px;
# font-weight:700;
# background:linear-gradient(90deg,#0078FF,#00D8FF);
# color:white;
# }

# </style>
# """, unsafe_allow_html=True)


# # -----------------------------
# # PDF EXTRACTION
# # -----------------------------
# def extract_pdf_text(file):
#     reader = PyPDF2.PdfReader(file)
#     text = ""
#     for page in reader.pages:
#         if page.extract_text():
#             text += page.extract_text() + "\n"
#     return text


# # -----------------------------
# # CONDITION DETECTION
# # -----------------------------
# def detect_conditions(text):
#     text = text.lower()

#     conditions = {
#         "vitamin": ["vitamin", "b12", "d deficiency"],
#         "cholesterol": ["cholesterol", "ldl", "hdl"],
#         "diabetes": ["glucose", "sugar", "hba1c"],
#         "liver": ["liver", "sgpt", "sgot"],
#         "kidney": ["creatinine", "urea", "kidney"]
#     }

#     found = []

#     for c, keys in conditions.items():
#         for k in keys:
#             if k in text:
#                 found.append(c)
#                 break

#     return found


# # -----------------------------
# # HEALTH SCORE ENGINE
# # -----------------------------
# def calculate_score(text):

#     conditions = detect_conditions(text)

#     score = 100

#     weights = {
#         "vitamin": 10,
#         "cholesterol": 20,
#         "diabetes": 25,
#         "liver": 20,
#         "kidney": 25
#     }

#     breakdown = {k: "Normal" for k in weights}

#     for c in conditions:
#         score -= weights[c]
#         breakdown[c] = "Detected"

#     return max(score, 0), breakdown


# # -----------------------------
# # SMART SUGGESTIONS (NEW FEATURE)
# # -----------------------------
# def get_suggestions(text):
#     text = text.lower()

#     suggestions = []

#     if "vitamin" in text:
#         suggestions.append("🥗 Diet plan for Vitamin deficiency")
#         suggestions.append("💊 Foods rich in Vitamin D & B12")

#     if "cholesterol" in text:
#         suggestions.append("❤️ Cholesterol reduction tips")
#         suggestions.append("🥑 Heart-healthy diet plan")

#     if "diabetes" in text:
#         suggestions.append("🍬 Blood sugar control guide")
#         suggestions.append("🚶 Lifestyle tips for diabetes")

#     if not suggestions:
#         suggestions = [
#             "🩺 General health improvement tips",
#             "🥗 Balanced diet recommendations"
#         ]

#     return suggestions


# # -----------------------------
# # SIGNUP
# # -----------------------------
# def signup_page():

#     st.markdown("<div class='title'>Healthcare RAG Copilot</div>", unsafe_allow_html=True)

#     st.subheader("Create Account")

#     name = st.text_input("Full Name")
#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")

#     if st.button("Create Account"):
#         if name and email and password:
#             st.session_state.user = name
#             st.session_state.page = "dashboard"
#             st.rerun()
#         else:
#             st.error("Fill all fields")


# # -----------------------------
# # DASHBOARD
# # -----------------------------
# def dashboard_page():

#     st.markdown("<div class='title'>Dashboard</div>", unsafe_allow_html=True)

#     st.write(f"Welcome {st.session_state.user}")

#     # -----------------------------
#     # UPLOAD
#     # -----------------------------
#     uploaded = st.file_uploader("Upload Medical PDF", type=["pdf"])

#     if uploaded:
#         st.session_state.pdf_text = extract_pdf_text(uploaded)
#         st.success("PDF processed")

#         with st.expander("Extracted Text"):
#             st.write(st.session_state.pdf_text[:2000])


#     question = st.text_input("Ask Question")

#     # -----------------------------
#     # ANALYSIS
#     # -----------------------------
#     if st.button("Generate AI Report"):

#         if not st.session_state.pdf_text:
#             st.error("Upload PDF first")
#             return

#         with st.spinner("Analyzing..."):
#             time.sleep(2)

#         text = st.session_state.pdf_text

#         score, breakdown = calculate_score(text)

#         output = f"""
# 🧠 AI HEALTH REPORT

# Score: {score}/100

# Detected Conditions:
# {breakdown}

# Recommendation:
# • Maintain healthy lifestyle
# • Regular checkups advised
# """

#         st.success(output)

#         st.metric("Score", f"{score}/100")
#         st.progress(score)

#         # -----------------------------
#         # SMART SUGGESTIONS BOX (ADDED HERE)
#         # -----------------------------
#         st.subheader("💡 Smart Suggestions")

#         suggestions = get_suggestions(text)

#         for s in suggestions:
#             if st.button(s):
#                 st.info(f"Selected: {s}")
#                 st.write("This can be connected to future AI chatbot / recommendation engine.")

#         # -----------------------------
#         # DOWNLOAD
#         # -----------------------------
#         st.download_button(
#             "Download Report",
#             data=output,
#             file_name="health_report.txt"
#         )


# # -----------------------------
# # ROUTER
# # -----------------------------
# if st.session_state.page == "signup":
#     signup_page()
# else:
#     dashboard_page()



import streamlit as st
import time
import PyPDF2

st.set_page_config(
    page_title="Healthcare RAG Copilot",
    page_icon="🏥",
    layout="wide"
)

# =============================
# SESSION STATE
# =============================

if "page" not in st.session_state:
    st.session_state.page = "signup"

if "user" not in st.session_state:
    st.session_state.user = ""

if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""

# =============================
# STYLING
# =============================

st.markdown("""
<style>

.stApp{
background:
linear-gradient(
135deg,
#06142E,
#0E2452,
#183B72
);
}

.title{
text-align:center;
font-size:56px;
font-weight:900;
color:white;
}

.card{
background:
rgba(255,255,255,.08);

padding:25px;

border-radius:18px;

text-align:center;

color:white;
}

.stButton button{

width:100%;

height:55px;

border-radius:14px;

background:
linear-gradient(
90deg,
#0088FF,
#00D8FF
);

color:white;

font-weight:700;

}

</style>
""", unsafe_allow_html=True)

# =============================
# PDF EXTRACTION
# =============================

def extract_pdf_text(file):

    reader = PyPDF2.PdfReader(file)

    text=""

    for page in reader.pages:

        content = page.extract_text()

        if content:

            text += content + "\n"

    return text


# =============================
# DOCUMENT TYPE DETECTOR
# =============================

def detect_document_type(text):

    text=text.lower()

    research_words=[

        "review article",
        "doi",
        "genetics",
        "variant",
        "mendelian",
        "journal",
        "authors",
        "sequence variant",
        "laboratory medicine"

    ]

    for word in research_words:

        if word in text:

            return "research"

    return "medical"


# =============================
# CONDITIONS
# =============================

def detect_conditions(text):

    text=text.lower()

    rules={

        "Vitamin":
        [
            "vitamin",
            "vitamin d",
            "b12"
        ],

        "Cholesterol":
        [
            "cholesterol",
            "ldl",
            "hdl"
        ],

        "Diabetes":
        [
            "glucose",
            "hba1c",
            "blood sugar"
        ],

        "Liver":
        [
            "liver",
            "sgot",
            "sgpt"
        ],

        "Kidney":
        [
            "creatinine",
            "urea"
        ]
    }

    found=[]

    for name,keys in rules.items():

        for key in keys:

            if key in text:

                found.append(name)

                break

    return found


# =============================
# HEALTH SCORE
# =============================

def calculate_score(text):

    detected=detect_conditions(text)

    score=100

    deductions={

        "Vitamin":10,

        "Cholesterol":20,

        "Diabetes":25,

        "Liver":20,

        "Kidney":25
    }

    breakdown={}

    for k in deductions:

        breakdown[k]="Normal"

    for d in detected:

        score -= deductions[d]

        breakdown[d]="Detected"

    return max(score,0), breakdown


# =============================
# RECOMMENDATIONS
# =============================

def get_recommendations(text):

    text=text.lower()

    tips=[]

    if "vitamin" in text:

        tips.append(
            "🥗 Improve Vitamin Intake"
        )

    if "cholesterol" in text:

        tips.append(
            "❤️ Reduce processed food"
        )

    if "glucose" in text:

        tips.append(
            "🚶 Daily exercise"
        )

    if not tips:

        tips=[

            "🩺 Regular health checkups",

            "🥗 Balanced diet"

        ]

    return tips


# =============================
# SIGNUP PAGE
# =============================

def signup_page():

    st.markdown(
        "<div class='title'>Healthcare RAG Copilot</div>",
        unsafe_allow_html=True
    )

    st.subheader(
        "Create Account"
    )

    name=st.text_input(
        "Full Name"
    )

    email=st.text_input(
        "Email"
    )

    password=st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "Create Account"
    ):

        if name and email and password:

            st.session_state.user=name

            st.session_state.page="dashboard"

            st.rerun()

        else:

            st.error(
                "Fill all fields"
            )


# =============================
# DASHBOARD
# =============================

def dashboard():

    st.markdown(
        "<div class='title'>Dashboard</div>",
        unsafe_allow_html=True
    )

    st.write(
        f"Welcome {st.session_state.user}"
    )

    a,b,c=st.columns(3)

    with a:

        st.markdown(
            "<div class='card'>📄<h2>24</h2>Reports</div>",
            unsafe_allow_html=True
        )

    with b:

        st.markdown(
            "<div class='card'>🧠<h2>132</h2>Insights</div>",
            unsafe_allow_html=True
        )

    with c:

        st.markdown(
            "<div class='card'>⭐<h2>87</h2>Health Score</div>",
            unsafe_allow_html=True
        )

    uploaded=st.file_uploader(
        "Upload Healthcare PDF",
        type=["pdf"]
    )

    if uploaded:

        st.session_state.pdf_text=extract_pdf_text(
            uploaded
        )

        st.success(
            "PDF Processed"
        )

    question=st.text_input(
        "Ask Question"
    )

    if st.button(
        "Generate AI Report"
    ):

        if not st.session_state.pdf_text:

            st.error(
                "Upload PDF first"
            )

            return

        with st.spinner(
            "Analyzing..."
        ):

            time.sleep(2)

        text=st.session_state.pdf_text

        doc_type=detect_document_type(
            text
        )

        # RESEARCH PAPER
        if doc_type=="research":

            st.warning(
                "Research Paper Detected"
            )

            st.success("""

📄 REPORT SUMMARY

Type:
Research Article

Summary:
This document discusses genetic variant interpretation.

No patient conditions detected.

Upload healthcare report for diagnosis.
""")

            return

        # MEDICAL REPORT

        score, breakdown=calculate_score(
            text
        )

        st.success(

f"""

Detected Conditions:
{breakdown}

Recommendation:
• Maintain healthy lifestyle
• Regular checkups advised

"""
)

        st.metric(
            "AI Health Score",
            f"{score}/100"
        )

        st.progress(
            score
        )

        st.subheader(
            "AI Suggestions"
        )

        for item in get_recommendations(text):

            st.info(item)

        st.download_button(

            "Download Report",

            data=str(breakdown),

            file_name="health_report.txt"
        )


# =============================
# ROUTER
# =============================

if st.session_state.page=="signup":

    signup_page()

else:

    dashboard()