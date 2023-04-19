"""
Takes Sciq and Synth evaluations exported from Google Sheets and adjusts column names and row
values for later use.

Preprocesses all CSVs in `IN_DIR` and writes new dataframes out to CSVs in `OUT_DIR`. File names
should contain 'sciq' or 'synth' in their name.
"""


import os
import pandas as pd


IN_DIR="./raw_data"
OUT_DIR="./data"


def is_synth(filename: str) -> bool:
    return "synth" in filename


def main():
    if not os.path.isdir(OUT_DIR):
        os.mkdir(OUT_DIR)

    for filename in os.listdir(IN_DIR):
        infilename = f"{IN_DIR}/{filename}"
        outfilename = f"{OUT_DIR}/{filename}"
        if is_synth(infilename):
            df = pd.read_csv(infilename)
            df = df.rename(columns={'The topic and question are related' : 'Topic Relevance',
                                    'The marked answer is correct' : 'Correctness',
                                    'The question is difficult' : 'Difficulty',
                                    'The meaning of the question is clear' : 'Clarity',
                                    'The distractor answers are relavant to the question' : 'Distractor Relevance'})
            df = df.loc[:, ['Index', 'Topic', 'Question', 'Answer', 
                            'Distractor1', 'Distractor2', 'Distractor3',
                            'Topic Relevance', 'Correctness', 'Difficulty', 'Clarity', 'Distractor Relevance']]
            df[['Topic Relevance', 'Correctness', 'Difficulty', 'Clarity', 'Distractor Relevance']] = \
                df[['Topic Relevance', 'Correctness', 'Difficulty', 'Clarity', 'Distractor Relevance']].apply(lambda s: int(s[0][0]))
            df.to_csv(outfilename, index=False)
        else:
            df = pd.read_csv(infilename)
            df = df.rename(columns={'The topic and question are related' : 'Topic Relevance',
                                    'The marked answer is correct' : 'Correctness',
                                    'The question is difficult' : 'Difficulty',
                                    'The meaning of the question is clear' : 'Clarity',
                                    'The distractor answers are relavant to the question' : 'Distractor Relevance'})
            # Remove Topic, Topic Relevance
            df = df.loc[:, ['Index', 'Question', 'Answer', 
                            'Distractor1', 'Distractor2', 'Distractor3',
                            'Correctness', 'Difficulty', 'Clarity', 'Distractor Relevance']]
            df[['Correctness', 'Difficulty', 'Clarity', 'Distractor Relevance']] = \
                df[['Correctness', 'Difficulty', 'Clarity', 'Distractor Relevance']].apply(lambda s: int(s[0][0]))
            df.to_csv(outfilename, index=False)


if __name__ == '__main__':
    main()
