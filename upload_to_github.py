import requests
import json
import os
import base64
from pathlib import Path

# GitHub API configuration
GITHUB_API_URL = "https://api.github.com"
REPO_OWNER = "AAQUIB3047"
REPO_NAME = "capstone"

# You'll need to provide a GitHub Personal Access Token
# Create one at: https://github.com/settings/tokens
GITHUB_TOKEN = input("Enter your GitHub Personal Access Token: ")

def create_repository():
    """Create the repository if it doesn't exist"""
    url = f"{GITHUB_API_URL}/user/repos"
    data = {
        "name": REPO_NAME,
        "description": "Capstone Project",
        "private": False,
        "auto_init": False
    }
    
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"Repository {REPO_NAME} created successfully!")
        return True
    elif response.status_code == 422:
        print(f"Repository {REPO_NAME} already exists!")
        return True
    else:
        print(f"Error creating repository: {response.json()}")
        return False

def upload_file(file_path, repo_path, commit_message="Upload file"):
    """Upload a file to the repository"""
    with open(file_path, 'rb') as f:
        content = base64.b64encode(f.read()).decode()
    
    url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/contents/{repo_path}"
    data = {
        "message": commit_message,
        "content": content
    }
    
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.put(url, json=data, headers=headers)
    if response.status_code in [200, 201]:
        print(f"Successfully uploaded {repo_path}")
        return True
    else:
        print(f"Error uploading {repo_path}: {response.json()}")
        return False

def main():
    # Create repository
    if not create_repository():
        return
    
    # Upload files from capstone-main directory
    capstone_dir = Path("capstone-main")
    if not capstone_dir.exists():
        print("capstone-main directory not found!")
        return
    
    # Upload README.md
    readme_path = capstone_dir / "README.md"
    if readme_path.exists():
        upload_file(readme_path, "README.md", "Initial commit - Add README")
    
    print("Upload completed!")

if __name__ == "__main__":
    main()
