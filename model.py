import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
import numpy as np

dataset = pd.read_csv('comps.csv')
#print(dataset.head())

#Remove Dead Data i.e NaN
dataset = dataset.fillna(method='ffill')

# Give set of variables to make prediction

X = dataset[["top_n_word_comparison",
                   "average_word_length_comparison",
                   "top_n_sentence_lengths_comparison",
                   "punctuation_comparison"]]

# Give Labl to predict
y = dataset[["same_author?"]].values

# Split Data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create and train model
regressor = LogisticRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

coeff_df = pd.DataFrame(regressor.coef_[0], X.columns, columns=['Coefficient'])
print(coeff_df)

actual_results = [arr.item() for arr in y_test]
predicted_results = y_pred
#print(actual_results)

total = 0
correct = 0

for actual, predicted in zip(actual_results, predicted_results):
    if actual == True:
        total += 1
        if predicted == True:
            correct += 1
print("% of same authors identified:", correct/total * 100)
for actual, predicted in zip(actual_results, predicted_results):
    if actual == False:
        total += 1
        if predicted == False:
            correct += 1

print("% of different authors identified:", correct/total * 100)

for actual, predicted in zip(actual_results, predicted_results):
    if predicted == True:
        total += 1
        if actual == True:
            correct += 1

print("% correct when guessing same authors:", correct/total * 100)