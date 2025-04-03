import json

def getUrl(software_name, version=None):
    with open("patch_notes.json", "r") as file:
        patch_notes = json.load(file)

    for entry in patch_notes:
        if entry["name"].lower() == software_name.lower():
            if "{version}" in entry["url"] and version:
                return entry["url"].replace("{version}", version)
            return entry["url"]

    return ()