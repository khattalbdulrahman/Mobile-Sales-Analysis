
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the mobile sales data
data = pd.read_csv("Mobile Sales.csv")

# Display the first few rows of the dataset
print(data.head())

# Data Cleaning: Handle missing values
data = data.dropna()  # Drop rows with any missing values
print(data.info())

# Calculate the discount percentage if not provided
data['discount percentage'] = ((data['Original Price'] - data['Selling Price']) / data['Original Price']) * 100

# Analysis 1: Average rating by brand
avg_rating_by_brand = data.groupby('Brands')['Rating'].mean()
print("Average Rating by Brand:")
print(avg_rating_by_brand)

# Analysis 2: Price distribution of mobiles
plt.figure(figsize=(10, 6))
sns.histplot(data['Selling Price'], bins=20, kde=True)
plt.title("Selling Price Distribution")
plt.xlabel("Selling Price")
plt.ylabel("Frequency")
plt.show()

# Analysis 3: Discount percentage across brands
plt.figure(figsize=(10, 6))
sns.barplot(x='Brands', y='discount percentage', data=data)
plt.xticks(rotation=90)
plt.title("Discount Percentage by Brand")
plt.xlabel("Brand")
plt.ylabel("Discount Percentage")
plt.show()

# Conclusion:
# - This dataset shows average ratings, price distribution, and discounts across different mobile brands.
# - Visualizations provide insights into brand ratings, price trends, and discount patterns.

# Save data summary
summary = data.describe()
print("Data Summary:")
print(summary)
