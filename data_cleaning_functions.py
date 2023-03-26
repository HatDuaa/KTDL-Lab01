import pandas as pd
import math
import numpy as np



# Write data to file
def write_csv(dataframe, file_path):
    # Mở file CSV trong chế độ ghi
    with open(file_path, 'w') as file:
        # Lấy các tên cột và ghi vào file
        columns = dataframe.columns.tolist()
        header = ''
        for column in columns:
            header += column + ','
        header = header[:-1] + '\n'
        file.write(header)
        # Lặp qua từng dòng trong DataFrame và ghi vào file
        for i in range(len(dataframe)):
            row_values = []
            for j in range(len(columns)):
                value = dataframe.iloc[i, j]
                # Thay thế giá trị NaN bằng rỗng ('') trước khi ghi vào file
                if is_nan(value):
                    value = ''
                else:
                    value = str(value)
                row_values.append(value)
            row = ''
            for value in row_values:
                row += value + ','
            row = row[:-1] + '\n'
            file.write(row)


# Check NaN
def is_nan(val):
    return val != val

# Check colume is numberic
def is_number(data, col):
    for val in data[col]:
        if not is_nan(val):
            if type(val) == str:
                return False
    
    return True

# Drop column or row
def my_drop(data, col=None, index=None):
    flag = False

    if col is not None:
        # Loại bỏ cột
        if col in data.columns:
            new_data = pd.DataFrame()
            for column in data.columns:
                if column != col:
                    new_data[column] = data[column]
            return new_data
        else:
            return data
    elif index is not None:
        # Loại bỏ hàng
        if index in data.index:
            new_data = pd.DataFrame()
            for i in range(len(data.index)):
                if i != index:
                    new_data.loc[len(new_data)] = data.iloc[i]
            return new_data
        else:
            return data
    else:
        return data


# Min
def my_min(data, col):
    min = data.loc[0, col]
    
    for val in data[col]:
        if not is_nan(val) and type(val) != str:
            if min > val: 
                min = val
    
    return min

# Min
def my_max(data, col):
    max = data.loc[0, col]
    
    for val in data[col]:
        if not is_nan(val) and type(val) != str:
            if max < val: 
                max = val
    
    return max

# standard deviation
def my_std(data, col):
    s = 0
    mean = my_mean(data, col)
    for val in data[col]:
        if not is_nan(val) and type(val) != str:
            s += (val - mean)**2
            
    s /= len(data[col]) - 1
    return math.sqrt(s) if s!=0 else None

# Mean
def my_mean(data, col):
    col_sum = 0
    count = 0
    for val in data[col]:
        if not is_nan(val) and type(val) != str:
            col_sum += val
            count += 1
    return col_sum / count if count > 0 else None

# Median
def my_median(data,col):
    n = len(data[col])
    if n % 2 == 1:
        return data[col][int(n/2)]
    else:
        s = (data[col][n/2 - 1] + data[col][n/2]) / 2
        return s

# mode
def my_mode(data, col):
    counts = {}
    mode_val = None
    max_count = 0
    for val in data[col]:
        if not is_nan(val) and type(val) == str:
            if val not in counts:
                counts[val] = 1
            else:
                counts[val] += 1
            if counts[val] > max_count:
                mode_val = val
                max_count = counts[val]
    return mode_val


# Extract columns with missing vals
def extract_missing(data):
    missing_cols = []
    for col in data.columns:
        missing = False
        for val in data[col]:
            if is_nan(val):
                missing = True
                break
        if missing:
            missing_cols.append(col)
    
    if data.loc[2, 'Alley'] != data.loc[2, 'Alley']:
        print(type(data.loc[2, 'Alley']))
        print(data.loc[2, 'Alley'])
    return missing_cols


# Count the number of lines with missing data
def count_missing(data):
    missing_row = []
    for index, row in data.iterrows():
        missing = False
        for val in row:
            if is_nan(val):
                missing = True
                break
        if missing:
            missing_row.append(index)

    return missing_row

# Fill in the missing val using mean, median and mode
def fill_missing(data, col, method):
    # Message 
    message = 'Missing values filled successfully!'
    # Tạo bản sao của DataFrame để tránh thay đổi dữ liệu gốc
    result_data = data.copy()
    tmp = None

    if method == 'mode':
    # Kiểm tra thuộc tính của cột
        if not is_number(result_data, col):
            # Điền mode vào các ô dữ liệu bị thiếu
            tmp = my_mode(result_data, col)
    elif is_number(result_data, col):
        if method == 'mean': 
            # Điền mean vào các ô dữ liệu bị thiếu
            tmp = my_mean(result_data, col)
        elif method == 'median':
            # Điền median vào các ô dữ liệu bị thiếu
            tmp = my_median(result_data, col)
        else:
            message = 'choose the correct method'
    else:
            message = 'choose the correct method'

    if tmp != None:
        for index, val in result_data[col].items():
            if is_nan(val):
                result_data.loc[index, col] = tmp
        
    return message, result_data


# Deleting rows containing more than a particular number of missing vals
def delete_rows(data, percents):
    delete_data = data.copy()
    
    n = delete_data.shape[1]
    for index, row in delete_data.iterrows():
        count_missing = 0
        for val in row:
            if is_nan(val):
                count_missing += 1 
        if count_missing > n*percents:
            delete_data = my_drop(data, None, index)
    
    return delete_data
    
    

# Deleting columns containing more than a particular number of missing vals
def delete_columns(data, percents):
    delete_data = data.copy()
    
    n = delete_data.shape[0]
    for col in data.columns:
        count_missing = 0
        for val in data[col]:
            if is_nan(val):
                count_missing += 1 
        if count_missing > n*percents:
            delete_data = my_drop(data, col, None)
    
    return delete_data

# Delete duplicate samples
def delete_duplicates(data):
    delete_data = data.copy()

    rows_seen = set() 
    rows_drop = []

    for index, row in delete_data.iterrows(): 
        row_tuple = tuple(row.fillna('nan'))
        if row_tuple in rows_seen:
            rows_drop.append(index)
        else: 
            rows_seen.add(row_tuple)

    for i in range(len(rows_drop)):
        delete_data = my_drop(delete_data, None, rows_drop[i])

    return delete_data

# Normalize a numeric attribute using min-max and Z-score methods.
def normalize_attribute(data, method):
    copied_data = data.copy()
    for col in data.columns:
        min = my_min(copied_data, col)
        max = my_max(copied_data, col)
        mean = my_mean(copied_data, col)
        s = my_std(copied_data, col)
        for i, val in enumerate(copied_data[col]):
            if not is_nan(val) and type(val) != str:
                if method == 'min-max':
                    if max - min != 0:
                        copied_data.loc[i, col] = (val - min)/(max - min)
                if method == 'z-score':
                    if s != None:
                        copied_data.loc[i, col] = (val - mean)/s
    
    return copied_data

# Performing addition, subtraction, multiplication, and division between two numerical attributes.
def performing_math(data, method, col1, col2):
    message = 'Performing calculate successfully!'
    result_data = pd.DataFrame(columns=['result'])

    if not is_number(data, col1) or not is_number(data, col2):
        message = 'Exits one attribute is not numerical'
        return message, result_data
    else:
        for i in range(len(data[col1])):
            val1 = data[col1][i]
            val2 = data[col2][i]

            if is_nan(val1) or is_nan(val2):
                result_data.loc[i] = np.nan
                continue
            
            if method == 'add':
                result_data.loc[i] = val1 + val2

            elif method == 'subtract':
                result_data.loc[i] = val1 - val2

            elif method == 'multiply':
                result_data.loc[i] = val1 * val2

            elif method == 'divide':
                if val2 != 0:
                    result_data.loc[i] = val1 / val2
                else:
                    result_data.loc[i] = np.nan
        
    return message, result_data




# Read data from file
data = pd.read_csv('house-prices.csv')
 

# missing_cols = extract_missing(data)
# print(len(count_missing(data)))
# a ,result_data= fill_missing(data, 'LotFrontage', 'mode')

# delete_rows(data, 0.5)
# delete_columns(data, 0.5)
# result_data=delete_duplicates(data)
# normalize_attribute(data, 'min-max')
# a, result_data = performing_math(data, 'add', 'LotFrontage', 'OverallQual')
# write_csv(result_data, 'result.csv')
#result_data.to_csv('result.csv', index = True)



