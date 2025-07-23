import os
from scraper import github_scraper, linkedIn_scraper
from typing import Dict, Any

def scrape_github(username: str) -> Dict[str, Any]:
    """
    Scrapes public GitHub data for the given username.

    Args:
        username (str): GitHub username

    Returns:
        dict: A dictionary of extracted GitHub profile data
    """
    if not username:
        raise ValueError("GitHub username is required")

    return github_scraper.extract_profile(username)


def scrape_linkedin(profile_url: str) -> Dict[str, Any]:
    """
    Scrapes public LinkedIn data for the given profile URL.

    Args:
        profile_url (str): LinkedIn profile URL

    Returns:
        dict: A dictionary of extracted LinkedIn profile data
    """
    if not profile_url:
        raise ValueError("LinkedIn profile URL is required")

    return linkedIn_scraper.extract_profile(profile_url)


def combined_scrape(github_username: str = None, linkedin_url: str = None) -> Dict[str, Any]:
    """
    Runs both GitHub and LinkedIn scrapers and returns merged skill data.

    Args:
        github_username (str): Optional GitHub username
        linkedin_url (str): Optional LinkedIn profile URL

    Returns:
        dict: Combined skill data from both platforms
    """
    combined_data = {}

    if github_username:
        try:
            github_data = scrape_github(github_username)
            combined_data["github"] = github_data
        except Exception as e:
            combined_data["github_error"] = str(e)

    if linkedin_url:
        try:
            linkedin_data = scrape_linkedin(linkedin_url)
            combined_data["linkedin"] = linkedin_data
        except Exception as e:
            combined_data["linkedin_error"] = str(e)

    return combined_data
