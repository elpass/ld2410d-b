# Contributing to LD2410D-B Integration

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and improve

## How to Contribute

### Reporting Bugs

1. Check if the issue already exists
2. Provide a clear description of the bug
3. Include:
   - Home Assistant version
   - Python version
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - Relevant logs
   - Device model and firmware version

### Suggesting Enhancements

1. Clearly describe the enhancement
2. Explain the use case and benefits
3. Provide examples if applicable
4. Discuss possible implementation approaches

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Ensure code quality:
   - Follow PEP 8 style guide
   - Add docstrings to functions
   - Update documentation as needed
5. Commit with clear messages (`git commit -m 'Add amazing feature'`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request with a clear description

## Development Setup

```bash
# Clone the repository
git clone https://github.com/elpass/ld2410d-b.git
cd ld2410d-b

# Recommended: Use a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt
```

## Testing

Ensure all changes are tested:

```bash
# Run linting
flake8 .

# Format code
black .

# Run type checking
mypy .
```

## Documentation

- Update README.md for user-facing changes
- Update CHANGELOG.md with version entries
- Add docstrings to all new functions
- Include inline comments for complex logic

## Areas for Contribution

- [ ] Additional sensor variants support
- [ ] Improved error handling
- [ ] Performance optimizations
- [ ] Additional localization languages
- [ ] Test coverage improvements
- [ ] Documentation improvements
- [ ] CI/CD pipeline enhancements

## Questions?

Feel free to open an issue with the `question` label or start a discussion.

Thank you for contributing! 🎉