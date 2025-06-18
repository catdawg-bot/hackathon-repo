# Optimized version of the script
# with performance improvements and better practices
import requests
import json
import base64
from typing import Dict


def create_branch_with_files(
    token: str,
    owner: str,
    repo: str,
    branch_name: str,
    files: Dict[str, str],
    base_branch: str = "main"
):
    """Create a new branch on GitHub and add files to it.
    
    Args:
        token: GitHub Personal Access Token
        owner: Repository owner (username or organization)
        repo: Repository name
        branch_name: Name of the new branch to create
        files: Dictionary of {file_path: file_content}
        base_branch: Base branch to create the new branch from (default: "main")
    
    Returns:
        bool: True if successful, False otherwise
    """
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }
    base_url = f"https://api.github.com/repos/{owner}/{repo}"

    try:
        # 1. Get the SHA of the base branch
        print(f"Getting SHA of base branch '{base_branch}'...")
        ref_response = requests.get(
            f"{base_url}/git/ref/heads/{base_branch}",
            headers=headers
        )
        if ref_response.status_code != 200:
            print(f"Error getting base branch: {ref_response.status_code} - {ref_response.text}")
            return False
        base_sha = ref_response.json()["object"]["sha"]
        print(f"Base branch SHA: {base_sha}")

        # 2. Create the new branch
        print(f"Creating new branch '{branch_name}'...")
        create_ref_data = {
            "ref": f"refs/heads/{branch_name}",
            "sha": base_sha
        }
        create_response = requests.post(
            f"{base_url}/git/refs",
            headers=headers,
            data=json.dumps(create_ref_data)
        )
        if create_response.status_code not in [201, 422]:  # 422 if branch already exists
            print(f"Error creating branch: {create_response.status_code} - {create_response.text}")
            return False
        if create_response.status_code == 422:
            print(f"Branch '{branch_name}' already exists, continuing...")
        else:
            print(f"Branch '{branch_name}' created successfully!")

        # 3. Add files to the branch
        for file_path, file_content in files.items():
            print(f"Adding file: {file_path}")
            encoded_content = base64.b64encode(file_content.encode('utf-8')).decode('utf-8')
            file_response = requests.get(
                f"{base_url}/contents/{file_path}?ref={branch_name}",
                headers=headers
            )
            file_data = {
                "message": f"Add/Update {file_path}",
                "content": encoded_content,
                "branch": branch_name
            }
            if file_response.status_code == 200:
                file_data["sha"] = file_response.json()["sha"]
                print(f"  Updating existing file...")
            else:
                print(f"  Creating new file...")
            put_response = requests.put(
                f"{base_url}/contents/{file_path}",
                headers=headers,
                data=json.dumps(file_data)
            )
            if put_response.status_code not in [200, 201]:
                print(f"Error adding file {file_path}: {put_response.status_code} - {put_response.text}")
                return False
            print(f"  File {file_path} added successfully!")
        print(f"All files added to branch '{branch_name}' successfully!")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


# Example usage
if __name__ == "__main__":
    # Configuration
    GITHUB_TOKEN = "your_personal_access_token_here"
    REPO_OWNER = "your_username"
    REPO_NAME = "your_repo_name"
    NEW_BRANCH = "feature/new-files"
    
    # Files to add
    files_to_add = {
        "src/hello.py": "print('Hello, World!')\n",
        "README_NEW.md": "# New Feature\n\nThis is a new feature branch.\n",
        "config/settings.json": '{\n  "version": "1.0.0",\n  "debug": true\n}\n'
    }
    
    # Create branch with files
    success = create_branch_with_files(
        token=GITHUB_TOKEN,
        owner=REPO_OWNER,
        repo=REPO_NAME,
        branch_name=NEW_BRANCH,
        files=files_to_add,
        base_branch="main"  # Optional, defaults to "main"
    )
    
    if success:
        print("Branch created and files added successfully!")
    else:
        print("Failed to create branch or add files.")