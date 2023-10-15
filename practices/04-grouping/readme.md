# Practice Exercises for Summarizing Retail Data

## Overview

In this exercise set, you'll get a chance to practice your skills in grouping and aggregating retail data. First, take a moment to review the core concepts that you've been introduced to. Then, proceed with the exercises provided below.

As always, these exercises are for your own understanding and practice. You're encouraged to attempt all of them for better grasp of the topic.

## Core Concepts

### Loading Data with Different Methods

You've seen two methods of loading data: directly from an Excel file and using Feather for faster loading.

Examples:

```python
sales = pd.read_excel('data/Online Retail.xlsx')
```

and 

```python
sales_f = pd.read_feather('data/Online Retail.fth')
```

### Exploratory Data Analysis (EDA)

EDA involves getting a basic understanding of the dataset, its structure, and any patterns or peculiarities within it.

### Grouping Data using pandas

Using `groupby()` in pandas, you can group data based on certain criteria.

Example:

```python
sales.groupby('Country').sum()
```

### Plotting Data

You can visualize aggregated data using different types of plots to derive insights.

Example:

```python
sales.groupby('Country').sum().plot.bar()
```

### Aggregating Data

Aggregating data helps summarize it. Common aggregation functions include `sum()`, `mean()`, `count()`, among others.

## Exercises

 
1. **Country Analysis**:
   - Find the top 5 countries by sales volume.
   - Visualize the sales of these top 5 countries in a pie chart.

2. **Monthly Sales Trend**: 
   - Aggregate the sales data on a monthly basis.
   - Visualize the monthly sales trend from the data's start to end.

3. **Handling Outliers**: 
   - Identify and visualize any outliers in the `UnitPrice` column using a box plot.

4. **Sales by StockCode**: 
   - Determine the top 10 `StockCode` values with the highest sales.
   - Create a bar chart to visualize this data.

5. **Advanced Grouping**:
   - Group the sales data first by `Country` and then by `InvoiceDate` on a monthly frequency.
   - Identify which country has the most consistent monthly sales. (Hint: Consider using standard deviation as a metric)

6. **Data Cleaning**:
   - You noticed negative values in the `Quantity` column during the EDA. Investigate these entries. Are they returns or mistakes in the data?
   - Suggest a method to handle these entries.

7. **Using Helpers**: Use the provided `limit_n` function to group countries outside the top 10 by sales volume into an 'Other' category. Visualize the sales distribution of the modified country list.

Remember to always inspect the data after performing operations to ensure your code has the desired effect.
