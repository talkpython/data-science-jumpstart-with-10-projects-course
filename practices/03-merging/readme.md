# Practice Exercises for Merging Data

## Overview

In this section, you'll practice techniques for merging and reshaping data from multiple sources using pandas. Go through the core concepts first, and then work on the exercises.

## Core Concepts

### Merging DataFrames with Pandas

Merging is a crucial operation in data manipulation. The primary function you will use in pandas for merging is `.merge()`. The merge function allows for a variety of join operations similar to those in SQL.

Examples:

```python
left = pd.DataFrame({'key': ['A', 'B'], 'value': [1, 2]})
right = pd.DataFrame({'key': ['A', 'B'], 'value': [3, 4]})
merged = left.merge(right, on='key')
```

### Validating Merges

You can validate merges using the `validate` parameter in the `.merge()` function. This can be set to:
- `'1:1'`: Check if merge keys are unique in both left and right datasets.
- `'1:m'`: Check if merge keys are unique in the left dataset.
- `'m:1'`: Check if merge keys are unique in the right dataset.
- `'m:m'`: No validation.

### Debugging and Data Cleaning

Utilizing functions like `.pipe()` to streamline your operations can also allow you to insert debugging functions to better understand the flow of your data.

Example:

```python
def debug(df):
    print(df.shape)
    return df

df.pipe(debug)
```

### Exporting Data to Excel

Pandas provides functionalities to write to Excel files. This can be achieved using the `.to_excel()` function and the `pd.ExcelWriter` context.

## Exercises

1. Create two small DataFrames with 3 columns each and perform an inner join using the `.merge()` function.
2. Try different types of joins (left, right, outer, inner) on the above DataFrames and observe the results.
3. Take two DataFrames with non-unique keys and try to validate the merge using `'1:1'`. Note down the error and understand why it's happening.
4. Create a debugging function that prints out the shape of the DataFrame and integrate it using the `.pipe()` method in a sequence of operations.


