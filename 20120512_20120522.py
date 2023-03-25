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
def my_mean(data, col):
    col_sum = 0
    count = 0
    for value in data[col]:
        if not pd.isna(value) and type(value) != str:
            col_sum += value
            count += 1
    return col_sum / count if count > 0 else None

def my_mode(data, col):
    counts = {}
    mode_value = None
    max_count = 0
    for value in data[col]:
        if not pd.isna(value) and type(value) == str:
            if value not in counts:
                counts[value] = 1
            else:
                counts[value] += 1
            if counts[value] > max_count:
                mode_value = value
                max_count = counts[value]
    return mode_value

def fill_missing(filled_data, missing_cols):
    # Tạo bản sao của DataFrame để tránh thay đổi dữ liệu gốc
    filled_data = filled_data.copy()
    
    for col in missing_cols:
        # Kiểm tra thuộc tính của cột
        if pd.api.types.is_numeric_dtype(filled_data[col]):
            # Điền mean vào các ô dữ liệu bị thiếu
            col_mean = my_mean(filled_data, col)
            for index, value in filled_data[col].items():
                if pd.isna(value):
                    filled_data.loc[index, col] = col_mean
        else:
            # Điền mode vào các ô dữ liệu bị thiếu
            col_mode = my_mode(filled_data, col)
            for index, value in filled_data[col].items():
                if pd.isna(value):
                    filled_data.loc[index, col] = col_mode
    
    return filled_data


# # Deleting rows containing more than a particular number of missing values
# data.dropna(thresh=len(data.columns)*0.5, axis=0, inplace=True)




missing_cols = extract_missing(data)
count_missing(data)
filled_data = fill_missing(data, missing_cols)




filled_data.to_csv('cleaned_data.csv', index=False)

