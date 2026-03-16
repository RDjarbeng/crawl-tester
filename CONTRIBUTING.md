This contributing AI generated, please don't fell intimidated to contribute in case this document sounds discouraging
# Contributing to Crawl Tester

Thank you for your interest in contributing to Crawl Tester! We welcome contributions from everyone.

## Code of Conduct

This project is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please be respectful and constructive in all interactions.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps which reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed after following the steps**
- **Explain which behavior you expected to see instead and why**
- **Include screenshots/output if possible**
- **Include your environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Explain why this enhancement would be useful**
- **List some other tools where this enhancement exists, if applicable**

### Pull Requests

- Fill in the required template
- Follow the Python style guide (PEP 8)
- Include appropriate test cases
- Update documentation as needed
- End all files with a newline

## Development Setup

1. Fork the repository and clone it locally:
```bash
git clone https://github.com/your-username/crawl-tester.git
cd crawl-tester
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:
```bash
playwright install
```

## Style Guide

### Python Style Guide

We follow [PEP 8](https://pep8.org/). Here are key points:

- Use 4 spaces for indentation
- Maximum line length is 88 characters
- Use meaningful variable and function names
- Add docstrings to functions and modules
- Add comments for complex logic

Example:
```python
def crawl_website(url: str, timeout: int = 30) -> str:
    """
    Crawl a website and return its content as markdown.
    
    Args:
        url: The URL to crawl
        timeout: Timeout in seconds (default: 30)
    
    Returns:
        The website content as markdown
    
    Raises:
        ValueError: If URL is invalid
    """
    pass
```

### Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

Example:
```
Add support for custom headers in crawler config

This allows users to set custom headers for their crawl requests.
Fixes #123
```

### Documentation

- Update README.md if you change functionality
- Add docstrings to all public functions
- Keep documentation clear and concise

## Testing

Before submitting a pull request:

1. Test your changes thoroughly
2. Ensure existing functionality still works
3. Test edge cases

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Feel free to open an issue or contact the maintainers.

Thank you for contributing! 🎉
