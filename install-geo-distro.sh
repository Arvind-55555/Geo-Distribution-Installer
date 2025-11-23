#!/bin/bash
# Quick installer for Geo Distribution

set -e

echo "🌍 Geo Distribution Quick Installer"
echo "======================================"

# Check if conda is installed
if ! command -v conda &> /dev/null; then
    echo "❌ Conda not found. Please install Miniconda or Anaconda first."
    echo "Download from: https://docs.conda.io/en/latest/miniconda.html"
    exit 1
fi

# Update conda
echo "🔄 Updating conda..."
conda update -n base -c defaults conda -y

# Create environment from YAML
echo "🔧 Creating geo-distro environment..."
conda env create -f environment.yml

echo "🎉 Installation complete!"
echo ""
echo "To activate the environment:"
echo "  conda activate geo-distro"
echo ""
echo "To start Jupyter Lab:"
echo "  jupyter lab"
echo ""
echo "Happy geospatial coding! 🌐"