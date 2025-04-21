# Step 1: Import libraries
import pandas as pd

# Step 2: Load dataset
# Note: This dataset uses tab ("\t") as the separator
df = pd.read_csv('marketing_campaign.csv', sep='\t')

# Step 3: Initial exploration
print("Initial Data Overview:")
print(df.head())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nData Types and Info:")
print(df.info())

# Step 4: Handle missing values
df = df.dropna()  # You can also use fillna() if preferred

# Step 5: Remove duplicates
df = df.drop_duplicates()

# Step 6: Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 7: Standardize text values
df['education'] = df['education'].str.strip().str.lower()
df['marital_status'] = df['marital_status'].str.strip().str.lower()

# Step 8: Convert date column to datetime format
df['dt_customer'] = pd.to_datetime(df['dt_customer'], dayfirst=True)

# Step 9: Fix data types
df['income'] = df['income'].astype(float)
df['age'] = 2025 - df['year_birth']  # Calculate age

# Final Overview
print("\nCleaned Data Overview:")
print(df.info())
print("\nDescriptive Statistics:")
print(df.describe())

# Optional: Save cleaned data to a new CSV file
df.to_csv('cleaned_customer_data.csv', index=False)
