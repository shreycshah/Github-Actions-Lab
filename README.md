# Github-Actions-Lab

Professor Lab: https://github.com/raminmohammadi/MLOps/tree/main/Labs/Github_Labs/Lab1

A hands-on laboratory project demonstrating the use of **GitHub Actions** for continuous integration and automated testing of Python applications. This repository showcases how to build CI/CD pipelines that automatically test a `Calculator` and `FinancialCalculator` module on every push or pull request.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [CI/CD Pipeline](#cicd-pipeline)

---

## Overview

This project serves as a practical reference for integrating **GitHub Actions** into a Python development workflow. It includes two core modules: a general-purpose `Calculator` and a domain-specific `FinancialCalculator` (created by me), each backed by a suite of unit tests that are automatically triggered via GitHub Actions on every code change.

The primary objective is to demonstrate how CI/CD automation catches regressions early, enforces test coverage, and streamlines the development lifecycle without any manual intervention.

---

## Features

- **Calculator** — Supports standard arithmetic operations: addition, subtraction, multiplication, and division.
- **FinancialCalculator** — Supports financial computations such as simple interest, compound interest etc.
- **Automated Testing** — Unit tests for both classes are automatically executed via GitHub Actions on every push and pull request.

### Changes made by me:
- Implemented a new FinancialCalculator class
- Wrote pytest & unittest for Calculator & FinancialCalculator class
- Added CI/CD workflow using GitHub Actions.
- 
---

## Project Structure

```
Github-Actions-Lab/
├── .github/
│   └── workflows/
│       ├── pytest_action.yml         # GitHub Actions CI workflow for pytest
│       └── unittest_action.yml       # GitHub Actions CI workflow for unittest
├── src/
│   ├── calculator.py                 # Basic Calculator class
│   └── financial_calculator.py      # FinancialCalculator class
├── test/
│   ├── test_calculator.py            # Unit tests for Calculator
│   └── test_financial_calculator.py # Unit tests for FinancialCalculator
├── data/                             # Sample data files
├── workflows/                        # Workflow scripts
├── requirements.txt                  # Python dependencies
└── README.md
```

---

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git

### Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/shreycshah/Github-Actions-Lab.git
   cd Github-Actions-Lab
   ```

2. **Create and activate a virtual environment** *(recommended)*

   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

### Running Tests Locally

```bash
pytest test/ -v
```

---

## CI/CD Pipeline

This repository uses **GitHub Actions** to automate testing on every push and pull request to `main`.

The workflow performs the following steps:

1. **Checkout Code** — Pulls the latest code from the repository.
2. **Set Up Python** — Configures the specified Python version.
3. **Install Dependencies** — Installs all packages listed in `requirements.txt`.
4. **Run Tests** — Executes the full test suite for both `Calculator` and `FinancialCalculator` using `pytest`.

Any test failure will immediately flag the workflow run as failed, preventing unstable code from being merged into `main`.
