## Translate Unique Non-English Values in a Table and Append Their Translations

The script uses [GoogleTrans](https://github.com/BoseCorp/py-googletrans), a *free and unlimited* python library to append English translations of non-English language text in a dataset.

For each column in the CSV with non-English text: the script creates a new vector with all the unique non-english text values in the column, runs each unique value through Google translate, and writes results to a column called input-column-name-english and then joins it back to the original dataset.

The [script](google_translator.py) takes the following inputs:

1. `INPUT_DIR`: set the dir path of input csv files.
2. `OUTPUT_DIR`: set the dir path for output.
3. `COLUMN_LIST`: set column name list that need to translate, e.g. 
    `['fath', 'name']`
4. `INPUT_LANGUAGE`: set source language, e.g. 'hindi'

The script by default outputs a CSV with the appended columns to input-csv-name-goog-translate.csv The translated CSV has additional columns with column names of translations as: input-column-name-english 

See [sample input](csvs/sample.csv) and [output](csvs/sample-goog-translate.csv).

### Running the Script

```
$ git clone https://github.com/BoseCorp/py-googletrans.git
$ cd ./py-googletrans
$ python setup.py install
$ cd ..
$ python google_translator.py
```
