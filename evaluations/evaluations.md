# Human Evaluation Guidelines

## Evaluation Questions

* 7-point Likert scale
    1) Strongly Disagree
    2) Disagree
    3) Somewhat Disagree, 
    4) Neither Agree nor Disagree
    5) Somewhat Agree
    6) Agree
    7) Strongly Agree
* Likert items
    1) The topic and question are related
    2) The marked answer is correct
    3) The question is difficult
    4) The meaning of the question is clear
    5) The distractor answers are relevant to the question

## Design

* Spreadsheet
    * Each person gets a tab in a shared Google Sheet
    * Random shuffle of mixed Sciq and synthetic questions
        * 240 total = 120 Sciq, 120 synthetic
* Implementation
    * CSV for random selection of synthetic data
    * CSV for random selection of Sciq data
    * Combined CSV...
        * Assign UUIDs to each question and store hash table linking UUID to Sciq/Synthetic status
    * Export shuffles of combined CSVs for each evaluator
    * Conduct evaluations...
    * Reconstruct CSV for each person with human evaluations and Sciq/Synthetic status using UUID
      table
