
import pandas as pd
import numpy as np

data = pd.DataFrame({
    'A': [1, 2, np.nan, 1],
    'B': [4, np.nan, 6, 4]
})


print(data['A'][1])

import argparse
import pandas as pd

def impute_data(data, method, columns):
    if method == 'mean':
        for col in columns:
            mean = data[col].mean()
            data[col].fillna(mean, inplace=True)
    return data

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='CSV file to impute')
    parser.add_argument('--method', choices=['mean', 'median', 'mode'], default='mean', help='Imputation method')
    parser.add_argument('--columns', nargs='+', help='Columns to impute')
    parser.add_argument('--out', help='Output file')
    args = parser.parse_args()

    # Read CSV file
    data = pd.read_csv(args.filename)

    # Impute missing values
    data = impute_data(data, args.method, args.columns)

    # Save result to CSV file
    if args.out:
        data.to_csv(args.out, index=False)
    else:
        print(data)
