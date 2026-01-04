# Development Guide

Welcome to the development guide for test-ia-a! This document outlines the setup process, development workflow, and guidelines for contributing to this project.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setting Up Your Development Environment](#setting-up-your-development-environment)
- [Project Structure](#project-structure)
- [Development Workflow](#development-workflow)
- [Running Tests](#running-tests)
- [Code Style and Standards](#code-style-and-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Troubleshooting](#troubleshooting)

## Prerequisites

Before you begin, ensure you have the following installed:

- **Git** (2.30+): Version control system
- **Node.js** (16+): JavaScript runtime
- **npm** (7+): Package manager (comes with Node.js)
- A text editor or IDE (VS Code, WebStorm, etc.)

## Setting Up Your Development Environment

### 1. Clone the Repository

```bash
git clone https://github.com/AedenMath/test-ia-a.git
cd test-ia-a
```

### 2. Create a Development Branch

```bash
git checkout -b feature/your-feature-name
```

Follow the naming convention:
- `feature/` for new features
- `bugfix/` for bug fixes
- `docs/` for documentation updates
- `refactor/` for code refactoring

### 3. Install Dependencies

```bash
npm install
```

### 4. Set Up Environment Variables (if applicable)

Create a `.env.local` file in the project root:

```bash
cp .env.example .env.local
```

Edit `.env.local` and configure the necessary variables for your development environment.

## Project Structure

```
test-ia-a/
├── src/                  # Source code
│   ├── components/       # React components
│   ├── utils/            # Utility functions
│   ├── styles/           # CSS/styling files
│   └── index.js          # Entry point
├── tests/                # Test files
├── public/               # Static assets
├── .github/              # GitHub configurations
├── package.json          # Project dependencies and scripts
├── README.md             # Project overview
└── DEVELOPMENT.md        # This file
```

## Development Workflow

### Starting Development

```bash
npm start
```

This starts the development server with hot-reload capabilities.

### Building the Project

```bash
npm run build
```

Creates an optimized production build.

### Linting

```bash
npm run lint
```

Check code quality and style consistency.

### Formatting

```bash
npm run format
```

Auto-format code according to project standards.

## Running Tests

### Run All Tests

```bash
npm test
```

### Run Tests in Watch Mode

```bash
npm test -- --watch
```

### Run Tests with Coverage

```bash
npm test -- --coverage
```

### Run Specific Test File

```bash
npm test -- filename.test.js
```

## Code Style and Standards

### General Guidelines

- **Language**: Write code in English
- **Indentation**: Use 2 spaces (configured in `.editorconfig`)
- **Line Length**: Keep lines under 100 characters when possible
- **Naming Conventions**:
  - Variables and functions: `camelCase`
  - Classes and Components: `PascalCase`
  - Constants: `UPPER_SNAKE_CASE`
  - Files: `kebab-case` or `PascalCase` for components

### JavaScript/React Standards

- Use ES6+ syntax
- Prefer `const` and `let` over `var`
- Use arrow functions for callbacks
- Write meaningful variable and function names
- Add JSDoc comments for complex functions:

```javascript
/**
 * Calculates the sum of two numbers
 * @param {number} a - First number
 * @param {number} b - Second number
 * @returns {number} The sum of a and b
 */
const add = (a, b) => a + b;
```

### CSS Standards

- Use descriptive class names
- Follow BEM (Block Element Modifier) naming convention
- Group related styles together
- Use CSS variables for common values:

```css
:root {
  --primary-color: #0066cc;
  --spacing-unit: 8px;
}
```

## Commit Guidelines

### Commit Message Format

```
<type>: <subject>

<body>

<footer>
```

### Type

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, missing semicolons, etc.)
- `refactor`: Code refactoring without feature or bug fix
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `chore`: Build process, dependencies, or tooling changes

### Subject Line

- Use imperative mood ("add" not "added" or "adds")
- Don't capitalize the first letter
- Don't end with a period
- Limit to 50 characters

### Body

- Explain what and why, not how
- Wrap at 72 characters
- Separate from subject with a blank line

### Footer

Include references to issues:

```
Fixes #123
Related to #456
```

### Example

```
feat: add user authentication

Implement JWT-based authentication system with login and logout
endpoints. Use bcrypt for password hashing and store tokens
in HTTP-only cookies for enhanced security.

Fixes #42
```

## Pull Request Process

### Before Submitting

1. **Update your branch** with the latest changes from main:
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. **Run tests** to ensure everything passes:
   ```bash
   npm test
   ```

3. **Lint and format** your code:
   ```bash
   npm run lint
   npm run format
   ```

4. **Review your changes** for quality and style compliance

### Creating a Pull Request

1. Push your branch to GitHub:
   ```bash
   git push origin feature/your-feature-name
   ```

2. Open a pull request with a descriptive title and description

3. Link related issues: `Fixes #123` or `Related to #456`

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
Describe how you tested these changes

## Checklist
- [ ] Tests pass locally
- [ ] Code follows style guidelines
- [ ] Self-reviewed code
- [ ] Comments added for complex logic
- [ ] Documentation updated
```

### Review Process

- At least one approval required before merging
- Address review comments promptly
- Re-request review after making changes
- Maintain a respectful and constructive tone

## Troubleshooting

### Common Issues

#### Port Already in Use

```bash
# Linux/Mac
lsof -i :3000
kill -9 <PID>

# Windows
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

#### Dependencies Installation Issues

```bash
# Clear npm cache
npm cache clean --force

# Remove node_modules and package-lock.json
rm -rf node_modules package-lock.json

# Reinstall
npm install
```

#### Git Merge Conflicts

1. Open conflicted files
2. Resolve conflicts manually
3. Stage resolved files: `git add .`
4. Complete the merge: `git commit -m "Resolve merge conflicts"`

#### Tests Failing Locally

```bash
# Clear Jest cache
npm test -- --clearCache

# Run tests in verbose mode
npm test -- --verbose
```

## Getting Help

- **Documentation**: Check the project README and inline code comments
- **Issues**: Search existing GitHub issues for solutions
- **Discussions**: Start a discussion for broader questions
- **Pull Requests**: Review existing PRs for examples

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Assume good intent
- Report harassment or inappropriate behavior

---

**Last Updated**: January 4, 2026

For additional information, see our main [README.md](README.md) and project repository.
