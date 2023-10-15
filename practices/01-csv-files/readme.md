# Practice Exercises: Understanding Student Data - Analysing and Visualizing Data from a CSV file

## Overview

In this set of exercises, you'll have the opportunity to practice the skills you learned in the module about analyzing and visualizing data from a CSV file. The data set used in this module is the "Student Performance Data Set" from [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Student+Performance).

Remember, it's essential to practice your coding skills. The exercises below are structured to help reinforce what you've learned. If an exercise seems challenging, take your time and try to work through it.

## Core Concepts to Review

### Loading CSVs and PyArrow

- You have learned how to load data from CSVs using the `pandas` library. The PyArrow backend can improve speed and memory usage.

### Summary Stats

- Descriptive statistics give a quick snapshot of the data's main properties.

### Correlations

- Correlation measures the strength and direction of the relationship between two numeric variables.

### Cross Tabulations

- Cross-tabulation is a method to quantitatively analyze the relationship between multiple variables.

### Visualizations

- Visualization provides a clear idea of the data's structure and relationships.

## Practice Exercises

1. **Loading Data**
   - Download the "Student Performance Data Set" from the given link and unzip it to retrieve the dataset.
   - Load the dataset `student-mat.csv` into a pandas DataFrame.
   - Display the first five rows of the DataFrame.

2. **Data Overview**
   - Identify and list down the categorical columns in the dataset.
   - Compute and display basic statistics for the numerical columns using the `describe()` method.
   
3. **Correlations**
   - Compute the Pearson correlation for numeric columns.

4. **Cross Tabulations**
   - Create a cross-tabulation between students' school (`school` column) and their desire for higher education (`higher` column).
   - Normalize this cross-tabulation across all cells and format the output as percentages.

5. **Visualizations**
   - Plot a histogram for students' first grades (`G1` column).
   - Create a scatter plot to see the relation between mothers' education (`Medu` column) and students' first grades (`G1` column). Use jitter if necessary.

6. **Bonus: Advanced Visualization**
   - Use jitter and grouping (or color) in a scatter plot to distinguish between students who have internet access at home (`internet` column) and those who don't, in relation to mothers' education (`Medu` column) and students' final grades (`G3` column).

Remember, these exercises are for your benefit. If a particular task feels too challenging, refer back to the original code, and try to understand the underlying processes and methods. The more you practice, the more comfortable you'll become with these tools and techniques.
