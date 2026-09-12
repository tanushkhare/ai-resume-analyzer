# ⚡ AI Resume & Skill Gap Analyzer

[![Live Web Demo](https://img.shields.io/badge/Live_App-Vercel-black?style=for-the-badge&logo=vercel)](https://ai-resume-analyzer-web-nine.vercel.app)
[![Portfolio Hub](https://img.shields.io/badge/Portfolio_Hub-Live-blue?style=for-the-badge)](https://portfolio-showcase-hub-web11.vercel.app)

🔗 **Production URL:** [https://ai-resume-analyzer-web-nine.vercel.app](https://ai-resume-analyzer-web-nine.vercel.app)  
🌐 **Showcase Hub:** [https://portfolio-showcase-hub-web11.vercel.app](https://portfolio-showcase-hub-web11.vercel.app)

---

## 📌 Architectural Overview
Asynchronous document parsing engine processing PDF/DOCX resumes via pdfplumber byte-stream ingestion and spaCy Named Entity Recognition (NER).

---

## 🛠️ Technology Ecosystem
* **Core Architecture:** FastAPI, spaCy NER, pdfplumber, Pydantic v2
* **Testing & Quality:** PyTest, Automated GitHub Actions CI
* **Deployment:** Vercel Edge Runtime

---

## 🚀 API Contracts
```http
POST /api/v1/resume/analyze
GET /health
```

---

## 💻 Local Quickstart
```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
pytest tests/ -v
```
