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


COLUMNS = 6
HEADER = "Topic,Question,Answer,Distractor1,Distractor2,Distractor3"


#openai.api_key = <INSERT OPEN_API_KEY STRING HERE> # Not needed anymore?


def print_error(line, comment):
    print("ERROR:", line)
    print("      ", "^" * len(line))
    print(comment + "\n")


def verify(output):
    try:
        # Try to read output into a CSV -- this *should* verify the output's validity
        # as a CSV
        return pd.read_csv(StringIO(output))
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
            error_detected = False
            if i == 0 and "".join(line.split()) != HEADER:
                print_error(line, "Header may be incorrect.")
                error_detected = True

            if line.count(",") != COLUMNS - 1:
                print_error(line, "Extra commas found -- unescaped commas in output or missing newline.")
                error_detected = True

            if not error_detected:
                # TODO: consider adding previous and next line as context?
                print_error(line, "Unknown error in line -- please review.")

        print("-" * 80)
        return None


def main():
    output = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          #{"role": "system", "content": "You are a helpful assistant that <generates X>."},
          {"role": "user", "content": \
                    "Please provide ten multiple choice science questions, in CSV format \
                        with newlines at the end of each row, formatted into columns \
                            Topic,Question,Answer,Distractor1,Distractor2,Distractor3"}
      ]
    )

    text_output = output['choices'][0]['message']['content']
    total_token_cost = output['usage']['total_tokens']

    print(f'Text output:\n{text_output}')
    print(f'Total response token cost: {total_token_cost}')

    print(text_output)

    df = verify(text_output)
    file_id = uuid.uuid4()

    if df:
        # TODO: better directory management; this should be ran in "data" directory
        filename = f"{file_id}.csv"
        print(f"Saving to {filename}")
        df.to_csv(filename)
    else:
        # Save file for review
        filename = f"REVIEW-{file_id}.csv"
        print(f"Saving file for review in {filename}.")

        with open(filename, "w", encoding="utf-8") as file:
            file.write(text_output)


if __name__ == '__main__':
    main()
