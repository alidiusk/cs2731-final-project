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
            df = df.rename(columns={'Index' : 'index',
                                    'Topic' : 'topic',
                                    'Question' : 'question',
                                    'Answer' : 'answer',
                                    'Distractor1' : 'distractor1',
                                    'Distractor2' : 'distractor2',
                                    'Distractor3' : 'distractor3',
                                    'The topic and question are related' : 'topic_relevance',
                                    'The marked answer is correct' : 'correctness',
                                    'The question is difficult' : 'difficulty',
                                    'The meaning of the question is clear' : 'clarity',
                                    'The distractor answers are relavant to the question' : 'distractor_relevance'})
            df = df.loc[:, ['index', 'topic', 'question', 'answer', 
                            'distractor1', 'distractor2', 'distractor3',
                            'topic_relevance', 'correctness', 'difficulty', 'clarity', 'distractor_relevance']]
            for column in ['topic_relevance', 'correctness', 'difficulty', 'clarity', 'distractor_relevance']:
                df[column] = df[column].map(lambda s: int(s[0]), na_action = 'ignore')
                # df[column] = df[column].map(lambda s: s[4:], na_action = 'ignore')
            df.to_csv(outfilename, index=False)
        else:
            df = pd.read_csv(infilename)
            df = df.rename(columns={'Index' : 'index',
                                    'Question' : 'question',
                                    'Answer' : 'answer',
                                    'Distractor1' : 'distractor1',
                                    'Distractor2' : 'distractor2',
                                    'Distractor3' : 'distractor3',
                                    'The topic and question are related' : 'topic_relevance',
                                    'The marked answer is correct' : 'correctness',
                                    'The question is difficult' : 'difficulty',
                                    'The meaning of the question is clear' : 'clarity',
                                    'The distractor answers are relavant to the question' : 'distractor_relevance'})
            # Remove Topic, Topic Relevance
            df = df.loc[:, ['index', 'question', 'answer', 
                            'distractor1', 'distractor2', 'distractor3',
                            'correctness', 'difficulty', 'clarity', 'distractor_relevance']]
            for column in ['correctness', 'difficulty', 'clarity', 'distractor_relevance']:
                df[column] = df[column].map(lambda s: int(s[0]), na_action = 'ignore')
                # df[column] = df[column].map(lambda s: s[4:], na_action = 'ignore')
            df.to_csv(outfilename, index=False)


if __name__ == '__main__':
    main()
