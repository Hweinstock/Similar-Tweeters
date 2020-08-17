import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.utils import shuffle
from diagnostics import generate_diagnostics
from features import get_features, get_label
import pickle


def run_model(args, csv_file):

    dataset = pd.read_csv(csv_file)
    # Remove Dead Data i.e NaN
    dataset = dataset.fillna(method='ffill')
    # Doesn't appear to have effect, might be built in.
    dataset = shuffle(dataset)

    # Give set of variables to make prediction
    X = dataset[get_features()]

    # Give Label to predict
    y = dataset[get_label()].values

    # Create and train model
    print("Creating model...")
    if args.load_from_save:
        with open('saved_model.pkl', 'rb') as model:
            regressor = pickle.load(model)
            X_test = X
            y_test = y
    else:
        regressor = LogisticRegression()

        # Split Data into train and test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

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

    if args.save_model:
        with open('saved_model.pkl', 'wb') as out:
            pickle.dump(regressor, out)

