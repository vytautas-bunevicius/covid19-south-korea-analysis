# COVID-19 Data Analysis in South Korea

This project aims to analyze and clean COVID-19-related datasets specific to South Korea, exploring various aspects such as case distribution, patient information, time trends, demographics, and government policies. The analysis is performed on multiple dataframes, each focusing on specific aspects of the pandemic in South Korea.

## Table of Contents

- [Setup Guide](#setup-guide)
  - [Clone the Repository](#clone-the-repository)
  - [Navigate to Repository Directory](#navigate-to-repository-directory)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Activate the Virtual Environment](#activate-the-virtual-environment)
    - [On macOS and Linux](#on-macos-and-linux)
    - [On Windows](#on-windows)
  - [Upgrade `pip`](#upgrade-pip)
  - [Install the Required Python Packages](#install-the-required-python-packages)
  - [Launch Jupyter Notebook](#launch-jupyter-notebook)
- [Exploratory Data Analysis](#exploratory-data-analysis)
  - [Case DataFrame Analysis](#case-dataframe-analysis)
    - [Case Analysis Questions](#case-analysis-questions)
    - [Case Data Cleaning Steps](#case-data-cleaning-steps)
  - [Patient Information Analysis](#patient-information-analysis)
    - [Patient Data Questions](#patient-data-questions)
    - [Patient Data Cleaning Steps](#patient-data-cleaning-steps)
  - [Time Series Analysis](#time-series-analysis)
    - [Time Series Questions](#time-series-questions)
    - [Time Series Data Cleaning](#time-series-data-cleaning)
  - [Age Distribution Analysis](#age-distribution-analysis)
    - [Age Data Questions](#age-data-questions)
    - [Age Data Cleaning Steps](#age-data-cleaning-steps)
  - [Gender Distribution Analysis](#gender-distribution-analysis)
    - [Gender Data Questions](#gender-data-questions)
    - [Gender Data Cleaning Steps](#gender-data-cleaning-steps)
  - [Provincial Analysis](#provincial-analysis)
    - [Provincial Data Questions](#provincial-data-questions)
    - [Provincial Data Cleaning Steps](#provincial-data-cleaning-steps)
  - [Regional Analysis](#regional-analysis)
    - [Regional Data Questions](#regional-data-questions)
    - [Regional Data Cleaning Steps](#regional-data-cleaning-steps)
  - [Weather Impact Analysis](#weather-impact-analysis)
    - [Weather Data Questions](#weather-data-questions)
    - [Weather Data Cleaning Steps](#weather-data-cleaning-steps)
  - [Search Trends Analysis](#search-trends-analysis)
    - [Search Data Questions](#search-data-questions)
    - [Search Data Cleaning Steps](#search-data-cleaning-steps)
  - [Seoul Population Analysis](#seoul-population-analysis)
    - [Population Data Questions](#population-data-questions)
    - [Population Data Cleaning Steps](#population-data-cleaning-steps)
  - [Policy Impact Analysis](#policy-impact-analysis)
    - [Policy Data Questions](#policy-data-questions)
    - [Policy Data Cleaning Steps](#policy-data-cleaning-steps)
- [Testing](#testing)
  - [Testing Framework](#testing-framework)
  - [Running the Tests](#running-the-tests)
    - [Ensure the Virtual Environment is Activated](#ensure-the-virtual-environment-is-activated)
    - [Navigate to the Project Root Directory](#navigate-to-the-project-root-directory)
    - [Run the Tests Using pytest](#run-the-tests-using-pytest)
      - [Verbose Output](#verbose-output)
      - [Run Specific Test Files or Functions](#run-specific-test-files-or-functions)
      - [Generate a Test Coverage Report](#generate-a-test-coverage-report)
- [License](#license)
- [Additional Recommendations](#additional-recommendations)

## Setup Guide

Follow these steps to set up the project environment using `pyproject.toml` and a virtual environment (`venv`):

### Clone the Repository

```bash
git clone https://github.com/vytautas-bunevicius/covid19-south-korea-analysis.git
```

### Navigate to Repository Directory

```bash
cd covid19-south-korea-analysis
```

### Create a Virtual Environment

```bash
python3 -m venv venv
```

### Activate the Virtual Environment

- **On macOS and Linux:**

  ```bash
  source venv/bin/activate
  ```

- **On Windows:**

  ```bash
  venv\Scripts\activate
  ```

### Upgrade `pip`

```bash
pip install --upgrade pip
```

### Install the Required Python Packages

- Install dependencies using `pyproject.toml`:

  ```bash
  pip install .
  ```

### Launch Jupyter Notebook

```bash
jupyter notebook
```

## Exploratory Data Analysis

The Jupyter Notebook contains a comprehensive analysis addressing the following questions:

### Case DataFrame Analysis

#### Case Analysis Questions

1. What are the most affected regions or cities?
2. How many cases are group infections?
3. What are the common infection cases?
4. Explore the geographical distribution of cases.

#### Case Data Cleaning Steps

- Check for missing values
- Ensure the correctness of the `case_id` format
- Handle any outliers in the `confirmed` column

### Patient Information Analysis

#### Patient Data Questions

1. What is the distribution of patients by age and sex?
2. How many cases are related to overseas inflow?
3. Explore the timeline of patient states (isolated, released, deceased)

#### Patient Data Cleaning Steps

- Handle missing values in key columns
- Check and handle duplicate rows
- Correct data types for date columns

### Time Series Analysis

#### Time Series Questions

1. What is the trend of COVID-19 tests over time?
2. Explore the daily changes in confirmed, released, and deceased cases

#### Time Series Data Cleaning

- Ensure the correctness of date and time formats
- Check for missing values

### Age Distribution Analysis

#### Age Data Questions

1. How does the age distribution of confirmed cases change over time?
2. Explore the number of deceased cases by age group

#### Age Data Cleaning Steps

- Check for missing values
- Ensure the correctness of date and age formats

### Gender Distribution Analysis

#### Gender Data Questions

1. Compare the confirmed and deceased cases between genders over time

#### Gender Data Cleaning Steps

- Check for missing values
- Ensure the correctness of date and gender formats

### Provincial Analysis

#### Provincial Data Questions

1. Explore the confirmed, released, and deceased cases by province over time

#### Provincial Data Cleaning Steps

- Check for missing values
- Ensure the correctness of date and province formats

### Regional Analysis

#### Regional Data Questions

1. Explore the geographical distribution of regions
2. Analyze the relationship between elderly population ratio and confirmed cases

#### Regional Data Cleaning Steps

- Check for missing values
- Ensure the correctness of latitude and longitude formats

### Weather Impact Analysis

#### Weather Data Questions

1. Explore the relationship between weather conditions and the number of confirmed cases

#### Weather Data Cleaning Steps

- Check for missing values
- Ensure the correctness of date and weather-related formats

### Search Trends Analysis

#### Search Data Questions

1. Analyze the search trend for COVID-19-related keywords over time

#### Search Data Cleaning Steps

- Check for missing values
- Ensure the correctness of date formats

### Seoul Population Analysis

#### Population Data Questions

1. Explore the fluctuation in the floating population in Seoul

#### Population Data Cleaning Steps

- Check for missing values
- Ensure the correctness of date and floating population number formats

### Policy Impact Analysis

#### Policy Data Questions

1. Analyze the types and impacts of government policies over time

#### Policy Data Cleaning Steps

- Check for missing values
- Ensure the correctness of date formats

## Testing

Ensuring the reliability and correctness of our data loading and processing functions is crucial. This project includes a comprehensive suite of unit tests designed to validate the core functionalities. Below is an overview of the testing framework and how to execute the tests.

### Testing Framework

- **Testing Library:** [pytest](https://docs.pytest.org/en/7.1.x/)
- **Mocking:** Utilizes `unittest.mock` for simulating file operations and environments.
- **Test Coverage:**
  - **Data Loading:**
    - Successful loading of CSV files.
    - Handling of corrupted or improperly formatted CSV files.
  - **Global Variable Assignments:**
    - Verification of global variable assignments when enabled.
  - **Dataset Information Retrieval:**
    - Accuracy of functions that retrieve and summarize dataset information.
  - **Edge Cases:**
    - Testing with empty datasets or unexpected input formats.

### Running the Tests

To run the unit tests, follow these steps:

1. **Ensure the Virtual Environment is Activated**

   Make sure you've activated the virtual environment as per the [Setup Guide](#setup-guide).

2. **Navigate to the Project Root Directory**

   Ensure you're in the root directory of the project where the `tests` folder is located.

3. **Run the Tests Using pytest**

   Execute the following command to run all tests:

   ```bash
   pytest
   ```

   **Additional Options:**

   - **Verbose Output:**

     To see more detailed test results, use the `-v` flag:

     ```bash
     pytest -v
     ```

   - **Run Specific Test Files or Functions:**

     To run a specific test file:

     ```bash
     pytest tests/test_utils.py
     ```

     To run a specific test function within a file:

     ```bash
     pytest tests/test_utils.py::test_load_covid_data_successful
     ```

   - **Generate a Test Coverage Report:**

     If you want to check the test coverage, install `pytest-cov`:

     ```bash
     pip install pytest-cov
     ```

     Then run:

     ```bash
     pytest --cov=src tests/
     ```

     This will display a coverage report in the terminal. For an HTML report, use:

     ```bash
     pytest --cov=src --cov-report=html tests/
     ```

     The HTML report will be available in the `htmlcov` directory.

## License

This project is licensed under the [Unlicense](LICENSE).
