# wait-for-status-checks
GitHub Action for searching and filtering Pull Requests based on specified criteria.

## Inputs

| Input           | Description                                                  | Required| Default                           |
|-----------------|--------------------------------------------------------------|---------|-----------------------------------|
| `repo`          | Github repo name e.g. owner/repo_name                        | Yes     | ${{ github.event.repository.name }} |
| `title`         | Title of the GitHub pull request to search and fetch details | Yes     | None                              |



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