# **Car Valuation E2E Test Suite**

This project is an end-to-end (E2E) automation test suite designed to validate vehicle details fetched from a car valuation website against expected results using a **Behavior-Driven Development (BDD)** approach. 

The framework uses **Python**, **Selenium**, and **pytest-bdd**, and is set up for seamless integration with **Jenkins**.

---

## **Table of Contents**

- [Features](#features)
- [Folder Structure](#folder-structure)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running Tests Locally](#running-tests-locally)
  - [Jenkins Pipeline](#jenkins-pipeline)
- [How It Works](#how-it-works)
  - [Input File](#input-file)
  - [Output File](#output-file)
- [Extensibility](#extensibility)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)

---

## **Features**

- Extracts car registration numbers from a text file.
- Fetches car details from a live car valuation website (e.g., [Motorway](https://motorway.co.uk/)).
- Compares fetched car details with expected results in a CSV file.
- Follows the **BDD approach** using Gherkin syntax for test scenarios.
- Modular and extensible structure for easy integration with additional input files or websites.
- Generates detailed test reports in HTML format.
- Compatible with CI/CD pipelines (e.g., Jenkins).

---

## **Folder Structure**

```
project_root/
│
├── features/                     # Gherkin feature files
│   ├── car_valuation.feature
│
├── steps/                        # Step definitions for BDD
│   ├── car_valuation_steps.py
│
├── src/                          # Core modules
│   ├── car_extractor.py          # Extracts registration numbers from input file
│   ├── car_valuation_api.py      # Interacts with the car valuation website
│   ├── data_comparator.py        # Compares fetched and expected car details
│   ├── utils.py                  # Utility functions
│
├── data/                         # Input and output files
│   ├── car_input.txt             # Input file with car registration numbers
│   ├── car_output.txt            # Expected car details for validation
│
├── reports/                      # Test reports
│   ├── test_report.html
│
├── Jenkinsfile                   # Jenkins pipeline configuration
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## **Setup Instructions**

### **Prerequisites**

1. **Python 3.8+** installed on your machine.
2. **Google Chrome** and **ChromeDriver** installed and added to your system's PATH.
3. Optionally, a working **Jenkins** instance for CI/CD.

---

### **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**

### **Running Tests Locally**

1. Ensure the `data/car_input.txt` and `data/car_output.txt` files are updated with your input and expected values.

2. Run the tests with:
   ```bash
   pytest --gherkin-terminal-reporter --html=reports/test_report.html --self-contained-html
   ```

3. The test report will be generated in the `reports/` folder as `test_report.html`.

### **Jenkins Pipeline**

1. Use the provided `Jenkinsfile` to configure your Jenkins pipeline.
2. Set up a Jenkins job and point it to this repository.
3. Jenkins will:
   - Install dependencies.
   - Run the tests.
   - Generate and archive the test report.

---

## **How It Works**

### **Input File**

The `data/car_input.txt` file contains plain text with embedded car registration numbers. Example:

```
Checking example BMW with registration AD58 VNF the value of the car is roughly around £3000.
However, car with registration BW57 BOW is not worth much in the current market.
```

### **Output File**

The `data/car_output.txt` file is a CSV containing expected car details. Example:

```
VARIANT_REG,MAKE,MODEL,YEAR
SG18HTN,Volkswagen,Golf 1.5 TSI EVO SE Nav SG18 HTN,2018
AD58VNF,BMW,1 SERIES DIESEL COUPE - 120d M Sport 2dr,2008
BW57BOF,TOYOTA,YARIS HATCHBACK - 1.0 VVT-i T2 3dr,2008
```

---

## **Extensibility**

- To add more input files, simply place them in the `data/` folder and update the `car_valuation.feature` file with the new file paths.
- You can extend the `src/car_valuation_api.py` module to support additional car valuation websites.
- Easily add more scenarios to `features/car_valuation.feature` for new test cases.

---

## **Tech Stack**

- **Python**: Core programming language.
- **Selenium**: Browser automation for fetching car details.
- **pytest-bdd**: Framework for BDD-style testing.
- **pytest-html**: Test report generation.
- **Jenkins**: CI/CD integration.

---

## **Contributing**

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature/new-feature
   ```
5. Open a Pull Request.
