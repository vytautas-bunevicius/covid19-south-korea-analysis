# COVID-19 Data Analysis in South Korea

This project aims to analyze and clean COVID-19-related datasets specific to South Korea, exploring various aspects such as case distribution, patient information, time trends, demographics, and government policies. The analysis is performed on multiple dataframes, each focusing on specific aspects of the pandemic in South Korea.

## Setup Guide

- Clone the Repository

            git clone https://github.com/vytautas-bunevicius/covid19-south-korea-analysis.git

- Navigate to Repository Directory

            cd covid19-south-korea-analysis

- Install the required Python packages using the following command:

            pip install -r requirements.txt
  
- Launch Jupyter Notebook

            jupyter notebook


## Exploratory Data Analysis:

The Jupyter Notebook contains a comprehensive analysis addressing the following questions:

## 1) Case DataFrame:

### EDA Questions:
1. What are the most affected regions or cities?
2. How many cases are group infections?
3. What are the common infection cases?
4. Explore the geographical distribution of cases.

### Data Cleaning:
- Check for missing values.
- Ensure the correctness of the case_id format.
- Handle any outliers in the confirmed column.

## 2) PatientInfo DataFrame:

### EDA Questions:
1. What is the distribution of patients by age and sex?
2. How many cases are related to overseas inflow?
3. Explore the timeline of patient states (isolated, released, deceased).

### Data Cleaning:
- Handle missing values in key columns.
- Check and handle duplicate rows.
- Correct data types for date columns.

## 3) Time DataFrame:

### EDA Questions:
1. What is the trend of COVID-19 tests over time?
2. Explore the daily changes in confirmed, released, and deceased cases.

### Data Cleaning:
- Ensure the correctness of date and time formats.
- Check for missing values.

## 4) TimeAge DataFrame:

### EDA Questions:
1. How does the age distribution of confirmed cases change over time?
2. Explore the number of deceased cases by age group.

### Data Cleaning:
- Check for missing values.
- Ensure the correctness of date and age formats.

## 5) TimeGender DataFrame:

### EDA Questions:
1. Compare the confirmed and deceased cases between genders over time.

### Data Cleaning:
- Check for missing values.
- Ensure the correctness of date and gender formats.

## 6) TimeProvince DataFrame:

### EDA Questions:
1. Explore the confirmed, released, and deceased cases by province over time.

### Data Cleaning:
- Check for missing values.
- Ensure the correctness of date and province formats.

## 7) Region DataFrame:

### EDA Questions:
1. Explore the geographical distribution of regions.
2. Analyze the relationship between elderly population ratio and confirmed cases.

### Data Cleaning:
- Check for missing values.
- Ensure the correctness of latitude and longitude formats.

## 8) Weather DataFrame:

### EDA Questions:
1. Explore the relationship between weather conditions and the number of confirmed cases.

### Data Cleaning:
- Check for missing values.
- Ensure the correctness of date and weather-related formats.

## 9) SearchTrend DataFrame:

### EDA Questions:
1. Analyze the search trend for COVID-19-related keywords over time.

### Data Cleaning:
- Check for missing values.
- Ensure the correctness of date formats.

## 10) SeoulFloating DataFrame:

### EDA Questions:
1. Explore the fluctuation in the floating population in Seoul.

### Data Cleaning:
- Check for missing values.
- Ensure the correctness of date and floating population number formats.

## 11) Policy DataFrame:

### EDA Questions:
1. Analyze the types and impacts of government policies over time.

### Data Cleaning:
- Check for missing values.
- Ensure the correctness of date formats.
