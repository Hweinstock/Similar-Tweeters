import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.utils import shuffle
from ...analyzer.model.diagnostics import generate_diagnostics
from ...config_files.config import get_features, get_label
import pickle
from ...config_files.config import return_configs

CONFIGS = return_configs()
PATH = 'text_backend/text_analyzer/text_model/analyzer/model/'


def load_model():
    with open(PATH + 'saved_model.pkl', 'rb') as model:
        regressor = pickle.load(model)
    return regressor


def run_on_object(CompObj):
    report = CompObj.__dict__()

    # Convert to pandas dataframe
    data = pd.DataFrame([report])

    features = data[get_features()]

    model = load_model()

    empty_data = features.isnull().values.any()

    # Temporary Fix for inputs without enough text.
    if empty_data:
        print("Error: Not enough data to generate full values, returning 0. (model.py 35)")
        return False, 0.0

    output = model.predict(features)[0]
    similarity_percentage = model.predict_proba(features)[0][1]

    return output, similarity_percentage


def run_model(args, dataset):

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
    if args is not None and args.load_from_save:
        regressor = load_model()
        X_test = X
        y_test = y
    else:
        regressor = LogisticRegression()

        # Split Data into train and test
        if not args.save_model:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=CONFIGS["test_split"], random_state=0)
        else:
            X_train, y_train = X, y
        train_size = len(X_train)
        test_size = len(X_test)
        print("Training model...")
        # Flatten train data
        y_train = y_train.ravel()

        regressor.fit(X_train, y_train)

    if not args.save_model:
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
        generate_diagnostics(actual_results, predicted_results, train_size, test_size)

        print("\nCoefficients: ")
        print(coeff_df)

    if args.save_model:
        print("Saving Model...")
        with open('saved_model2.pkl', 'wb') as out:
            pickle.dump(regressor, out)


if __name__ == '__main__':
    run_model(None, 'comps.csv')