import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health_endpoint():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_resume_text_analysis():
    sample_resume = (
        "Senior Software Engineer with 5 years experience in Python, FastAPI, Docker, "
        "PostgreSQL, AWS, and PyTorch machine learning models."
    )
    files = {"file": ("test_resume.txt", sample_resume.encode("utf-8"), "text/plain")}
    res = client.post("/api/v1/resume/analyze", files=files)
    assert res.status_code == 200
    data = res.json()
    assert data["filename"] == "test_resume.txt"
    assert "Python" in data["skill_analysis"]["matched_skills"]
    assert data["skill_analysis"]["match_percentage"] > 50.0
