# Development Guide

This guide will help you set up a development environment for contributing to Crawl Tester.

## Prerequisites

- Python 3.8 or higher
- Git
- pip or conda
- A text editor or IDE (VS Code, PyCharm, etc.)

## Setting Up Your Development Environment

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/crawl-tester.git
cd crawl-tester
```

### 2. Create a Virtual Environment

**Using venv (Python built-in):**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**Using conda:**
```bash
conda create -n crawl-tester python=3.10
conda activate crawl-tester
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers

```bash
playwright install
```

### 5. Verify Installation

```bash
python main.py --output test
```

You should see output files created in the project root.

## Project Structure

```
crawl-tester/
├── main.py                 # Entry point
├── requirements.txt        # Python dependencies
├── setup.py               # Setup configuration
├── pyproject.toml         # Modern Python project config
├── README.md              # Project documentation
├── LICENSE                # MIT License
├── CONTRIBUTING.md        # Contributing guidelines
├── SECURITY.md            # Security policy
├── EXAMPLES.md            # Usage examples
├── DEVELOPMENT.md         # This file
└── .gitignore            # Git ignore patterns
```

## Code Style

We follow PEP 8. Here are the key points:

- 4 spaces for indentation
- Maximum line length: 88 characters (Black default)
- Use meaningful variable names
- Add docstrings to all functions
- Add type hints where practical

### Format Your Code

We recommend using **black** for automatic formatting:

```bash
pip install black
black main.py
```

### Lint Your Code

Check for style issues with **flake8**:

```bash
pip install flake8
flake8 main.py
```

### Type Checking

Check types with **mypy**:

```bash
pip install mypy
mypy main.py
```

## Running Tests

Currently, the project is in early development. Tests will be added soon.

```bash
pytest tests/
```

## Common Development Tasks

### Adding a New Feature

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Write your code following the style guide
3. Test your changes
4. Commit with a clear message: `git commit -m "Add my feature"`
5. Push to your fork: `git push origin feature/my-feature`
6. Open a Pull Request

### Fixing a Bug

1. Create a bug fix branch: `git checkout -b fix/bug-description`
2. Write a test that reproduces the bug
3. Fix the bug
4. Verify the test passes
5. Follow the commit and push steps above

### Updating Dependencies

```bash
pip list --outdated
pip install --upgrade <package-name>
```

Update `requirements.txt` after upgrading:

```bash
pip freeze > requirements.txt
```

## Git Workflow

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Create a feature branch** from `main`
4. **Make your changes** with clear commits
5. **Push to your fork** on GitHub
6. **Open a Pull Request** against the main repository

### Commit Message Guidelines

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, missing semicolons, etc.)
- `refactor`: Code refactoring without feature changes
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `chore`: Build process, dependencies, etc.

**Example:**
```
feat(crawler): add support for custom headers

Allow users to set custom headers for crawler requests
through the CrawlerRunConfig object.

Fixes #123
```

## Debugging

### Enable Verbose Logging

```python
async with AsyncWebCrawler(verbose=True) as crawler:
    # Your code here
```

### Print Debugging

```python
import asyncio

async def debug_example():
    print(f"Debug: url = {url}")
    result = await crawler.arun(url=url, crawler_config=config)
    print(f"Debug: result = {result}")
```

### Using a Debugger

VS Code example `.vscode/launch.json`:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
```

## Performance Profiling

```python
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()

# Your code here

profiler.disable()
stats = pstats.Stats(profiler)
stats.sort_stats("cumulative")
stats.print_stats()
```

## Documentation

When adding features:

1. Update README.md if behavior changes
2. Add docstrings using Google style:
```python
def function(param1: str, param2: int) -> bool:
    """Brief description.
    
    Longer description if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When something is invalid
    """
    pass
```

3. Update CHANGELOG.md with your changes
4. Add examples to EXAMPLES.md if applicable

## Getting Help

- Check existing issues and PRs
- Read the documentation in README.md
- Look at EXAMPLES.md for usage patterns
- Ask in GitHub Discussions (when available)

## Code Review Process

All contributions go through code review:

1. GitHub Actions runs automated checks
2. At least one maintainer reviews the PR
3. Address any requested changes
4. Once approved, the PR is merged

## Releasing a New Version

(For maintainers only)

1. Update version in `setup.py` and `pyproject.toml`
2. Update CHANGELOG.md
3. Create a git tag: `git tag v1.0.0`
4. Push tag: `git push origin v1.0.0`
5. GitHub Actions automatically builds and publishes

## Questions?

Feel free to open an issue or discussion on GitHub!

---

Thank you for helping improve Crawl Tester! 🚀
