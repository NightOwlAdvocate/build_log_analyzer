# Build Log Analyzer

A small Python command-line tool for analysing build logs from software projects. Сan be used in CI pipelines to fail the build when compiler errors or failed tests are detected.

Detects:
- compiler errors
- compiler warnings
- failed tests
- summary statistics

## Purpose of this project

Experimenting in software tooling, building analysis, CI/CD workflows, and quality-oriented software development. Was inspired by tasks in embedded software teams.

## Technologies

- Python
- Pytest
- GitHub Actions
- CLI tooling
- Basic build/test log analysis

## Usage

```bash
python build_log_analyzer.py sample_logs/failed_build.log
```

## To run the test

```bash
python3 -m pytest
