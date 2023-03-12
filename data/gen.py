# LINKS TO USEFUL SOURCES:
# https://platform.openai.com/docs/guides/chat

# Note: Make sure you’re using openai version > 0.27.0
# If needed, run in the console or command line: pip install --upgrade openai

# TODOS
# - Consider counting current master CSV size -- count lines in each valid CSV
# - Consider taking number of questions to generate as a script parameter


import uuid
from io import StringIO

import openai
import pandas as pd
import sys


COLUMNS = 6
HEADER = "Topic,Question,Answer,Distractor1,Distractor2,Distractor3"
COLUMNS = ["Topic","Question","Answer","Distractor1","Distractor2","Distractor3"]


# Either place the API key here or paste it in a '.openai' file in this directory.
# openai.api_key = <INSERT OPEN_API_KEY STRING HERE>
openai.api_key_path = ".openai"


def print_error(line, comment):
    print("ERROR:", line)
    print(f"      ", "^", comment, "\n")


def verify(output):
    try:
        # Try to read output into a CSV -- this *should* verify the output's validity
        # as a CSV
        #
        
        # Replace pipes with commas and commas with pipes, triggering of the error below
        # is indicitive of an extra pipe operator somewhere in the output. 
        print("\nOUTPUT\n", StringIO(output.strip()).read())
        trans_output = ''.join([',' if char == '|' else '|' if char == ',' else char for char in output.strip()])
        print("\nTRANS_OUTPUT\n", StringIO(trans_output.strip()).read())
        return pd.read_csv(StringIO(trans_output), sep=",", header=None, names=COLUMNS)
    except Exception as err:
        print("-" * 80)
        print(f"Exception encountered:\n{err}")

        # Verify that header is correct
        # Attempt to find an offending line
        #
        # We want to identify a line with extra commas -- this could be indicative of
        # text containing commas, or of a missing newline -- highlight for manual
        # intervention.
        for i, line in enumerate(output.lines()):
            if i == 0 and "".join(line.split()) != HEADER:
                print_error(line, "Header may be incorrect.")

            if line.count(",") != COLUMNS - 1:
                print_error(line, "Extra commas found -- unescaped commas in output or missing newline.")

        print("-" * 80)
        return None

# Specify number of questions to generate as first command line argument
# Ex. $ python3 gen.py fifty
def main():
    output = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          #{"role": "system", "content": "You are a helpful assistant that <generates X>."},
          {"role": "user", "content": \
                    "Provide {} multiple choice science questions, in CSV format \
                      replacing the comma separator \",\" with a pipe \"|\" separator \
                        and with newlines at the end of each row, formatted into columns \
                          Topic|Question|Answer|Distractor1|Distractor|Distractor3".format(sys.argv[1])}
      ]
    )

    text_output = output['choices'][0]['message']['content']
    total_token_cost = output['usage']['total_tokens']

    print(f'Text output:\n{text_output}')
    print(f'Total response token cost: {total_token_cost}')

    df = verify(text_output)
    file_id = uuid.uuid4()

    if df is not None:
        # TODO: better directory management; this should be ran in "data" directory
        filename = f"{file_id}.csv"
        print(f"Saving to {filename}")
        df.to_csv(filename, index=False)
    else:
        # Save file for review
        filename = f"REVIEW-{file_id}.csv"
        print(f"Saving file for review in {filename}.")

        with open(filename, "w", encoding="utf-8") as file:
            file.write(text_output)


if __name__ == '__main__':
    main()
