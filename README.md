# search-github-prs
GitHub Action for searching and filtering Pull Requests based on specified criteria. This action is designed to retrieve a list of Pull Requests from a GitHub repository and filter them based on user-defined criteria, providing a customizable and efficient way to manage and analyze your Pull Requests.


## Inputs

| Input           | Description                                                  | Required| Default                             |
|-----------------|--------------------------------------------------------------|---------|-------------------------------------|
| `repo`          | Github repo name e.g. owner/repo_name                        | Yes     | ${{ github.event.repository.name }} |
| `title`         | Title of the GitHub pull request to search and fetch details | Yes     | None                                |
| `repo_token`    | Pass the github token for authentication                     | Yes     | ${{ secret.GITHUB_TOKEN }}          |


## outputs

| Output   | Description                      |
|----------|----------------------------------|
| `result` | PR details of search/filter PR   |

## Example Usage

```yaml
name: Search for Specific Pull Request
on: push

jobs:
  search_for_pr:
    runs-on: ubuntu-latest
    steps:
      - name: Search for the pull request
        id: outcome
        uses: omkarkhatavkar/search-github-prs@main
        with:
          repo: 'satellite/robottelo'
          title: 'exact title of the pr you wanted to search or filter'
      - name: Check the result
        run: |
          if [ ${{ steps.outcome.outputs.result }} == 'success' ]; then
            echo "The PR is found"
          else
            echo "Failed to find the PR"
          fi
```
