# AdNabu QA Automation Assignment

## Overview
This repository contains my submission for the **Quality Assurance Engineer Assignment at AdNabu**.

The assignment includes:

- Writing **manual test cases** for Product Search and Add to Cart.
- Automating a scenario to **search for a product and successfully add it to the cart** using **Python and Selenium**.

---

## Manual Test Cases

The manual test cases for **Product Search** and **Add to Cart** are documented in a Google Sheet.

The sheet includes:
- Positive scenarios
- Negative scenarios
- Edge cases

The Google Sheet link has been shared in the assignment submission email.

---

## Automated Test Scenario

The following scenario is automated:

**Search for a product and add it to the cart successfully**

### Steps Automated

1. Open the AdNabu Test Store website  
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

## Project Structure

```
adnabu-qa-assignment
│
├── test_product_search_add_to_cart.py   # Selenium automation script
├── requirements.txt                        # Python dependencies
├── report.html                             # Generated test report
├── README.md                               # Project documentation
└── .gitignore
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YogapriyaMuthuvel/adnabu-qa-assignment
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Test

Execute the test using:

```bash
pytest
```

---

## Generate HTML Test Report

```bash
pytest --html=report.html
```

After execution, open **report.html** in a browser to view the test results.

---

## Notes

- Explicit waits are used instead of hardcoded `sleep()` to improve reliability.
