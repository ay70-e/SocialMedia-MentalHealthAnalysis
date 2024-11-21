#Create by Aya Laheb
# Date 20/11/2024

# This script concludes the data exploration and visualization steps. 
# It provides insights into potential relationships between social media usage and mental health based on the data.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('G:\python\SocialMedia-MentalHealthAnalysis\dataanalaysis.csv')  # Ensure the file path is correct

# ====== Data Cleaning ======

# 1. Check for missing values and handle them
print("Missing values in each column before cleaning:")
print(data.isnull().sum())

# Drop columns with a high percentage of missing values if any (adjust threshold as needed)
threshold = 0.5  # Drop columns with more than 50% missing values
data = data[data.columns[data.isnull().mean() < threshold]]

# Fill remaining missing values: For numerical columns, use mean; for categorical, use mode
for column in data.columns:
    if data[column].dtype == 'object':
        data[column].fillna(data[column].mode()[0], inplace=True)  # Fill categorical with mode
    else:
        data[column].fillna(data[column].mean(), inplace=True)  # Fill numerical with mean

# Verify there are no missing values after cleaning
print("\nMissing values in each column after cleaning:")
print(data.isnull().sum())

# 2. Handle inconsistent capitalization or values in categorical columns (if any)
data['Gender'] = data['Gender'].str.capitalize()  # Standardize gender capitalization, e.g., "male" -> "Male"
data['Relationship Status'] = data['Relationship Status'].str.capitalize()  # Example standardization

# 3. Check for duplicates and remove them if found
print("\nNumber of duplicate rows:", data.duplicated().sum())
data = data.drop_duplicates()

# ====== EDA with Visualization ======

# Set seaborn style
sns.set(style="whitegrid")

# 1. Age Distribution
plt.figure(figsize=(8, 5))
sns.histplot(data['What is your age?'], bins=10, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# 2. Gender Distribution
plt.figure(figsize=(12, 5))
sns.countplot(x='Gender', data=data)
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# 3. Relationship Status Distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='Relationship Status', data=data)
plt.title("Relationship Status Distribution")
plt.xlabel("Relationship Status")
plt.ylabel("Count")
plt.show()

# 4. Correlation Heatmap
numeric_data = data.select_dtypes(include='number')
correlation_matrix = numeric_data.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# 5. Social Media Time vs Anxiety Levels
plt.figure(figsize=(12, 5))
sns.scatterplot(x='What is the average time you spend on social media every day?',
                y='On a scale of 1 to 5, how much are you bothered by worries?', data=data)
plt.title("Social Media Time vs Anxiety Levels")
plt.xlabel("Average Time on Social Media")
plt.ylabel("Anxiety Level")
plt.show()

# 6. Distractibility vs Depression
plt.figure(figsize=(8, 5))
sns.boxplot(x='On a scale of 1 to 5, how easily distracted are you?',
            y='How often do you feel depressed or down?', data=data)
plt.title("Distractibility vs Depression")
plt.xlabel("Distractibility Level")
plt.ylabel("Depression Frequency")
plt.show()

# 7. Frequency of Purposeless Social Media Use
plt.figure(figsize=(8, 5))
sns.histplot(data['How often do you find yourself using Social media without a specific purpose?'], bins=5, kde=True)
plt.title("Frequency of Purposeless Social Media Use")
plt.xlabel("Frequency")
plt.ylabel("Count")
plt.show()

# 8. Self-Comparison Frequency on Social Media
plt.figure(figsize=(8, 5))
sns.countplot(x='On a scale of 1-5, how often do you compare yourself to other successful people through the use of social media?', data=data)
plt.title("Self-Comparison Frequency on Social Media")
plt.xlabel("Self-Comparison Level")
plt.ylabel("Count")
plt.show()
