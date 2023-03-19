import pandas as pd

# Read data from file
data = pd.read_csv('house-prices.csv')

# Extract columns with missing values
def extract_missing(data):
    missing_cols = []
    for col in data.columns:
        missing = False
        for value in data[col]:
            if pd.isna(value):
                missing = True
                break
        if missing:
            missing_cols.append(col)
    
    return missing_cols


# Count the number of lines with missing data
def count_missing(data):
    missing_row = []
    for index, row in data.iterrows():
        missing = False
        for value in row:
            if pd.isna(value):
                missing = True
                break
        if missing:
            missing_row.append(index)
    print(len(missing_row))
    return missing_row

# Fill in the missing value using mean, median and mode
def mean(data, col):
    col_sum = 0
    count = 0
    for value in data[col]:
        if not pd.isna(value):
            col_sum += value
            count += 1
    return col_sum / count if count > 0 else None


data.fillna(data.mean(), inplace=True)  # replace missing values with mean
data.fillna(data.median(), inplace=True)  # replace missing values with median
data.fillna(data.mode().iloc[0], inplace=True)  # replace missing values with mode

# # Deleting rows containing more than a particular number of missing values
# data.dropna(thresh=len(data.columns)*0.5, axis=0, inplace=True)

# # Deleting columns containing more than a particular number of missing values
# data.dropna(thresh=len(data.index)*0.5, axis=1, inplace=True)

# # Delete duplicate samples
# data.drop_duplicates(inplace=True)


extract_missing(data)
count_missing(data)