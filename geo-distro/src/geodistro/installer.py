"""
Main installer functionality for Geo Distribution
"""

import os
import sys
import subprocess
import platform
import time
from pathlib import Path
from typing import Optional, List, Dict

import click
from tqdm import tqdm

from geodistro.core import GeoDistroConfig

class GeoDistroInstaller:
    def __init__(self, verbose: bool = False):
        self.system = platform.system().lower()
        self.verbose = verbose
        self.install_method = self._check_prerequisites()
        
    def _check_prerequisites(self) -> str:
        """Check if conda/mamba is available"""
        for method in ["mamba", "conda"]:
            try:
                subprocess.run([method, "--version"], 
                             capture_output=not self.verbose, 
                             check=True)
                click.echo(f"✓ {method.capitalize()} found")
                return method
            except (subprocess.CalledProcessError, FileNotFoundError):
                continue
        
        click.echo("⚠ Conda/Mamba not found. Please install Miniconda or Anaconda first.")
        click.echo("Download from: https://docs.conda.io/en/latest/miniconda.html")
        sys.exit(1)
    
    def _run_command(self, cmd: List[str], check: bool = True) -> bool:
        """Run a command with error handling"""
        try:
            if self.verbose:
                click.echo(f"Running: {' '.join(cmd)}")
            result = subprocess.run(cmd, check=check, capture_output=not self.verbose)
            return result.returncode == 0
        except subprocess.CalledProcessError as e:
            if self.verbose:
                click.echo(f"Command failed: {e}")
            return False
    
    def create_environment(self, env_name: str) -> bool:
        """Create conda environment"""
        click.echo(f"🔧 Creating environment: {env_name}")
        
        cmd = [
            self.install_method, "create", "-n", env_name, 
            "python=3.9", "-y"
        ]
        
        if self._run_command(cmd):
            click.echo(f"✓ Environment '{env_name}' created successfully")
            return True
        else:
            click.echo(f"✗ Failed to create environment '{env_name}'")
            return False
    
    def install_packages(self, env_name: str, category: str, packages: List[str]):
        """Install packages for a specific category"""
        click.echo(f"\n📦 Installing {category} packages...")
        
        successful = []
        failed = []
        
        for package in tqdm(packages, desc=category):
            # Use conda-forge for core geospatial packages
            if category == "core_geospatial":
                cmd = [
                    self.install_method, "install", "-c", "conda-forge",
                    "-n", env_name, package, "-y"
                ]
            else:
                # Use pip for Python packages
                if self.system == "windows":
                    pip_cmd = f"conda activate {env_name} && pip install {package}"
                    cmd = ["cmd", "/c", pip_cmd]
                else:
                    pip_cmd = f"source activate {env_name} && pip install {package}"
                    cmd = ["bash", "-c", pip_cmd]
            
            if self._run_command(cmd, check=False):
                successful.append(package)
            else:
                failed.append(package)
        
        if successful:
            click.echo(f"✓ Successfully installed {len(successful)}/{len(packages)} packages")
        if failed:
            click.echo(f"⚠ Failed to install: {', '.join(failed)}")
    
    def install_all(self, env_name: str = None, create_shortcuts: bool = True):
        """Install complete Geo Distribution"""
        if env_name is None:
            env_name = GeoDistroConfig.ENV_NAME
        
        click.echo("🚀 Starting Geo Distribution Installation")
        click.echo("=" * 50)
        
        # Create environment
        if not self.create_environment(env_name):
            return False
        
        # Install all package categories
        all_packages = GeoDistroConfig.get_all_packages()
        
        for category, packages in all_packages.items():
            self.install_packages(env_name, category, packages)
            time.sleep(1)  # Brief pause between categories
        
        # Post-installation setup
        self._setup_jupyter_extensions(env_name)
        
        if create_shortcuts:
            self._create_shortcuts(env_name)
        
        click.echo("\n🎉 Installation Complete!")
        click.echo("=" * 50)
        click.echo(f"Environment: {env_name}")
        click.echo("\nTo activate:")
        click.echo(f"  conda activate {env_name}")
        click.echo("\nTo start Jupyter Lab:")
        click.echo("  jupyter lab")
        
        return True
    
    def _setup_jupyter_extensions(self, env_name: str):
        """Setup Jupyter extensions"""
        click.echo("\n⚙️ Setting up Jupyter extensions...")
        
        extensions = [
            "jupyterlab-geojson",
            "jupyterlab-kernelspy"
        ]
        
        for ext in extensions:
            if self.system == "windows":
                cmd = f"conda activate {env_name} && jupyter labextension install {ext}"
                subprocess.run(["cmd", "/c", cmd], capture_output=not self.verbose)
            else:
                cmd = f"source activate {env_name} && jupyter labextension install {ext}"
                subprocess.run(["bash", "-c", cmd], capture_output=not self.verbose)
    
    def _create_shortcuts(self, env_name: str):
        """Create desktop shortcuts"""
        click.echo("\n📝 Creating shortcuts...")
        
        shortcuts_dir = Path.home() / "GeoDistribution"
        shortcuts_dir.mkdir(exist_ok=True)
        
        # Create Jupyter Lab starter script
        if self.system == "windows":
            bat_content = f"""@echo off
call conda activate {env_name}
jupyter lab
pause
"""
            bat_file = shortcuts_dir / "GeoJupyterLab.bat"
            bat_file.write_text(bat_content)
        else:
            script_content = f"""#!/bin/bash
conda activate {env_name}
jupyter lab
"""
            script_file = shortcuts_dir / "geojupyterlab.sh"
            script_file.write_text(script_content)
            script_file.chmod(0o755)