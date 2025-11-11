# Exercise 2 — Coverage Analysis

## Overview
This exercise focuses on improving and analyzing **test coverage** for Python functions using **pytest** and **pytest-cov**.  
Coverage reports help identify untested lines or branches and guide improvements toward higher test completeness.

---

## Setup
Install the required packages:
```bash
pip install pytest pytest-cov

##To view coverage stats, go to the required directory and run this:
python -m pytest -p pytest_cov --cov=. --cov-branch --cov-report=term-missing -q

## To generate the xml and HTML reports, run this in the directory:
python -m pytest -p pytest_cov --cov=. --cov-branch \                                                  
  --cov-report=html:../coverage_reports/<name>_html \
  --cov-report=xml:../coverage_reports/<name>_coverage.xml -q
