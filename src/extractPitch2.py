import os
import pandas as pd

# Path to the folder containing CSV files
folder_path = 'src/data/output'

result_df = pd.DataFrame()


# Loop through each CSV file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        # Assuming your CSV files are comma-separated; if not, adjust the delimiter
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path, usecols=['F0_sma'])
        df.rename(columns={'F0_sma': filename}, inplace=True)
        # Extract filename and the desired column value
        result_df = pd.concat([result_df, df], axis=1)

        # Append the information to the result DataFrame
result_df.to_csv('src/data/result.csv', index=False)
