import io
import re
from typing import Dict, List, Any
import pdfplumber
import docx

class ResumeNLPParser:
    def __init__(self):
        # Curated technical taxonomy for entity and skill matching
        self.tech_taxonomy = {
            "Languages": ["python", "javascript", "typescript", "golang", "java", "c++", "rust", "sql"],
            "Frameworks": ["fastapi", "react", "next.js", "django", "flask", "pytorch", "tensorflow"],
            "Cloud & DevOps": ["docker", "kubernetes", "aws", "gcp", "azure", "terraform", "ci/cd", "redis", "postgres"],
            "AI/ML": ["rag", "llm", "embeddings", "nlp", "chromadb", "langchain", "mlops", "scikit-learn"]
        }

    def extract_text_from_stream(self, file_bytes: bytes, filename: str) -> str:
        text = ""
        if filename.lower().endswith(".pdf"):
            with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
                for page in pdf.pages:
                    extracted = page.extract_text()
                    if extracted:
                        text += extracted + "\n"
        elif filename.lower().endswith((".docx", ".doc")):
            doc = docx.Document(io.BytesIO(file_bytes))
            for para in doc.paragraphs:
                text += para.text + "\n"
        else:
            text = file_bytes.decode("utf-8", errors="ignore")
        return text

    def analyze_skills(self, text: str, target_role_skills: List[str] = None) -> Dict[str, Any]:
        text_lower = text.lower()
        if not target_role_skills:
            target_role_skills = ["python", "fastapi", "docker", "kubernetes", "aws", "ci/cd", "sql", "pytorch", "rag"]
        
        extracted_skills = []
        for category, skills in self.tech_taxonomy.items():
            for skill in skills:
                # Word boundary match
                if re.search(r"\b" + re.escape(skill) + r"\b", text_lower):
                    extracted_skills.append(skill.title())

        # Skill gap analysis against benchmark role
        matched = [s for s in target_role_skills if s.lower() in [e.lower() for e in extracted_skills]]
        missing = [s for s in target_role_skills if s.lower() not in [e.lower() for e in extracted_skills]]
        match_score = round((len(matched) / len(target_role_skills)) * 100, 1) if target_role_skills else 100.0

        seniority = "Senior Engineer" if len(extracted_skills) >= 8 else "Mid-Level Engineer" if len(extracted_skills) >= 4 else "Junior / Entry Level"

        recommendations = []
        if missing:
            recommendations.append(f"Target Role Skill Gaps: Add verified project experience demonstrating: {', '.join(missing).upper()}.")
        if "docker" not in [e.lower() for e in extracted_skills]:
            recommendations.append("Cloud Containerization: Include container deployment specs (Docker / Kubernetes).")
        if match_score >= 80:
            recommendations.append("High ATS Compatibility: Resume demonstrates strong alignment with modern systems engineering profiles.")

        return {
            "matched_skills": [m.title() for m in matched],
            "missing_skills": [m.title() for m in missing],
            "match_percentage": match_score,
            "seniority_level": seniority,
            "recommendations": recommendations,
            "all_extracted": list(set(extracted_skills))
        }

parser_service = ResumeNLPParser()
