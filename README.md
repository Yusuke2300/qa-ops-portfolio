# QA Ops E2E Test Automation Framework

An automated End-to-End (E2E) testing framework designed for modern web applications, demonstrating scalable architecture and continuous integration practices.

## 🎯 Overview
This repository serves as a robust E2E test automation framework built with Python and Playwright. It is architected to prioritize maintainability, execution speed, and automated quality reporting, moving beyond simple script execution to a fully integrated QA Ops pipeline.

## 🛠 Tech Stack
- **Language:** Python 3.9+
- **Automation Tool:** Playwright
- **Testing Framework:** Pytest
- **Design Pattern:** Page Object Model (POM)
- **CI/CD:** GitHub Actions
- **Reporting:** pytest-html

## 🏗 Architecture & Key Features

### 1. Page Object Model (POM)
UI interactions and element locators are strictly separated from test logic. This encapsulation ensures that any future UI changes require updates in only one place, significantly reducing maintenance overhead.
- `login_page.py`: Defines locators and page-specific actions.
- `test_login.py`: Contains only the test procedures and assertions.

### 2. Data-Driven Testing (DDT)
Utilizes `@pytest.mark.parametrize` to execute a single test logic against multiple sets of data. This approach maximizes test coverage while keeping the codebase DRY (Don't Repeat Yourself).

### 3. Advanced UI Interactions & Dynamic Waits
- **Bypassing OS Dialogs:** File uploads are handled directly via DOM manipulation (`set_input_files`), avoiding flaky OS-level window interactions.
- **Dynamic Waiting:** Implemented Playwright's auto-wait capabilities alongside explicit state assertions (`to_be_visible(timeout=...)`) to handle network latency and dynamic DOM rendering without resorting to hardcoded sleeps.

### 4. CI/CD Pipeline Integration
A fully automated GitHub Actions workflow (`playwright.yml`) is triggered on every push to the `main` branch.
- Provisions a headless Ubuntu runner.
- Installs dependencies and Playwright browsers.
- Executes the entire test suite.
- Generates a standalone HTML report and uploads it as a downloadable CI artifact.

## 🚀 How to Run Locally

### Prerequisites
Ensure Python 3.9+ is installed on your machine.

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/YourUsername/qa-ops-portfolio.git](https://github.com/YourUsername/qa-ops-portfolio.git)
   cd qa-ops-portfolio