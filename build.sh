#!/usr/bin/env bash
chmod +x build.sh
# exit on error
set -o errexit

# Set environment variables for build
export CFLAGS="-I/usr/include/python3.11"
export LDFLAGS="-L/usr/lib/python3.11"

# Install build essentials
apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    python3.11-dev \
    gcc

# Install core dependencies first
pip install -r requirements-first.txt

# Clean any previous builds
pip cache purge
rm -rf build/ dist/ *.egg-info

# Install the rest of the requirements
pip install -r requirements.txt