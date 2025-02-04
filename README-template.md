# EECA Python Template

![Tests](https://github.com/EECA-NZ/eeca-python-template/actions/workflows/python-tests.yml/badge.svg)
![Linting](https://github.com/EECA-NZ/eeca-python-template/actions/workflows/pylint.yml/badge.svg)
[Test Coverage Report](https://eeca-nz.github.io/eeca-python-template/htmlcov)

This repository serves as a template for Python projects at EECA, including pre-configured GitHub Actions workflows for linting and testing.

## How to Use

It is assumed that the devloper is working in Ubuntu (typically within `wsl` on an EECA laptop).

1. Click on "Use this template" on the GitHub repository page.
1. Create a new repository using this template.
1. Clone the repository: `git clone git@github.com:<gituser>/<new_repo_name>.git`
1. Update `pyproject.toml` and if necessary add a `setup.py` with your project's details.
1. Create a virtual environment for your project:
   ```
   python -m venv .venv
   source ./.venv/bin/activate
   ```
   Note that in powershell these commands would be:
   ```
   python -m venv .venv
   .\.venv\Scripts\activate
   ```
1. Install the required dependencies:

   ```
   python -m pip install --upgrade pip
   python -m pip install -r requirements-dev.txt
   ```
1. Install the pre-commit hooks:
   ```
   pre-commit install
   ```
    This installs the Git hooks specified in `.pre-commit-config.yaml` and ensures that code formatting and linting checks run before each commit.
1. Start developing your Python package in the `src/` directory.
1. Write tests in the `tests/` directory.
1. Running Tests Locally:
    ```
    python -m pytest
    ```
1. Running Linters and Formatters Locally:
    * Black and Isort:
        ```
        python -m black src/ tests/
        python -m isort src/ tests/
        ```
    * Pylint:
        ```
        python -m pylint src/ tests/
        ```
1. Ensure Code Quality Before Pushing:
Make sure all tests pass and code adheres to style guidelines before pushing changes.

## Viewing Coverage Reports on GitHub Pages
This template repository is configured to generate coverage reports using Coverage.py during the GitHub Actions workflows. The coverage reports are automatically pushed to the gh-pages branch. By enabling GitHub Pages in your repository, you can view these reports online.

Steps to Enable GitHub Pages:

1. Navigate to Repository Settings:
    * Go to your repository on GitHub.
    * Click on the Settings tab.

1. Enable GitHub Pages:
    * In the left sidebar, click on Pages (or scroll down to the GitHub Pages section).
    * Under Source, select the `gh-pages` branch and set the folder to / (root).
    * Click Save.

1. Update the link at the top of the `README.md` to point at the coverage report for the new repository:
    * Once GitHub Pages is enabled, your coverage report will be available at:
    ```
    https://[your-username].github.io/[your-repository-name]/htmlcov/
    ```
    Replace [your-username] and [your-repository-name] with your GitHub username and the repository name.

Example:
For the template repository, the coverage report can be viewed at: `https://eeca-nz.github.io/eeca-python-template/htmlcov/`.

Notes:
* It may take a few minutes for the GitHub Pages site to become active after enabling.
* The coverage report will be updated each time the tests are run and coverage is generated in the GitHub Actions workflow.


## Features
* Code Formatting: Enforces consistent code style with Black and Isort.
* Linting: Analyzes code quality using Pylint.
* Testing: Runs tests using Pytest and reports coverage with Coverage.py.
* Pre-commit Hooks: Automates code formatting and linting before commits.
* Continuous Integration: GitHub Actions workflows automate linting and testing on each push and pull request.

## Notes on Pre-commit:
* Configuration: The `.pre-commit-config.yaml` file contains the configuration for pre-commit hooks.
* Automatic Formatting: When you attempt to commit changes, pre-commit will automatically run Black, Isort and Pylint. If they make changes, you'll need to add the changes and commit again.
* Skipping Hooks: If necessary, you can skip pre-commit hooks by committing with the --no-verify flag, but this is not recommended.
