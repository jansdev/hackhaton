import pandas as pd

def parse_excel_data(filename, columns):
    # Load the Excel file into a Pandas DataFrame
    df = pd.read_excel(filename)

    #change second row to be data titles
    headers = df.iloc[0]
    code_as_header_df  = pd.DataFrame(df.values[1:], columns=headers)
    
    # Select the values only from desired stations
    filtered_df = code_as_header_df[columns]

    # Return the DataFrame
    return filtered_df