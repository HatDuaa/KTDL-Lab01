import argparse
import pandas as pd
import data_cleaning_functions as dcf 

def main(args):
    data = pd.read_csv(args.input)
    message = 'Invalid operation'

    if args.operation == 'list-missing':
        missing_cols = dcf.extract_missing(data)
        message = ''
        print('Columns with missing vals: ', missing_cols)

    elif args.operation == 'count-missing':
        missing_row = dcf.count_missing(data)
        message = ''
        print('The number of lines with missing data: ', len(missing_row))

    elif args.operation == 'fill-missing':
        message, filled_data = dcf.fill_missing(data, args.columns, args.method)
        dcf.write_csv(filled_data, 'result.csv')

    elif args.operation == 'deleting-rows':
        deleting_data = dcf.delete_rows(data, args.threshold)
        dcf.write_csv(deleting_data, 'result.csv')
        message = 'Rows deleted successfully!'
        
    elif args.operation == 'deleting-columns':
        deleting_data = dcf.delete_columns(data, args.threshold)
        dcf.write_csv(deleting_data, 'result.csv')
        message = 'Columns deleted successfully!'
        
    elif args.operation == 'deleting-duplicates':
        deleting_data = dcf.delete_duplicates(data)
        dcf.write_csv(deleting_data, 'result.csv')
        message = 'Duplicate rows deleted successfully!'
        
    elif args.operation == 'normalize':
        normalized_data = dcf.normalize_attribute(data, args.type)
        dcf.write_csv(normalized_data, 'result.csv')
        message = 'Data normalized successfully!'
    
    elif args.operation == 'calculate':
        message, calculate_data = dcf.normalize_attribute(data, args.type)
        dcf.write_csv(calculate_data, 'result.csv')
    
    print(message)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform basic data cleaning operations.")
    parser.add_argument("operation", help="list-missing, count-missing, fill-missing, deleting-rows, deleting-columns, deleting-duplicates, normalize")
    
    # input and output files
    parser.add_argument("--input", "-i", required=True, help="path to the input file")
    parser.add_argument("--out", "-o", required=True, help="path to the output file")
    
    # options for fill-missing operation
    parser.add_argument("--columns", "-c", help="columns to fill missing values")
    parser.add_argument("--method", "-m", help="method for filling missing values", choices=["mean", "median", "mode"])
    
    # options for delete-rows and delete-columns operations
    parser.add_argument("--threshold", "-t", type=float, default=0.5, help="threshold for deleting rows/columns")
    
    # options for normalize operation
    parser.add_argument("--type", "-n", help="type of normalization", choices=["min-max", "z-score"])

    # options for performing math
    parser.add_argument("--calculation", "-cal", help="calculate between 2 column", choices=["add", "sub", "multi", "div"])
    parser.add_argument("--col1", "-c1", help="columns to calculate")
    parser.add_argument("--col2", "-c2", help="columns to calculate")
    
    args = parser.parse_args()
    main(args)
