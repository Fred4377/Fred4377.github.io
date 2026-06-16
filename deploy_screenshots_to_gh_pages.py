import os
import shutil
import subprocess

repos = [
    "shopease",
    "dashpro-dashboard",
    "bookease",
    "chatbotpro",
    "CCGworkflow"
]

base_path = r"C:\Users\admin"
temp_dir = r"C:\Users\admin\temp_previews"
os.makedirs(temp_dir, exist_ok=True)

for repo in repos:
    repo_path = os.path.join(base_path, repo)
    print(f"\n========================================\nProcessing gh-pages for: {repo}\n========================================")
    
    if not os.path.exists(repo_path):
        print(f"Directory {repo_path} does not exist. Skipping.")
        continue

    # 1. Save the preview.png from the current branch
    src_preview = os.path.join(repo_path, "screenshots", "preview.png")
    if not os.path.exists(src_preview):
        print(f"Source preview image not found at {src_preview}. Skipping.")
        continue
        
    temp_preview_path = os.path.join(temp_dir, f"{repo}_preview.png")
    shutil.copy2(src_preview, temp_preview_path)
    print(f"Saved original screenshot to {temp_preview_path}")

    # 2. Get current active branch
    branch_run = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=repo_path, capture_output=True, text=True)
    original_branch = branch_run.stdout.strip()
    print(f"Original branch: {original_branch}")

    # Stash any local uncommitted changes
    subprocess.run(["git", "add", "."], cwd=repo_path)
    subprocess.run(["git", "stash"], cwd=repo_path)

    try:
        # 3. Fetch remote gh-pages branch
        print("Fetching origin gh-pages...")
        subprocess.run(["git", "fetch", "origin", "gh-pages"], cwd=repo_path)

        # 4. Checkout gh-pages
        local_branches_run = subprocess.run(["git", "branch"], cwd=repo_path, capture_output=True, text=True)
        local_branches = local_branches_run.stdout
        
        if "gh-pages" in local_branches:
            print("Checking out existing local gh-pages...")
            subprocess.run(["git", "checkout", "gh-pages"], cwd=repo_path)
            subprocess.run(["git", "reset", "--hard", "origin/gh-pages"], cwd=repo_path)
        else:
            print("Checking out and tracking origin/gh-pages...")
            subprocess.run(["git", "checkout", "-b", "gh-pages", "origin/gh-pages"], cwd=repo_path)

        # 5. Recreate screenshots folder and copy the preview.png back in
        dest_screenshots_dir = os.path.join(repo_path, "screenshots")
        os.makedirs(dest_screenshots_dir, exist_ok=True)
        dest_preview = os.path.join(dest_screenshots_dir, "preview.png")
        shutil.copy2(temp_preview_path, dest_preview)
        print(f"Copied screenshot back to {dest_preview}")

        # 6. Commit changes
        subprocess.run(["git", "add", "screenshots/preview.png"], cwd=repo_path)
        status_run = subprocess.run(["git", "status", "--porcelain"], cwd=repo_path, capture_output=True, text=True)
        if not status_run.stdout.strip():
            print("No changes in screenshots for gh-pages.")
        else:
            subprocess.run(["git", "commit", "-m", "chore: add screenshots preview for portfolio catalog"], cwd=repo_path)
            print("Committed screenshots/preview.png to gh-pages")

        # 7. Push to origin gh-pages
        print("Pushing to origin gh-pages...")
        push_result = subprocess.run(["git", "push", "origin", "gh-pages"], cwd=repo_path, capture_output=True, text=True)
        print("Push stdout:", push_result.stdout.strip())
        print("Push stderr:", push_result.stderr.strip())

    except Exception as e:
        print(f"Error while processing gh-pages for {repo}: {e}")
    finally:
        # 8. Restore original branch and pop stash
        print(f"Returning to original branch: {original_branch}...")
        subprocess.run(["git", "checkout", original_branch], cwd=repo_path)
        subprocess.run(["git", "stash", "pop"], cwd=repo_path)

# Clean up temp dir
try:
    shutil.rmtree(temp_dir)
except Exception as e:
    pass

print("\nDeployment completed successfully!")
