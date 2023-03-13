#import modules
import os
import glob
import pandas as pd

def main():
  #list all csv files only
  csv_files = glob.glob('*.{}'.format('csv'))
  #append all files together
  df_concat = pd.concat([pd.read_csv(f) for f in csv_files ], ignore_index=True)
  #print(df_concat.head())
  #print(df_concat.info())
  categories_df = df_concat.sort_values(by="Topic")
  #print(categories_df.head())
  categories_df.to_csv("sorted-questions.csv", index=False)

if __name__ == '__main__':
    main()