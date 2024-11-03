# COVID-19 Data Analysis in South Korea

This project aims to analyze and clean COVID-19-related datasets specific to South Korea, exploring various aspects such as case distribution, patient information, time trends, demographics, and government policies. The analysis is performed on multiple dataframes, each focusing on specific aspects of the pandemic in South Korea.

## Setup Guide

Follow these steps to set up the project environment using `pyproject.toml` and a virtual environment (`venv`):

1. **Clone the Repository**

```bash
git clone https://github.com/vytautas-bunevicius/covid19-south-korea-analysis.git
```

1. **Navigate to Repository Directory**

```bash
cd covid19-south-korea-analysis
```

1. **Create a Virtual Environment**

```bash
python3 -m venv venv
```

1. **Activate the Virtual Environment**

- **On macOS and Linux:**

```bash
source venv/bin/activate
```

- **On Windows:**

```bash
venv\Scripts\activate
```

1. **Upgrade `pip`**

```bash
pip install --upgrade pip
```

1. **Install the Required Python Packages**

- Install dependencies using `pyproject.toml`:

```bash
pip install .
```

1. **Launch Jupyter Notebook**

```bash
jupyter notebook
```

## Exploratory Data Analysis

The Jupyter Notebook contains a comprehensive analysis addressing the following questions:

### 1) Case DataFrame Analysis

#### Case Analysis Questions

1. What are the most affected regions or cities?
2. How many cases are group infections?
3. What are the common infection cases?
4. Explore the geographical distribution of cases.

#### Case Data Cleaning Steps

- Check for missing values
- Ensure the correctness of the `case_id` format
- Handle any outliers in the `confirmed` column

### 2) Patient Information Analysis

#### Patient Data Questions

1. What is the distribution of patients by age and sex?
2. How many cases are related to overseas inflow?
3. Explore the timeline of patient states (isolated, released, deceased)

#### Patient Data Cleaning Steps

- Handle missing values in key columns
- Check and handle duplicate rows
- Correct data types for date columns

### 3) Time Series Analysis

#### Time Series Questions

1. What is the trend of COVID-19 tests over time?
2. Explore the daily changes in confirmed, released, and deceased cases

#### Time Series Data Cleaning

- Ensure the correctness of date and time formats
- Check for missing values

### 4) Age Distribution Analysis

#### Age Data Questions

1. How does the age distribution of confirmed cases change over time?
2. Explore the number of deceased cases by age group

#### Age Data Cleaning Steps

- Check for missing values
- Ensure the correctness of date and age formats

### 5) Gender Distribution Analysis

#### Gender Data Questions

1. Compare the confirmed and deceased cases between genders over time

#### Gender Data Cleaning Steps

- Check for missing values
- Ensure the correctness of date and gender formats

### 6) Provincial Analysis

#### Provincial Data Questions

1. Explore the confirmed, released, and deceased cases by province over time

#### Provincial Data Cleaning Steps

- Check for missing values
- Ensure the correctness of date and province formats

### 7) Regional Analysis

#### Regional Data Questions

1. Explore the geographical distribution of regions
2. Analyze the relationship between elderly population ratio and confirmed cases

#### Regional Data Cleaning Steps

- Check for missing values
- Ensure the correctness of latitude and longitude formats

### 8) Weather Impact Analysis

#### Weather Data Questions

1. Explore the relationship between weather conditions and the number of confirmed cases

#### Weather Data Cleaning Steps

- Check for missing values
- Ensure the correctness of date and weather-related formats

### 9) Search Trends Analysis

#### Search Data Questions

1. Analyze the search trend for COVID-19-related keywords over time

#### Search Data Cleaning Steps

- Check for missing values
- Ensure the correctness of date formats

### 10) Seoul Population Analysis

#### Population Data Questions

1. Explore the fluctuation in the floating population in Seoul

#### Population Data Cleaning Steps

- Check for missing values
- Ensure the correctness of date and floating population number formats

### 11) Policy Impact Analysis

#### Policy Data Questions

1. Analyze the types and impacts of government policies over time

#### Policy Data Cleaning Steps

- Check for missing values
- Ensure the correctness of date formats

## License

This project is licensed under the [Unlicense](LICENSE).
