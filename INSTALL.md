# Installation Guide

Welcome to the AedenMath/test-ia-a project! This guide will help you set up the project on your local machine.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Detailed Installation Steps](#detailed-installation-steps)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)
- [Advanced Installation Options](#advanced-installation-options)
- [Next Steps](#next-steps)

## Prerequisites

Before you begin, ensure you have the following installed on your system:

### Required
- **Git**: Version 2.20 or higher
  - [Download Git](https://git-scm.com/downloads)
  - Verify installation: `git --version`

- **Python**: Version 3.8 or higher
  - [Download Python](https://www.python.org/downloads/)
  - Verify installation: `python --version` or `python3 --version`

- **pip**: Python package manager (usually comes with Python)
  - Verify installation: `pip --version` or `pip3 --version`

### Optional (Recommended)
- **Virtual Environment Manager**: venv (built-in with Python 3.3+) or virtualenv
- **Node.js**: Version 14 or higher (if the project includes JavaScript components)
- **Docker**: Version 20.10 or higher (for containerized installation)

### System Requirements
- **Operating System**: Windows, macOS, or Linux
- **RAM**: Minimum 2GB (4GB recommended)
- **Disk Space**: At least 500MB free space
- **Internet Connection**: Required for downloading dependencies

## Quick Start

Get up and running in 5 minutes:

```bash
# 1. Clone the repository
git clone https://github.com/AedenMath/test-ia-a.git
cd test-ia-a

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Verify installation
python -m pytest tests/ -v
```

If all tests pass, you're ready to go! Proceed to [Next Steps](#next-steps).

## Detailed Installation Steps

### Step 1: Clone the Repository

```bash
git clone https://github.com/AedenMath/test-ia-a.git
cd test-ia-a
```

### Step 2: Choose Your Installation Method

#### Option A: Virtual Environment (Recommended)

Virtual environments isolate project dependencies from your system Python.

**Create and activate virtual environment:**

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

You should see `(venv)` prefix in your terminal when active.

#### Option B: System-Wide Installation

```bash
# Note: This is not recommended for development as it can cause version conflicts
pip install --user -r requirements.txt
```

### Step 3: Install Dependencies

```bash
# Upgrade pip to latest version
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt

# Install development dependencies (optional, for contributing)
pip install -r requirements-dev.txt
```

### Step 4: Configure Environment Variables

If the project requires configuration:

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your configuration
# On Windows:
notepad .env
# On macOS/Linux:
nano .env
```

Ensure you update any required configuration values (API keys, database URLs, etc.).

### Step 5: Initialize Database (if applicable)

```bash
# Run database migrations
python manage.py migrate

# Create initial data/fixtures
python manage.py seed_database
```

## Verification

Verify that everything is installed correctly:

### Test 1: Python and pip Versions

```bash
python --version
pip --version
```

Expected output:
```
Python 3.8.0 (or higher)
pip 21.0 (or higher)
```

### Test 2: Verify Virtual Environment

```bash
# Should show your project path
which python  # macOS/Linux
where python  # Windows
```

### Test 3: Check Installed Packages

```bash
pip list
```

### Test 4: Run Unit Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_core.py -v

# Run tests with coverage
pytest --cov=src tests/
```

### Test 5: Import Check

```bash
python -c "import your_package; print('Successfully imported')"
```

### Test 6: Run Application (if applicable)

```bash
# Start development server
python run.py

# Or
flask run

# Application should be accessible at http://localhost:5000
```

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: "Python command not found"
**Cause**: Python is not installed or not in PATH

**Solution**:
```bash
# Check if python is installed
which python3
python3 --version

# Create an alias (macOS/Linux)
echo "alias python=python3" >> ~/.bashrc
source ~/.bashrc

# On Windows, reinstall Python and ensure "Add Python to PATH" is checked
```

#### Issue 2: "ModuleNotFoundError" or "ImportError"
**Cause**: Dependencies not installed correctly

**Solution**:
```bash
# Verify you're in the virtual environment (should see (venv) prefix)
which python

# Reinstall all dependencies
pip install -r requirements.txt --force-reinstall

# Check if package is installed
pip show package_name
```

#### Issue 3: "Permission denied" errors
**Cause**: Insufficient permissions

**Solution**:
```bash
# On macOS/Linux, use sudo cautiously
sudo pip install -r requirements.txt

# Better: Use user installation
pip install --user -r requirements.txt

# Or ensure virtual environment is activated
source venv/bin/activate
```

#### Issue 4: Virtual environment activation fails
**Cause**: Virtual environment corrupted or not created properly

**Solution**:
```bash
# Remove and recreate virtual environment
rm -rf venv  # or rmdir venv on Windows
python -m venv venv

# Activate and reinstall
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

#### Issue 5: "Conflicting dependency versions"
**Cause**: Incompatible package versions

**Solution**:
```bash
# Clear pip cache and reinstall
pip cache purge
pip install -r requirements.txt --no-cache-dir

# Or use a specific Python version
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Issue 6: Tests fail after installation
**Cause**: Missing test dependencies or environment not configured

**Solution**:
```bash
# Install test dependencies
pip install -r requirements-dev.txt

# Check test configuration
cat pytest.ini  # or setup.cfg

# Run tests with verbose output
pytest tests/ -v --tb=long
```

### Getting Help

If you encounter issues not covered here:

1. Check the project's [GitHub Issues](https://github.com/AedenMath/test-ia-a/issues)
2. Search for your error message online
3. Create a new GitHub issue with:
   - Your operating system
   - Python version (`python --version`)
   - pip version (`pip --version`)
   - Full error message and traceback
   - Steps to reproduce the issue

## Advanced Installation Options

### Docker Installation

If you prefer containerized installation:

```bash
# Build Docker image
docker build -t test-ia-a .

# Run container
docker run -it test-ia-a

# Or with volume mounting for development
docker run -it -v $(pwd):/app test-ia-a
```

**Dockerfile example** (if not provided):
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "run.py"]
```

### Development Installation

For contributing to the project:

```bash
# Clone and navigate to repo
git clone https://github.com/AedenMath/test-ia-a.git
cd test-ia-a

# Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux or venv\Scripts\activate on Windows

# Install with development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install pre-commit hooks (for code quality)
pre-commit install

# Create a development branch
git checkout -b feature/your-feature-name
```

### Editable Installation

For development work with the package:

```bash
# Install in editable mode
pip install -e .

# Or with development dependencies
pip install -e ".[dev]"
```

### Conda Installation

If you prefer using Conda:

```bash
# Create conda environment
conda create -n test-ia-a python=3.9

# Activate environment
conda activate test-ia-a

# Install dependencies
conda install --file requirements.txt

# Or install from pip within conda
pip install -r requirements.txt
```

### macOS-Specific: Using Homebrew

```bash
# Install Python via Homebrew
brew install python@3.9

# Create virtual environment
python3.9 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Windows-Specific: Using Chocolatey

```bash
# Install Python via Chocolatey
choco install python

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### GPU Support (if applicable)

For CUDA/GPU acceleration:

```bash
# Install CUDA-compatible PyTorch (example)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Verify GPU is detected
python -c "import torch; print(torch.cuda.is_available())"
```

## Next Steps

Congratulations! You've successfully installed the project. Here's what you can do next:

### For Users

1. **Read the Documentation**
   - Check out [README.md](README.md) for project overview
   - Review [docs/](docs/) directory for detailed documentation

2. **Explore Examples**
   ```bash
   python examples/basic_usage.py
   ```

3. **Run the Application**
   ```bash
   python run.py
   # or
   flask run
   ```

4. **Read the API Documentation**
   - Swagger/OpenAPI docs usually available at `http://localhost:5000/docs`

### For Contributors

1. **Set Up Development Environment**
   ```bash
   pip install -r requirements-dev.txt
   pre-commit install
   ```

2. **Review Contribution Guidelines**
   - Read [CONTRIBUTING.md](CONTRIBUTING.md)

3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Write and Run Tests**
   ```bash
   pytest tests/ -v
   pytest --cov=src tests/  # With coverage
   ```

5. **Submit a Pull Request**
   - Push your branch and create a PR on GitHub

### Additional Resources

- **Project Repository**: [GitHub](https://github.com/AedenMath/test-ia-a)
- **Issue Tracker**: [Issues](https://github.com/AedenMath/test-ia-a/issues)
- **Documentation**: [Docs](docs/)
- **Community**: Check GitHub Discussions or community channels

### Keeping Your Installation Updated

```bash
# Update packages to latest versions
pip install --upgrade -r requirements.txt

# Pull latest changes from repository
git pull origin main

# Reinstall dependencies in case of changes
pip install -r requirements.txt
```

### Uninstallation

To remove the project:

```bash
# Deactivate virtual environment
deactivate

# Delete the project directory
rm -rf test-ia-a  # macOS/Linux
rmdir /s test-ia-a  # Windows

# Delete virtual environment
rm -rf venv  # macOS/Linux
rmdir /s venv  # Windows
```

---

**Last Updated**: January 4, 2026

For additional help, please visit our [GitHub Issues](https://github.com/AedenMath/test-ia-a/issues) page or check the project's documentation.