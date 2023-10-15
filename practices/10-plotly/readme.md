Based on the provided sample which is centered around the use of Plotly for data visualization and creating Dashboards using the Dash library, here's a markdown exercise for you:

# Practice Exercises for Plotly and Dashboards

## Overview

In this section, you'll delve deeper into the capabilities of Plotly and Dash to generate compelling visualizations and dashboards. Start with a review of the core concepts covered, then move on to the exercises below.

Remember, it's essential to grasp these concepts well, as data visualization is a crucial skill in data analysis and data science.

## Core Concepts

### Plotly Basics

Plotly is an open-source plotting library that provides a rich set of interactive plots and visualizations. It is especially known for its capabilities to produce interactive web-ready visualizations.

Example:
```python
import plotly.express as px
df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="sex")
fig.show()
```

### Creating Dashboards using Dash

Dash is a Python framework for building analytical web applications. It's built on top of Plotly, and it seamlessly integrates with data manipulation libraries such as pandas.

Example:
```python
import dash
from dash import dcc, html
import plotly.express as px

app = dash.Dash(__name__)

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="sex")

app.layout = html.Div(children=[
    html.H1("Dash App"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
```

### Data Cleaning with Pandas

Ensuring that the data is clean and well-structured is a prerequisite for any visualization task. We can use pandas for data manipulation and cleaning.

Example:
```python
import pandas as pd
df = pd.DataFrame({'A': [1,2,3], 'B': [4,5,6]})
df = df.assign(C = df['A'] + df['B'])
```

## Exercises

To solidify your understanding, try out the following exercises:

1. Use Plotly to create a line plot for any time-series dataset. Add titles, axis labels, and legends to make the visualization self-explanatory.
2. Generate a bar plot using Plotly. Ensure that the bars are color-coded based on a categorical variable.
3. With pandas, load a dataset, inspect its first few rows, check for any missing values, and create a new column based on existing columns.
4. Create a basic dashboard using Dash that showcases two plots side by side.
5. Extend the dashboard by adding a dropdown widget that allows the user to select which variable they want to visualize in one of the plots.

Remember to check out the official [Plotly](https://plotly.com/python/) and [Dash](https://dash.plotly.com/) documentation for any doubts or additional functionalities you'd like to explore.
