#!/usr/bin/env bash
chmod +x build.sh
# exit on error
set -o errexit

# Install build essentials
apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    gcc

# Install core dependencies first
pip install -r requirements-first.txt

# Install the rest of the requirements
pip install -r requirements.txt