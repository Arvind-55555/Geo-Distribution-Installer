# Geo-Distro CLI - Lightweight Docker Container
# This container provides the geo-distro CLI tool for installing geospatial libraries

FROM python:3.11-slim

# Set metadata
LABEL org.opencontainers.image.title="Geo-Distro CLI"
LABEL org.opencontainers.image.description="Lightweight CLI tool for installing geospatial Python libraries"
LABEL org.opencontainers.image.authors="Arvind <arvind.saane.111@gmail.com>"
LABEL org.opencontainers.image.source="https://github.com/Arvind-55555/Geo-Distribution-Installer"
LABEL org.opencontainers.image.licenses="MIT"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set working directory
WORKDIR /app

# Install system dependencies (minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy only necessary files for installation
COPY pyproject.toml README.md LICENSE ./
COPY src/ ./src/
COPY requirements.txt ./

# Install the package
RUN pip install --no-cache-dir -e .

# Create a non-root user
RUN useradd -m -u 1000 geodistro && \
    chown -R geodistro:geodistro /app

# Switch to non-root user
USER geodistro

# Set the entrypoint to the CLI
ENTRYPOINT ["geo-distro"]

# Default command shows help
CMD ["--help"]
