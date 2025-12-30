# Contributing to No-IP Hostname Renewal Automation

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## Code of Conduct

- Be respectful and constructive
- Welcome newcomers and help them learn
- Focus on what's best for the community

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:

- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Your environment (OS, Python version, etc.)
- Relevant logs (with sensitive data removed)

### Suggesting Features

Feature requests are welcome! Please:

- Check if the feature has already been requested
- Clearly describe the feature and its benefits
- Explain your use case

### Pull Requests

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Test your changes locally
5. Commit with clear messages
6. Push to your fork
7. Submit a pull request

### Coding Standards

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Add docstrings to functions and classes
- Keep functions focused and single-purpose
- Use descriptive variable names
- Add logging for important operations
- Handle errors gracefully

### Commit Messages

Use clear, descriptive commit messages:

```
Add feature: Brief description

Longer explanation if needed, explaining what and why
rather than how.
```

### Testing

- Test your changes locally before submitting
- Ensure the script works in both headless and headed modes
- Verify error handling works as expected

## Development Setup

1. Clone your fork
2. Install dependencies: `poetry install`
3. Install Playwright: `poetry run playwright install chromium`
4. Create `.env` from `.env.example`
5. Make your changes
6. Test thoroughly

## Questions?

Feel free to open an issue for questions or discussion.

Thank you for contributing!
