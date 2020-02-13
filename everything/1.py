import pandas as pd

tweets_df = pd.read_csv('../tweets.csv')

result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])

for tweet in list(result):
    print(tweet)
