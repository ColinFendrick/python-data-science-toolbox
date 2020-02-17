import pandas as pd

# Initialize reader object: df_reader
df_reader = pd.read_csv('../world_ind_pop.csv', chunksize=10)

print(next(df_reader))
print(next(df_reader))
