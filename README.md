# yt-knowledge-pipeline

A professional learning project to extract, store, and later process YouTube transcripts.

## Current version

V0: local transcript extraction script

## Goal

This project starts as a simple local script and will evolve into a cloud-native pipeline with:

- API
- queue
- workers
- storage
- observability
- Kubernetes
- Terraform

## Project structure

```text
src/        Python package
scripts/    entrypoint scripts
outputs/    generated transcript files
tests/      tests
```

## Installation

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .

## Usage
python scripts/get_transcript.py "https://www.youtube.com/watch?v=VIDEO_ID"

Roadmap
V0: local script
V1: cleaner CLI
V2: FastAPI service
V3: queue + workers
V4: Kubernetes + Terraform

