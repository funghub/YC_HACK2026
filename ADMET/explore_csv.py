import pandas as pd
import numpy

csv_file_path = "./ADMET/results/myJobName/pred.csv"

df = pd.read_csv(csv_file_path)

# # Show first 10 rows nicely formatted
# print(df.head(10))

print(df.columns)