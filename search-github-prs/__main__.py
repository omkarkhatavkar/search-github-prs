import argparse
import os
import requests
import json
import sys
from pathlib import Path

outputs_path = Path(os.environ["GITHUB_OUTPUT"])
summary_path = Path(os.environ["GITHUB_STEP_SUMMARY"])


def write_to_summary(message, is_error=False):
    with summary_path.open(mode="a") as summary_file:
        if is_error:
            sys.stderr.write(message + "\n")
        else:
            sys.stdout.write(message + "\n")
        summary_file.write(message + "\n")


def set_gha_output(name, value):
    """Set an action output using an environment file.

    Refs:
    * https://hynek.me/til/set-output-deprecation-github-actions/
    * https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter
    """
    with open(outputs_path, "a") as outputs_file:
        print(f"{name}={value}", file=outputs_file, end="\n")


def main(arguments):
    from github import Github

    github = Github(arguments.repo_token)
    repo = github.get_repo(arguments.repo)
    pr_list = repo.get_pulls()
    pr_details = []
    for pr in pr_list:
        if pr.title == arguments.title:
            write_to_summary("Found the matching PR.")
            pr_details.append({"html_url": pr.html_url})
    set_gha_output("details", json.dumps(pr_details))
    if len(pr_details):
        set_gha_output("result", "success")
    else:
        set_gha_output("result", "failure")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="GitHub Actions that search/filter github PR's"
    )
    parser.add_argument(
        "--repo", required=True, type=str, help="Github repo name e.g. owner/repo_name"
    )
    parser.add_argument("--title", required=True,
                        type=str, help="Title of PR name")
    parser.add_argument(
        "--repo_token", required=True, type=str, help="Repo Token for authentication"
    )
    arguments = parser.parse_args()
    global api_endpoint
    api_endpoint = f"https://api.github.com/repos/{arguments.repo}/pulls"
    main(arguments)
