import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.utils import shuffle
from text_model.analyzer.model.diagnostics import generate_diagnostics
from text_model.config_files.config import get_features, get_label
import pickle
from text_model.config_files.config import return_configs

CONFIGS = return_configs()
PATH = '../text_model/analyzer/model/'


def load_model():
    with open(PATH + 'trained_model.pkl', 'rb') as model:
        regressor = pickle.load(model)
    return regressor


def run_on_object(CompObj):
    report = CompObj.__dict__()

    # Convert to pandas dataframe
    data = pd.DataFrame([report])

    features = data[get_features()]

    model = load_model()
    output = model.predict(features)[0]

    return output


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
        generate_diagnostics(actual_results, predicted_results)

        print("\nCoefficients: ")
        print(coeff_df)

    if args.save_model:
        print("Saving Model...")
        with open('saved_model2.pkl', 'wb') as out:
            pickle.dump(regressor, out)


if __name__ == '__main__':
    run_model(None, 'comps.csv')