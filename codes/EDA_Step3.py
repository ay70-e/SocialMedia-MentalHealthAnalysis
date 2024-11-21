#Create by Aya Laheb
# Date 20/11/2024

# This Python script performs an exploratory data analysis (EDA) on a dataset related to social media usage and mental health. 
# It incorporates libraries like pandas, seaborn, and matplotlib for data manipulation, visualization, and statistical analysis.

# The script performs the following key steps:
# 1. Imports necessary libraries
# 2. Loads the data from a CSV file (replace the path with your actual location)
# 3. Checks for missing values and data types
# 4. Provides a basic statistical summary of the data
# 5. Visualizes the distribution of age using a histogram
# 6. Visualizes the distribution of gender and relationship status using bar charts
# 7. Calculates and visualizes the correlation matrix between numerical variables
# 8. Visualizes the relationship between social media usage time and anxiety levels using a scatter plot
# 9. Visualizes the relationship between distractibility and depression using a box plot
# 10. Visualizes the frequency of purposeless social media use using a histogram
# 11. Visualizes the frequency of self-comparison on social media using a bar chart



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('G:\python\SocialMedia-MentalHealthAnalysis\dataanalaysis.csv')  

# Check for missing values and data types
print("Missing values in each column:")
print(data.isnull().sum())
print("\nData Types:")
print(data.dtypes)

# Basic statistical overview
print("\nStatistical summary:")
print(data.describe())

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