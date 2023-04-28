import os

from datasets import load_dataset

import pandas as pd


SAMPLE_COUNT = 120
RANDOM_STATE = 2731
NUMBER_SHUFFLES = 4


SYNTHETIC_PATH = 'https://raw.githubusercontent.com/alidiusk/cs2731-final-project/main/data/synth_cleaned.csv?token=GHSAT0AAAAAAB6T4654GM2APAJNT77F5VCEZA6AJPA'
SHUFFLE_DIR = './shuffles'


# Get Sciq dataset
def get_sciq() -> pd.DataFrame:
    sciq_df = load_dataset("sciq")
    # Return whole dataset instead of one of train/validation/test
    return pd.concat(map(pd.DataFrame, 
                         map(lambda s: sciq_df[s], 
                             ['train', 'validation', 'test'])))


# Get synthetic dataset
def get_synth() -> pd.DataFrame:
    return pd.read_csv(SYNTHETIC_PATH)


def main():
    sciq_df = get_sciq()
    synth_df = get_synth()

    # Randomly sample datasets
    rand_sciq_df = sciq_df.sample(n=SAMPLE_COUNT, replace=False, random_state=RANDOM_STATE)
    rand_synth_df = synth_df.sample(n=SAMPLE_COUNT, replace=False, random_state=RANDOM_STATE)

    # Change Sciq column names to match those of Synth (for convenience and consistency)
    rand_sciq_df = rand_sciq_df.rename(columns={'question' : 'Question',
                                                'distractor3' : 'Distractor3',
                                                'distractor2' : 'Distractor2',
                                                'distractor1' : 'Distractor1',
                                                'correct_answer' : 'Answer'})
    rand_sciq_df = rand_sciq_df.loc[:, ['Question', 'Answer', 'Distractor1', 'Distractor2', 'Distractor3']]

    # Make shuffle dir
    if not os.path.isdir(SHUFFLE_DIR):
        os.mkdir(SHUFFLE_DIR)

    # Export four Sciq random shuffles
    for i in range(NUMBER_SHUFFLES):
        filename = f'{SHUFFLE_DIR}/sciq{i:02d}.csv'
        rand_sciq_df.sample(frac=1, random_state=RANDOM_STATE + i).to_csv(filename, index_label="Index")

    # Export four Synth random shuffles
    for i in range(NUMBER_SHUFFLES):
        filename = f'{SHUFFLE_DIR}/synth{i:02d}.csv'
        rand_synth_df.sample(frac=1, random_state=RANDOM_STATE + i).to_csv(filename, index_label="Index")

    # Old code that handled mixing the two datasets to reduce potential evaluator bias
    # 
    # This was decided against due to the Sciq dataset not having a Topic column and our
    # choosing to retain the Topic/Question relevance criterion

    # Generate UUIDs and add UUID column
    # uuids = [uuid.uuid4() for _ in range(2 * SAMPLE_COUNT)]
    # rand_sciq_df['uuid'] = uuids[:SAMPLE_COUNT]
    # rand_synth_df['uuid'] = uuids[SAMPLE_COUNT:]

    # Export UUID sets for reconstruction later
    # sciq_uuids = set(uuids[:SAMPLE_COUNT])
    # synth_uuids = set(uuids[SAMPLE_COUNT:])
    # with open('sciq_uuids.pkl', 'wb') as f:
    #     dump(sciq_uuids, f)
    # with open('synth_uuids.pkl', 'wb') as f:
    #     dump(synth_uuids, f)

    # Combine dataframes
    # TODO -- different column names
    # rand_sciq_df.columns = rand_synth_df.columns
    # rand_df = pd.concat([rand_sciq_df, rand_synth_df], ignore_index=True)
    # print(rand_df)
    # rand_df = pd.concat([rand_sciq_df, rand_synth_df])

    # # Export four random shuffles
    # # Use same RANDOM_STATE but increment so shuffles are different but reproducible
    # for i in range(NUMBER_SHUFFLES):
    #     filename = f'shuffle{i:02d}.csv'
    #     rand_df.sample(frac=1, random_state=RANDOM_STATE+i).to_csv(filename)


if __name__ == '__main__':
    main()
