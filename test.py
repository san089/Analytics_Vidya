import os
import sys
import pandas as pd
import re

#Get the presently working directory (which is the parent path and the root of the Project)
parent_path = os.getcwd()

test_file = os.path.join( parent_path , 'data' , 'test.csv')
train_file = os.path.join( parent_path , 'data' , 'train.csv')

def Run_sentiment_analysis():
    tweet_df = pd.read_csv(train_file)
    print(
        "Some stats on data: \nTotal number of records in the dataset: {0}\nTotal number of columns in dataset: {1}".format(
            tweet_df.shape[0], tweet_df.shape[1]))
    columns = tweet_df.columns.values
    print("Columns are : {}".format(' , '.join(columns)))
    tweet_df['clean_tweet'] = tweet_df['tweet'].map(clean_data)
    print(tweet_df)

def clean_data(a):
    #a = re.sub(pattern='#(\w+)' , repl='' ,string=a)
    a = re.sub(pattern='@(\w+)' , repl='' ,string= a )
    a = re.sub(pattern='(http(|s):[a-zA-Z.-//0-9]+)|(#(\w+))' , repl='' , string=a)
    a = re.sub(pattern='[^0-9a-zA-Z.\' \$]' , repl='' , string=a)
    return a

if __name__ == "__main__":
    Run_sentiment_analysis()