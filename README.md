
# 🚀 Skill Gap Analyzer and Employability Enhancer

> Empowering tier-3 college engineering students to become job-ready by identifying and bridging the skill gaps through AI and real-world benchmarking.

---

## 📌 Problem Statement

Despite the growing number of engineering graduates in India, over **83% remain jobless or underemployed**, primarily due to a lack of soft skills, modern technical exposure, and practical experience. There's also **no standardized framework** to measure job readiness or align academic outcomes with real-time industry demands.

---

## 🎯 Objectives

- Parse resumes, extract skills, and analyze coding profiles.
- Compare student data with benchmark profiles of engineers at Google, Microsoft, etc.
- Identify technical and non-technical skill gaps.
- Generate a **personalized learning roadmap** for each student.
- Support entrepreneurship using the **MAST model** where applicable.
- Provide dashboards for institutions to analyze skill readiness at scale.

---

## 🧠 Core Features

- ✅ Resume Parsing (PDF/DOCX → Structured Data)
- ✅ Skill Gap Analysis using ML/NLP
- ✅ Benchmarking with real-world job roles & profiles
- ✅ Personalized Learning Roadmap (courses, projects, timelines)
- ✅ Firebase Integration for student data
- ✅ Institution Dashboard for batch-level analytics
- ✅ GPU-accelerated NLP model support

---

## 🧱 Tech Stack

| Layer       | Tech Used                                     |
|-------------|-----------------------------------------------|
| Frontend    | React.js, Chart.js, Axios                     |
| Backend     | Flask, Flask-CORS, Gunicorn                   |
| ML/NLP      | spaCy, BERT, Transformers, Scikit-learn       |
| DB & Auth   | Firebase Admin SDK, Firestore / MongoDB       |
| Scraping    | Selenium, BeautifulSoup, GitHub/LinkedIn APIs |
| Resume Parse| docx2txt, pdfminer.six, python-docx           |
| Deployment  | Docker (optional), VS Code, GPU (RTX 3050)    |

---

## 🗂️ Project Structure

```bash
SkillGapAnalyzer/
├── backend/               # Flask backend
│   ├── routes/            # API endpoints: upload, analyze, roadmap
│   ├── services/          # NLP/ML logic for parsing, comparison
│   └── config.py          # Firebase & app config
├── frontend/              # React frontend
│   ├── src/components/    # Navbar, Cards, Dashboard
│   └── src/pages/         # UploadPage, ResultsPage
├── ml_nlp_model/          # Resume & skill analysis models
│   ├── fine_tuned_model/  # BERT/spaCy models
│   └── inference.py
├── scraper/               # LinkedIn/GitHub profile scraper
├── database/              # Firebase/MongoDB schema
├── tests/                 # Backend unit tests
├── requirements.txt       # Python dependencies
└── README.md              # You are here!
```

---

## 📥 Setup Instructions

### 🔧 Backend

```bash
cd backend/
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate
pip install -r ../requirements.txt
```

Install **PyTorch with GPU**:
```bash
pip install torch==2.2.2+cu121 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### ⚙️ Firebase Setup

1. Create a Firebase project.
2. Download the `serviceAccountKey.json`.
3. Place it in `backend/config/` and reference it in `config.py`.

---

### 🌐 Frontend

```bash
cd frontend/
npm install
npm start
```

---

## 📊 Sample Output

```json
{
  "user": "John Doe",
  "gap_score": 62,
  "missing_skills": ["System Design", "Kubernetes", "Django"],
  "top_match": "Google SWE Profile",
  "recommendations": [
    "Complete Udemy course on System Design",
    "Build a project using Kubernetes and Docker",
    "Contribute to GitHub repos in your field"
  ]
}
```

---

## 🏁 Future Scope

- 🔄 Real-time job listings for dynamic gap analysis
- 🎙️ Voice-based resume feedback
- 🎓 NEAT/AICTE integration for nationwide rollout
- 🔌 Plugin for use in college placement cells

---

## 📚 References

- NASSCOM Report on Engineering Graduates
- BERT for Resume Parsing [Research]
- OECD Compass Framework for AI in Education
- GitHub & LinkedIn Public Profiles

---

## 👨‍💻 Author

Pushpak Chakraborty — Tier-3 CSE Student | AI & ML | Project hosted in VS Code using RTX 3050

---

## 📝 License

This project is under the [MIT License](https://opensource.org/licenses/MIT).
