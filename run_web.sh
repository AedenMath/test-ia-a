#!/bin/bash

# Web server launcher script with Python and Flask checks
# This script ensures the required dependencies are available before launching the web server

set -e

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}================================${NC}"
echo -e "${GREEN}Web Server Launcher${NC}"
echo -e "${GREEN}================================${NC}"
echo ""

# Check if Python is installed
echo -e "${YELLOW}Checking for Python...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed or not in PATH${NC}"
    echo "Please install Python 3 to continue."
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo -e "${GREEN}✓ Python ${PYTHON_VERSION} found${NC}"
echo ""

# Check if Flask is installed
echo -e "${YELLOW}Checking for Flask...${NC}"
if ! python3 -c "import flask" 2>/dev/null; then
    echo -e "${RED}Error: Flask is not installed${NC}"
    echo "Installing Flask..."
    python3 -m pip install flask
    if [ $? -ne 0 ]; then
        echo -e "${RED}Failed to install Flask${NC}"
        exit 1
    fi
fi

FLASK_VERSION=$(python3 -c "import flask; print(flask.__version__)" 2>/dev/null)
echo -e "${GREEN}✓ Flask ${FLASK_VERSION} found${NC}"
echo ""

# Check if virtual environment exists (optional but recommended)
if [ -d "venv" ]; then
    echo -e "${YELLOW}Activating virtual environment...${NC}"
    source venv/bin/activate
    echo -e "${GREEN}✓ Virtual environment activated${NC}"
    echo ""
fi

# Launch the web server
echo -e "${GREEN}Starting web server...${NC}"
echo -e "${YELLOW}================================${NC}"
echo ""

python3 -m flask run

# Exit status
EXIT_CODE=$?
if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}Web server stopped gracefully${NC}"
else
    echo -e "${RED}Web server exited with error code: ${EXIT_CODE}${NC}"
fi

exit $EXIT_CODE
