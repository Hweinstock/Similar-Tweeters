import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.utils import shuffle
from diagnostics import generate_diagnostics

dataset = pd.read_csv('comps.csv')

# Doesn't appear to have effect, might be built in.
dataset = shuffle(dataset)

# Give set of variables to make prediction
X = dataset[["top_n_word_comparison",
                   "average_word_length_comparison",
                   "top_n_sentence_lengths_comparison",
                   "punctuation_comparison"]]

# Give Labl to predict
y = dataset[["same_author"]].values

# Split Data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
# Create and train model
print("Creating model...")
regressor = LogisticRegression()

print("Training model...")
regressor.fit(X_train, y_train)

# Predict on test dataset
print("Predicting with model...")
y_pred = regressor.predict(X_test)

# Create Dataframe of coefficients
coeff_df = pd.DataFrame(regressor.coef_[0], X.columns, columns=['Coefficient'])

# Rename for clarity and reformatting
actual_results = [arr.item() for arr in y_test]
predicted_results = y_pred
print("Generating diagnostics...")
# Print out diagnostics of tests
generate_diagnostics(actual_results, predicted_results)

print("\nCoefficients: ")
print(coeff_df)
