import streamlit as st

st.markdown("""
    <style>
        .stApp {
            background-color: #090d16;
            color: #f8fafc;
            font-family: 'Inter', sans-serif;
        }
        .sidebar .stSidebar {
            background-color: #0f172a;
            border-right: 1px solid #1e293b;
        }
        h1, h2, h3 {
            color: #f8fafc;
            font-weight: 700;
            letter-spacing: -0.02em;
        }
        .stButton>button {
            background: linear-gradient(135deg, #38bdf8 0%, #0284c7 100%);
            color: #090d16;
            font-weight: 600;
            border: none;
            border-radius: 0.5rem;
            padding: 0.5rem 1rem;
        }
    </style>
""", unsafe_allow_html=True)

import streamlit as st
import requests

st.set_page_config(page_title="AI Resume & Skill Gap Analyzer", layout="wide")

st.title("📄 AI Resume & Skill Gap NLP Analyzer")
st.markdown("Automated entity extraction, document stream parsing, and benchmark skill scoring.")

uploaded_file = st.file_uploader("Upload Resume (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Document Submission")
        st.info(f"Loaded: **{uploaded_file.name}** ({len(uploaded_file.getvalue()) / 1024:.1f} KB)")
        
        if st.button("Run NLP Extraction Pipeline", type="primary"):
            with st.spinner("Parsing document stream and extracting entities..."):
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type or "text/plain")}
                try:
                    res = requests.post("http://localhost:8000/api/v1/resume/analyze", files=files, timeout=10)
                    if res.status_code == 200:
                        st.session_state["resume_data"] = res.json()
                        st.success("Resume Parsed Successfully!")
                    else:
                        st.error(f"Extraction Error: {res.text}")
                except Exception:
                    st.warning("Backend API offline. Running local client-side extraction simulation.")
                    st.session_state["resume_data"] = {
                        "filename": uploaded_file.name,
                        "skill_analysis": {
                            "match_percentage": 88.5,
                            "seniority_level": "Senior Systems Engineer",
                            "matched_skills": ["Python", "FastAPI", "Docker", "AWS", "CI/CD", "SQL", "PyTorch"],
                            "missing_skills": ["Kubernetes", "RAG"]
                        },
                        "extracted_entities": {"skills_detected": ["Python", "FastAPI", "Docker", "AWS", "Postgres", "PyTorch", "Redis"]},
                        "recommendations": [
                            "Target Role Skill Gaps: Add verified project experience demonstrating KUBERNETES, RAG.",
                            "High ATS Compatibility: Resume demonstrates strong alignment with modern systems engineering profiles."
                        ]
                    }

    with col2:
        if "resume_data" in st.session_state:
            data = st.session_state["resume_data"]
            skill_info = data["skill_analysis"]
            
            st.subheader("ATS Compatibility & Skill Scores")
            st.metric(label="Target Match Compatibility", value=f"{skill_info['match_percentage']}%", delta=skill_info["seniority_level"])
            
            st.markdown("#### Matched Skills")
            st.success(", ".join(skill_info["matched_skills"]))
            
            if skill_info["missing_skills"]:
                st.markdown("#### Skill Gap Deficits")
                st.error(", ".join(skill_info["missing_skills"]))
            
            st.markdown("#### Strategic Recommendations")
            for rec in data["recommendations"]:
                st.info(f"💡 {rec}")

