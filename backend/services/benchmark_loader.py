import os
import json

BENCHMARK_FILE = os.path.join("database", "benchmark_profiles.json")


def get_benchmark_profile(job_role: str) -> dict:
    """
    Retrieves the benchmark profile for the given job role.

    Args:
        job_role (str): The job role to look up.

    Returns:
        dict: A dictionary containing required and optional skills.
    """
    if not os.path.exists(BENCHMARK_FILE):
        raise FileNotFoundError(f"Benchmark file not found at: {BENCHMARK_FILE}")

    with open(BENCHMARK_FILE, "r") as f:
        data = json.load(f)

    # Case-insensitive matching for job role
    for profile in data:
        if profile.get("job_role", "").lower() == job_role.lower():
            return profile

    return None  # No matching profile found