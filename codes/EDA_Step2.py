#Create by Aya Laheb
# Date 20/11/2024

# This Python script performs an exploratory data analysis (EDA) on a dataset related to social media usage and mental health. 
# It incorporates libraries like pandas, seaborn, and matplotlib for data manipulation, visualization, and statistical analysis.

# The script performs the following key steps:
# 1. Imports necessary libraries
# 2. Loads the data from a CSV file (replace the path with your actual location)
# 3. Checks and potentially converts data types (e.g., dates)
# 4. Provides a statistical summary of numerical data
# 5. Analyzes the distribution of categorical variables like age, gender, etc.
# 6. Calculates descriptive statistics for social media usage data
# 7. Analyzes the distribution of mental health indicators
# 8. Calculates and displays the correlation matrix between numerical variables
# 9. Visualizes the correlation matrix using a heatmap



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the data
data = pd.read_csv('G:\python\SocialMedia-MentalHealthAnalysis\dataanalaysis.csv')  # Replace with your file path

# Print data types
print(data.dtypes)

# Convert date strings to datetime if applicable
# Replace 'Date' with the actual column name if you have a date column
if 'Date' in data.columns:
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Statistical overview of numerical data
print("Statistical summary of numerical data:")
print(data.describe())

# Age distribution
print("\nAge distribution:")
print(data['What is your age?'].value_counts())

# Gender distribution
print("\nGender distribution:")
print(data['Gender'].value_counts())

# Relationship status distribution
print("\nRelationship status distribution:")
print(data['Relationship Status'].value_counts())

# Occupation status distribution
print("\nOccupation status distribution:")
print(data['Occupation Status'].value_counts())

# Social media time statistics
print("\nStatistics on the average time spent on social media every day:")
print(data['What is the average time you spend on social media every day?'].describe())

# Distractibility levels distribution
print("\nDistractibility levels distribution:")
print(data['On a scale of 1 to 5, how easily distracted are you?'].value_counts())

# Anxiety levels distribution
print("\nAnxiety levels distribution:")
print(data['On a scale of 1 to 5, how much are you bothered by worries?'].value_counts())

# Difficulty concentrating distribution
print("\nDifficulty concentrating distribution:")
print(data['Do you find it difficult to concentrate on things?'].value_counts())

# Self-comparison distribution
print("\nSelf-comparison distribution:")
print(data['On a scale of 1-5, how often do you compare yourself to other successful people through the use of social media?'].value_counts())

# Depression feelings distribution
print("\nDepression feelings distribution:")
print(data['How often do you feel depressed or down?'].value_counts())

# ====== Calculate the correlation matrix ======
print("\nCorrelation matrix between variables:")
numeric_data = data.select_dtypes(include=[np.number])  # Select only numeric columns
correlation_matrix = numeric_data.corr()
print(correlation_matrix)

# ====== Plot the heatmap ======
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()