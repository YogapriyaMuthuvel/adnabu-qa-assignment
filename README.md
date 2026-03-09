# AdNabu QA Assignment

## Overview
This repository contains my submission for the **Quality Assurance Engineer Assignment** at **AdNabu**.

The assignment includes:
- Writing manual test cases for **Product Search** and **Add to Cart**
- Automating a scenario to **search for a product and add it to the cart successfully** using **Python and Selenium**

---

## Manual Test Cases
The manual test cases are documented in the Excel file:

**AdNabu_QA_TestCases.xlsx**

The test cases cover:
- Positive scenarios
- Negative scenarios
- Edge cases

Modules covered:
- Product Search
- Add to Cart

---

## Automated Test Scenario
The following scenario is automated:

**Search for a product and add it to the cart successfully**

### Steps:
1. Open the AdNabuTestStore website
2. Enter the store password
3. Search for a product
4. Select the product from search results
5. Click **Add to Cart**
6. Verify that the product is added to the cart

---

## Tech Stack
- Python
- Selenium WebDriver
- PyTest
- WebDriver Manager
- PyTest HTML Report

---

## Files in this Repository
test_product_search_add_to_cart.py # Selenium automation script
AdNabu_QA_TestCases.xlsx # Manual test cases
requirements.txt # Python dependencies
report.html # Generated test report
README.md # Project documentation


---

## Setup Instructions

### 1. Clone the Repository
git clone <https://github.com/YogapriyaMuthuvel/adnabu-qa-assignment>



### 2. Create Virtual Environment
python -m venv venv

Activate the environment:

**Windows**
venv\Scripts\activate

**Mac/Linux**
source venv/bin/activate


---

### 3. Install Dependencies
pip install -r requirements.txt

---

## Run the Test

Execute the test using:pytest
---

## Generate HTML Test Report
pytest --html=report.html


Open the report in a browser to view the results.

---

## Notes
- Explicit waits are used instead of hardcoded sleeps.
- Code is written to be readable and maintainable.
- WebDriver Manager is used to automatically manage browser drivers.