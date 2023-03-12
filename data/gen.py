# LINKS TO USEFUL SOURCES:
# https://platform.openai.com/docs/guides/chat

# Note: Make sure you’re using openai version > 0.27.0
# If needed, run in the console or command line: pip install --upgrade openai

import os
import openai
import pandas as pd
import uuid
from io import StringIO

#openai.api_key = <INSERT OPEN_API_KEY STRING HERE> # Not needed anymore?                          

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

       
textOutput = output['choices'][0]['message']['content']
totalTokenCost = output['usage']['total_tokens']

print(f'Text output:\n{textOutput}')
print(f'Total response token cost: {totalTokenCost}')

print(textOutput)

# TODO: error handling
df = pd.read_csv(StringIO(textOutput))
# TODO: better directory management; this should be ran in "data" directory
df.to_csv('./{}.csv'.format(uuid.uuid4())) 
