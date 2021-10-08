# Arguments

Text Analyzer Files:
```
usage: text_analyzer.py [-h] [-lm LOAD_FROM_SAVE] [-sm] [-sc] [-lc DATASET]
                        [-st] [-lt] [-u] [--text-objects TEXT_OBJECTS]
                        [--text-object-type {discord_message,book}]

optional arguments:
  -h, --help            show this help message and exit
  -lm LOAD_FROM_SAVE, --load-from-save LOAD_FROM_SAVE
                        Whether or not to load model from save or train a
                        fresh one
  -sm, --save-model     Whether or not to save model after running
  -sc, --save_comps     Where or not to save comps dataframe after creating.
  -lc DATASET, --load_comps DATASET
                        Path to CSV file to read in.
  -st, --save_text      Whether or not to store the text objects.
  -lt, --text_objects   Path to pickle to load text objects from.
  -u, --dont-balance-data
                        Whether or not to balance data
  --text-objects TEXT_OBJECTS
                        Path to Pickle file to load in textObjects
  --text-object-type {discord_message,book}
                        Type of text object to create.

```
