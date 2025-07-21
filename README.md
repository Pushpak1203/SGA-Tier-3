
# 🚀 Skill Gap Analyzer & Employability Enhancer

Empowering tier-3 college engineering students to become job-ready by identifying and bridging skill gaps through AI and real-world benchmarking.

## About

This project helps students and institutions analyze skill gaps in engineering graduates by parsing resumes, comparing against top industry profiles, and generating personalized learning roadmaps. It targets the "skills gap" that leaves many talented graduates underemployed, and provides actionable recommendations to level up.

## Features

- **Resume Parsing:** Extract skills, education, and experience from PDF/DOCX files.
- **Skill Matching:** Compare parsed skills against benchmark engineers at top companies (Google, Microsoft, etc.).
- **Skill Gap Analysis:** Identify technical and soft skill gaps.
- **Personalized Roadmaps:** Recommend courses, projects, and milestones for each student.
- **Re-Evaluation:** Students can re-upload resumes to track progress and update recommendations.
- **Dashboard:** Institutional dashboard for batch-level analytics and reporting.
- **Entrepreneurship Pathway:** MAST model integration for entrepreneurial students.

## Project Structure

```
SkillGapAnalyzer/
├── backend/                       # Flask backend (API endpoints, services)
├── frontend/                      # React frontend (components, pages, services)
├── ml_nlp_model/                  # ML/NLP models for parsing and extraction
├── scraper/                       # Scrapers for LinkedIn/GitHub profiles
├── database/                      # Schemas and sample data
├── reports/                       # Generated gap analysis reports
├── tests/                         # Unit and integration tests
├── requirements.txt               # Python dependencies
├── README.md                      # This file
└── Dockerfile                     # Containerization setup
```

## Tech Stack

- **Frontend:** React.js, Chart.js, Axios
- **Backend:** Flask, Flask-CORS, Gunicorn
- **ML/NLP:** spaCy, BERT, Transformers, Scikit-learn
- **Database:** Firebase Admin SDK, Firestore/MongoDB
- **Scraping:** Selenium, BeautifulSoup, requests
- **Deployment:** Docker, GPU (optional)

## Getting Started

### Prerequisites

- **Python 3.9+**
- **Node.js 16+** (for frontend)
- **Firebase Admin credentials** (if using Firebase)
- **Git** (optional, for version control)
- **Docker** (optional, for containerized deployment)

### Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/SkillGapAnalyzer.git
   cd SkillGapAnalyzer
   ```

2. **Set up backend:**
   ```
   cd backend
   pip install -r ../requirements.txt
   ```

3. **Set up frontend:**
   ```
   cd ../frontend
   npm install
   ```

4. **Configure environment variables:**
   - Rename `.env.example` to `.env` in both `backend/` and `frontend/`.
   - Fill in Firebase, API keys, and other secrets as needed.

5. **Run the backend:**
   ```
   cd ../backend
   flask run
   ```

6. **Run the frontend:**
   ```
   cd ../frontend
   npm start
   ```

7. **Access the app at [http://localhost:3000](http://localhost:3000)**

### Deployment

- For production, use Gunicorn (`gunicorn -w 4 app:app`) and a reverse proxy (Nginx, Apache).
- Containerize using Docker (see `Dockerfile`).
- For GPU acceleration, ensure CUDA/cuDNN is installed.

## Usage

1. **Student:** Upload your resume, view skill gaps, and follow the personalized roadmap.
2. **Faculty/Admin:** Access the dashboard to see batch analytics and track institutional progress.
3. **Periodic Re-Evaluation:** Re-upload your resume to update your skill profile and roadmap.

## Contributing

Feel free to fork, submit issues, or send pull requests. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines (if applicable).



**For support, questions, or feedback, please open an issue on GitHub or contact the project maintainers.**



📚 References
NASSCOM Report on Engineering Graduates

BERT for Resume Parsing [Research]

OECD Compass Framework for AI in Education

GitHub & LinkedIn Public Profiles





👨‍💻 Author
Pushpak Chakraborty — Tier-3 CSE Student | AI & ML | Project hosted in VS Code using RTX 3050





📝 License
This project is under the MIT License.



