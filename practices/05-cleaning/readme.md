# Practice Exercises for Cleaning up Data

## Overview

In this section, you'll have a chance to practice the concepts of data cleaning with Python and pandas. We'll be using the heart disease dataset for the exercises. First, review the core concepts covered. Then, proceed to the exercises below.

Remember, these exercises aim to enhance your understanding. If you're unable to solve a particular challenge, it might be helpful to revisit the related content.

## Core Concepts

### 1. Reading Multiple CSVs with `glob`

Using `glob`, you can fetch filenames matching a specified pattern, which is useful when you need to load multiple CSV files into a DataFrame.

### 2. Examine DataFrame

Understanding the data by examining the columns, data types, and basic statistics is crucial before processing it.

### 3. Data Transformation with `assign` and `astype`

Pandas provides various functions like `assign` and `astype` to modify the dataset. 

### 4. Memory Usage

Datasets can be large, so knowing the memory usage and optimizing it is essential.

### 5. Custom Functions for Cleaning

You can define custom functions to streamline the cleaning of specific columns.

---

## Exercises

### 1. Load and Examine

- Use the `glob` library to find all the CSVs in the `data` directory matching the pattern `processed*.data`.
- Load all these CSVs into a single DataFrame.
- Display the first 5 rows of the DataFrame.

### 2. Data Inspection

- Use the `.dtypes` attribute to list the data types of all columns.
- Identify columns with `object` or `string` data types and check their unique values.

### 3. Data Transformation

- Convert the `age` column to data type `int8` and examine its distribution using a histogram.
- Replace values in the `sex` column: `1.0` to 'male' and `0.0` to 'female'. Then, check the counts of each gender.

### 4. Memory Check

- Calculate the memory usage of the initial DataFrame.
- After converting `age` to `int8` and `sex` to `string`, calculate the memory usage again.
- Comment on the difference.

### 5. Function Creation and Application

- Create a function named `clean_column` that replaces '?' with `np.nan`, converts the column to float and then to a given data type.
- Apply this function to the `thalach` column and set its type to `int16`.
  
### 6. Challenge Exercise

Using the knowledge gained:

- Write a function named `clean_data` that:
    - Converts multiple columns to their respective datatypes.
    - Replaces specific values across multiple columns.
    - Returns the cleaned DataFrame.
- Test your function on the heart disease dataset.
