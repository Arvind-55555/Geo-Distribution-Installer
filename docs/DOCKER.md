# 🐳 Docker Usage Guide for Geo-Distro

## Overview

The Geo-Distro Docker container provides a lightweight CLI tool for installing and managing geospatial Python libraries. The container is published to GitHub Container Registry (ghcr.io).

## Quick Start

### Pull the Container

```bash
docker pull ghcr.io/arvind-55555/geo-distribution-installer:latest
```

### Basic Usage

```bash
# Show help
docker run --rm ghcr.io/arvind-55555/geo-distribution-installer:latest --help

# Show package information
docker run --rm ghcr.io/arvind-55555/geo-distribution-installer:latest info

# Verify installation (if geo-distro is installed on host)
docker run --rm ghcr.io/arvind-55555/geo-distribution-installer:latest verify
```

## Installation Methods

### Method 1: Using Docker as a CLI Tool

Run geo-distro commands directly from the container:

```bash
# Create an alias for convenience
alias geo-distro='docker run --rm -v $(pwd):/workspace ghcr.io/arvind-55555/geo-distribution-installer:latest'

# Now use it like a regular command
geo-distro info
geo-distro --help
```

### Method 2: Interactive Shell

Enter the container for interactive use:

```bash
docker run -it --rm --entrypoint /bin/bash ghcr.io/arvind-55555/geo-distribution-installer:latest

# Inside the container
geo-distro info
geo-distro --help
```

### Method 3: Mount Host Directory

Mount your project directory to work with local files:

```bash
docker run --rm -v $(pwd):/workspace -w /workspace \
  ghcr.io/arvind-55555/geo-distribution-installer:latest info
```

## Available Tags

- `latest` - Latest stable release
- `v0.1.0` - Specific version
- `main` - Latest build from main branch
- `main-<sha>` - Specific commit from main branch

## Advanced Usage

### Using with Docker Compose

Create a `docker-compose.yml`:

```yaml
version: '3.8'

services:
  geo-distro:
    image: ghcr.io/arvind-55555/geo-distribution-installer:latest
    volumes:
      - ./:/workspace
    working_dir: /workspace
```

Run commands:

```bash
docker-compose run --rm geo-distro info
docker-compose run --rm geo-distro --help
```

### Building Locally

```bash
# Clone the repository
git clone https://github.com/Arvind-55555/Geo-Distribution-Installer.git
cd Geo-Distribution-Installer

# Build the image
docker build -t geo-distro:local .

# Run the local image
docker run --rm geo-distro:local --help
```

### Multi-Platform Support

The container is built for multiple platforms:
- `linux/amd64` (Intel/AMD 64-bit)
- `linux/arm64` (ARM 64-bit, Apple Silicon)

Docker will automatically pull the correct image for your platform.

## Use Cases

### 1. CI/CD Pipeline

Use in GitHub Actions or other CI systems:

```yaml
jobs:
  check-geo-libs:
    runs-on: ubuntu-latest
    container:
      image: ghcr.io/arvind-55555/geo-distribution-installer:latest
    steps:
      - name: Check geo-distro info
        run: geo-distro info
```

### 2. Development Environment

Use as a development tool without installing on host:

```bash
# Add to your shell profile (~/.bashrc or ~/.zshrc)
alias geo-distro='docker run --rm -v $(pwd):/workspace ghcr.io/arvind-55555/geo-distribution-installer:latest'
```

### 3. Testing Different Versions

Test different versions easily:

```bash
docker run --rm ghcr.io/arvind-55555/geo-distribution-installer:v0.1.0 info
docker run --rm ghcr.io/arvind-55555/geo-distribution-installer:latest info
```

## Container Details

### Image Information

- **Base Image**: `python:3.11-slim`
- **Size**: ~200-250MB
- **User**: Runs as non-root user `geodistro` (UID 1000)
- **Working Directory**: `/app`
- **Entrypoint**: `geo-distro`

### Included Components

- Python 3.11
- geo-distro CLI tool
- All Python dependencies (click, requests, tqdm, pyyaml)
- Git, curl, ca-certificates

### Security

- Runs as non-root user for security
- Minimal base image (python:3.11-slim)
- No unnecessary packages installed
- Regular security updates via base image

## Troubleshooting

### Permission Issues

If you encounter permission issues with mounted volumes:

```bash
# Run with your user ID
docker run --rm --user $(id -u):$(id -g) \
  -v $(pwd):/workspace \
  ghcr.io/arvind-55555/geo-distribution-installer:latest info
```

### Container Not Found

Ensure you're logged in to GitHub Container Registry:

```bash
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin
```

For public images, login is not required.

### Network Issues

If you're behind a proxy:

```bash
docker run --rm \
  -e HTTP_PROXY=http://proxy.example.com:8080 \
  -e HTTPS_PROXY=http://proxy.example.com:8080 \
  ghcr.io/arvind-55555/geo-distribution-installer:latest info
```

## Examples

### Example 1: Check Package Info

```bash
docker run --rm ghcr.io/arvind-55555/geo-distribution-installer:latest info
```

### Example 2: Use in a Script

```bash
#!/bin/bash
# check-geo-setup.sh

echo "Checking geo-distro information..."
docker run --rm ghcr.io/arvind-55555/geo-distribution-installer:latest info

echo "Done!"
```

### Example 3: Integration with Makefile

```makefile
.PHONY: geo-info
geo-info:
	docker run --rm ghcr.io/arvind-55555/geo-distribution-installer:latest info

.PHONY: geo-verify
geo-verify:
	docker run --rm ghcr.io/arvind-55555/geo-distribution-installer:latest verify
```

## Links

- **Container Registry**: https://github.com/Arvind-55555/Geo-Distribution-Installer/pkgs/container/geo-distribution-installer
- **Source Code**: https://github.com/Arvind-55555/Geo-Distribution-Installer
- **PyPI Package**: https://pypi.org/project/geo-distro/
- **Documentation**: https://github.com/Arvind-55555/Geo-Distribution-Installer#readme

## Support

For issues or questions:
- **GitHub Issues**: https://github.com/Arvind-55555/Geo-Distribution-Installer/issues
- **Discussions**: https://github.com/Arvind-55555/Geo-Distribution-Installer/discussions

## License

MIT License - See [LICENSE](../LICENSE) for details.
