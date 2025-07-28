from datetime import datetime

class UserProfile:
    def __init__(self, user_id, name=None, email=None, phone=None,
                 skills=None, education=None, projects=None,
                 parsed_at=None, top_match=None, gap_score=None,
                 missing_skills=None, roadmap=None):
        
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.skills = skills or []
        self.education = education or []
        self.projects = projects or []
        self.parsed_at = parsed_at or datetime.utcnow().isoformat()
        self.top_match = top_match
        self.gap_score = gap_score
        self.missing_skills = missing_skills or []
        self.roadmap = roadmap or {}

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "skills": self.skills,
            "education": self.education,
            "projects": self.projects,
            "parsed_at": self.parsed_at,
            "top_match": self.top_match,
            "gap_score": self.gap_score,
            "missing_skills": self.missing_skills,
            "roadmap": self.roadmap
        }

    @staticmethod
    def from_dict(data):
        return UserProfile(
            user_id=data.get("user_id"),
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone"),
            skills=data.get("skills", []),
            education=data.get("education", []),
            projects=data.get("projects", []),
            parsed_at=data.get("parsed_at"),
            top_match=data.get("top_match"),
            gap_score=data.get("gap_score"),
            missing_skills=data.get("missing_skills", []),
            roadmap=data.get("roadmap", {})
        )
