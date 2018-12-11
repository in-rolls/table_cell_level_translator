## Append English Translations

The script uses the [Google Translate API](https://cloud.google.com/translate/docs/translating-text) to append English translations of non-English language text in a dataset.

The script takes the following inputs:

1. Path to input CSV
2. Google API token
3. Column names with non-English text
4. Language

The script by default outputs a CSV with the appended columns to input-csv-name-goog-translate.csv The translated CSV has additional columns with column names of translations as: input-column-name-english 

### Functionality

For each column in the CSV with non-English text: 
creates a new vector with all the unique non-english text values in the column, runs each unique value through google translate, and writes results to a column called input-column-name-english and then joins it back to the original dataset.

