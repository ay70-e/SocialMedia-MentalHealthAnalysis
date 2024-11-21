#Create by Aya Laheb
# Date 12/11/2024


## This Python script performs a basic exploratory data analysis (EDA) 
# on a dataset related to social media usage and its potential impact
#  on mental health. It calculates descriptive statistics for numerical 
# variables, analyzes categorical data distributions, and provides 
# insights into user demographics, social media habits, and self-reported mental health indicators.


import pandas as pd

# Load the data
data = pd.read_csv('G:\python\SocialMedia-MentalHealthAnalysis\dataanalaysis.csv')  

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