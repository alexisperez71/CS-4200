import json
import requests
from bs4 import BeautifulSoup

def scrape_patch_notes(url):
    """Scrape patch notes from the given URL."""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: Unable to access {url}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract relevant sections (this may vary by website)
    sections = soup.find_all(["h2", "h3", "p"])  # Adjust tags as needed

    patch_notes = []
    for section in sections:
        text = section.get_text(strip=True)
        if any(keyword in text.lower() for keyword in ["new", "fix", "deprecated", "security"]):
            patch_notes.append(text)

    return patch_notes if patch_notes else ["No structured patch notes found."]


def fetch_updates(software_name, version=None):
    """Get the patch notes for a specific software and version."""
    url = get_patch_notes_url(software_name, version)
    if not url:
        print("Software not found in patch_notes.json.")
        return

    print(f"Fetching patch notes from: {url}")
    notes = scrape_patch_notes(url)

    print("\n📌 Patch Notes:")
    for note in notes:
        print(f"- {note}")


# Example Usage
fetch_updates("Python", "3.11")  # Get Python 3.11 updates
fetch_updates("Node.js")  # Get Node.js updates
fetch_updates("React")  # Get React updates
