# Practice Exercises for Text Data Processing with Movie Reviews

## Overview

In this section, you'll get hands-on experience working with text data, specifically focusing on movie reviews. You'll learn the nuances of text cleaning, pre-processing, and even some introductory aspects of text classification. Whether you're aspiring to build a sentiment analysis model or just curious about the world of NLP, these exercises are a great starting point.

Remember, it's essential to apply what you've learned to ensure a deeper understanding. So, even if some tasks may seem basic, they're building the foundation for more advanced skills.

## Core Concepts

### Text Cleaning and Pre-processing

Working with raw text data can be messy. Before any analysis or modeling, it's crucial to clean and pre-process the data. Common steps include:
- Removing punctuation
- Lowercasing all the text
- Removing HTML tags, like `<br />`
- Handling contractions (e.g., "don't" to "do not")
- Removing stop words (common words that don't carry significant meaning in analysis)

### Text Vectorization

In order to perform machine learning on text, we need to transform our text data into a numerical format. One common method is TF-IDF (Term Frequency-Inverse Document Frequency), which reflects how important a word is to a document in a collection.

### Text Classification

With our processed text, we can build models to classify it into various categories, like sentiment (positive or negative). One of the models used in the provided code is XGBoost, a gradient boosting algorithm.

### Principal Component Analysis (PCA)

PCA is a dimensionality reduction technique. For high-dimensional text data, PCA can help visualize the data in a lower-dimensional space, often just 2D or 3D.

## Exercises

1. **Text Cleaning**: Write a function to clean the review text:
    - Convert all text to lowercase.
    - Remove punctuation from the text.
    - Replace all occurrences of `<br />` with a space.
  
2. **Stop Words**: Instead of using SpaCy, try using the `stopwords` list from the NLTK library to remove stop words from the reviews. Compare the results.

3. **Text Vectorization**: Using the `CountVectorizer` from Scikit-learn, vectorize the text data and observe the most common words. Compare this with the TF-IDF vectorization.

4. **Build Another Model**: Try building a Logistic Regression model using the Scikit-learn library on the TF-IDF vectorized data. Compare its performance with the XGBoost model.

5. **PCA Visualization**: Using the PCA results:
    - Visualize the distribution of positive and negative sentiments on the first two principal components.
    - Identify the words that have the highest weight in the first two principal components.

6. **New Review Prediction**: Add more sample reviews to the "Predict a New Review" section and interpret the results. Try reviews with sarcasm or mixed sentiments to check the robustness of the model.

Remember, these exercises are meant to reinforce the concepts you've encountered and observed in the given code. Don't hesitate to refer back to the code for inspiration or guidance.
