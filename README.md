# Build Log Analyzer

A command-line tool for extracting actionable information from software build logs. Detects compiler errors, warnings, and failed tests. Groups them by category. Prints a structured summary that can be used by developers or CI pipelines.

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
```
