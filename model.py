import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.utils import shuffle

import numpy as np

dataset = pd.read_csv('balanced_comps.csv')
#print(dataset.head())

# Remove Dead Data i.e NaN
# dataset = dataset.fillna(method='ffill')

# Give set of variables to make prediction
dataset = shuffle(dataset)

X = dataset[["top_n_word_comparison",
                   "average_word_length_comparison",
                   "top_n_sentence_lengths_comparison",
                   "punctuation_comparison"]]

# Give Labl to predict
y = dataset[["same_author"]].values

# Split Data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create and train model
regressor = LogisticRegression()
regressor.fit(X_train, y_train)

# Predict on test dataset
y_pred = regressor.predict(X_test)

# Create Dataframe of coefficients
coeff_df = pd.DataFrame(regressor.coef_[0], X.columns, columns=['Coefficient'])

# Rename for clarity and reformatting
actual_results = [arr.item() for arr in y_test]
predicted_results = y_pred

total = 0
correct = 0

for actual, predicted in zip(actual_results, predicted_results):
    if actual == True:
        total += 1
        if predicted == True:
            correct += 1
print("% of same authors identified:", correct/total * 100)

total = 0
correct = 0

for actual, predicted in zip(actual_results, predicted_results):
    if actual == False:
        total += 1
        if predicted == False:
            correct += 1

print("% of different authors identified:", correct/total * 100)

total = 0
correct = 0
for actual, predicted in zip(actual_results, predicted_results):
    if predicted == True:
        total += 1
        if actual == True:
            correct += 1

print("% correct when guessing same authors:", correct/total * 100)

total = 0
correct = 0
for actual, predicted in zip(actual_results, predicted_results):
    total += 1
    if actual == predicted:
        correct += 1

print("Overall % Correct:", correct/total * 100)
print(coeff_df)