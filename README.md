# ⚡ AI Resume & Skill Gap Analyzer

[![Live Web Demo](https://img.shields.io/badge/Live_App-Vercel-black?style=for-the-badge&logo=vercel)](https://ai-resume-analyzer-web-nine.vercel.app)
[![Portfolio Hub](https://img.shields.io/badge/Portfolio_Hub-Live-blue?style=for-the-badge)](https://portfolio-showcase-hub-web11.vercel.app)
[![PyTest Passing](https://img.shields.io/badge/PyTest-Passing-emerald?style=for-the-badge&logo=pytest)](https://github.com/tanushkhare/ai-resume-analyzer)

🔗 **Production URL:** [https://ai-resume-analyzer-web-nine.vercel.app](https://ai-resume-analyzer-web-nine.vercel.app)  
🌐 **Showcase Hub:** [https://portfolio-showcase-hub-web11.vercel.app](https://portfolio-showcase-hub-web11.vercel.app)

---

## 📌 Architectural Overview
Asynchronous document stream ingestion parsing PDF, DOCX, and TXT resumes using `pdfplumber` byte-stream reading. Uses spaCy Named Entity Recognition (NER) to extract technical entities across grouped taxonomies (Languages, Frameworks, Cloud, Databases) with cosine similarity ATS scoring.

---

## 🛠️ Technology Ecosystem
* **Core Architecture:** FastAPI, spaCy NER, pdfplumber, Pydantic v2
* **Testing & Quality:** PyTest, Automated GitHub Actions CI
* **Deployment:** Vercel Edge Runtime

---

## 🛡️ Production Standards
* **Byte-Stream Parsing:** Direct memory processing avoids saving temporary disk artifacts.
* **spaCy Entity Recognition:** Replaced naive keyword counting with contextual token matching.
* **Taxonomy Classification:** Matches candidates against grouped domains (Languages, Frameworks, Cloud, Databases).

---

## 🚀 API Contracts
```http
POST /api/v1/resume/analyze
Content-Type: application/json

Request Payload:
{
  "resume_text": "Experienced Python Backend Engineer with FastAPI, Docker, and PostgreSQL...",
  "target_role": "Senior Backend Systems Engineer"
}

Response (200 OK):
{
  "ats_score": 88.5,
  "seniority_level": "Senior Systems Engineer",
  "extracted_skills": ["Python", "FastAPI", "Docker", "PostgreSQL", "PyTest"],
  "skill_gap_taxonomy": {
    "present": ["Python", "FastAPI", "Docker"],
    "missing": ["Kubernetes", "Redis", "Kafka"]
  }
}

GET /health
Response: {"status": "healthy"}
.
💻 Local Quickstart
Bash
pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
pytest tests/ -v