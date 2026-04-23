# Base image with Python
FROM mcr.microsoft.com/devcontainers/python:3.12-bullseye

EXPOSE 8000
    
# Install system dependencies
# graphviz → required for many Sphinx diagrams
# openjdk-17 → needed if you want PlantUML diagrams
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        graphviz \
        openjdk-17-jre-headless \
        make \
        git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set work directory
# WORKDIR /workspace

# Install Sphinx + ReadTheDocs theme + useful extensions
RUN pip install --no-cache-dir \
    sphinx \
    sphinx-rtd-theme \
    myst-parser \
    sphinx-autobuild \
    sphinxcontrib-mermaid \
    sphinxcontrib-plantuml \
    sphinx-copybutton \
    sphinx-design

# Environment variables for PlantUML
ENV PLANTUML_JAR=/usr/share/plantuml/plantuml.jar

# Create an entry to easily run sphinx-autobuild
CMD [ "bash" ]
