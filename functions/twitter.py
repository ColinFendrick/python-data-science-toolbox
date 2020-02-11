import pandas as pd

tweets_df = pd.read_csv('../tweets.csv')

def count_entries(df, col_name):
    langs_count = {}
    col = df[col_name]

    for entry in col:
        if entry in langs_count.keys():
            langs_count[entry] = langs_count[entry] + 1
        else:
            langs_count[entry] = 1
    return langs_count

result = count_entries(tweets_df, 'lang')
print(result)
