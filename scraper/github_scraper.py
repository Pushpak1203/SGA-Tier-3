import requests
from typing import List, Dict

GITHUB_API_URL = "https://api.github.com"

def get_user_repos(username: str) -> List[Dict]:
    """
    Fetch all public repositories of a GitHub user.
    """
    url = f"{GITHUB_API_URL}/users/{username}/repos"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch repos for {username}: {response.status_code}")

    return response.json()

def extract_skills_from_repos(repos: List[Dict]) -> List[str]:
    """
    Derive skills based on programming languages and tech stacks used in repos.
    """
    skills = set()

    for repo in repos:
        if repo.get("language"):
            skills.add(repo["language"])
        
        # Optionally inspect description or topics for more info
        if "topics" in repo:
            skills.update(repo["topics"])

    return list(skills)

def get_starred_repo_count(username: str) -> int:
    """
    Count the number of repositories the user has starred.
    """
    url = f"{GITHUB_API_URL}/users/{username}/starred"
    response = requests.get(url)

    if response.status_code != 200:
        return 0

    return len(response.json())

def scrape_github_profile(username: str) -> Dict:
    """
    Aggregate data for GitHub profile and infer technical strengths.
    """
    try:
        repos = get_user_repos(username)
        skills = extract_skills_from_repos(repos)
        stars = get_starred_repo_count(username)

        return {
            "username": username,
            "public_repo_count": len(repos),
            "skills": skills,
            "starred_count": stars
        }

    except Exception as e:
        print(f"[GitHub Scraper Error] {e}")
        return {
            "username": username,
            "public_repo_count": 0,
            "skills": [],
            "starred_count": 0,
            "error": str(e)
        }

# CLI Test
if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    profile_data = scrape_github_profile(username)
    print(profile_data)
