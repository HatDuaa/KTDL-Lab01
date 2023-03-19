import pandas as pd

# Read data from file
data = pd.read_csv('house-prices.csv')

# Extract columns with missing values
cols_with_missing = data.columns[data.isnull().any()].tolist()
print(cols_with_missing)

# Count the number of lines with missing data
num_rows_with_missing = sum(data.isnull().sum(axis=1) > 0)
print(num_rows_with_missing)

# # Fill in the missing value using mean, median and mode
# data.fillna(data.mean(), inplace=True)  # replace missing values with mean
# data.fillna(data.median(), inplace=True)  # replace missing values with median
# data.fillna(data.mode().iloc[0], inplace=True)  # replace missing values with mode

# # Deleting rows containing more than a particular number of missing values
# data.dropna(thresh=len(data.columns)*0.5, axis=0, inplace=True)

# # Deleting columns containing more than a particular number of missing values
# data.dropna(thresh=len(data.index)*0.5, axis=1, inplace=True)

# # Delete duplicate samples
# data.drop_duplicates(inplace=True)

# # Normalize a numeric attribute using min-max and Z-score methods
# numeric_cols = data.select_dtypes(include=[float, int]).columns.tolist()
# data[numeric_cols] = (data[numeric_cols] - data[numeric_cols].min()) / (data[numeric_cols].max() - data[numeric_cols].min())  # min-max normalization
# data[numeric_cols] = (data[numeric_cols] - data[numeric_cols].mean()) / data[numeric_cols].std()  # Z-score normalization

# # Performing addition, subtraction, multiplication, and division between two numerical attributes
# numeric_cols = data.select_dtypes(include=[float, int]).columns.tolist()
# for i in range(len(numeric_cols)):
#     for j in range(i+1, len(numeric_cols)):
#         col1 = numeric_cols[i]
#         col2 = numeric_cols[j]
#         data[f'{col1} + {col2}'] = data[col1] + data[col2]
#         data[f'{col1} - {col2}'] = data[col1] - data[col2]
#         data[f'{col1} * {col2}'] = data[col1] * data[col2]
#         data[f'{col1} / {col2}'] = data[col1] / data[col2]

# # Save data to file
# data.to_csv('cleaned_data.csv', index=False)
