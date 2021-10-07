from imblearn.over_sampling import SMOTE
import pandas as pd
from ...config_files.config import get_label, get_headers, get_features


def balance_data(df):
    # for reproducibility
    seed = 100

    # SMOTE number of neighbors
    k = 1

    df = df[get_headers()]

    # Remove Dead Data i.e NaN
    df = df.fillna(method='ffill')


    # Separate what is being used to predict and what is being predicted.

    #X = df.loc[:, df.columns != get_label()[0]]
    # TODO: Fix the Error here. "ValueError: The target 'y' needs to have more than 1 class. Got 1 class instead"
    X = df.loc[:, get_features()]
    y = df.same_author
    over_sampler = SMOTE(sampling_strategy='auto',
                         k_neighbors=k,
                         random_state=seed)

    # over sample the data
    X_res, y_res = over_sampler.fit_resample(X, y)

    # Merge it back into a dataframe
    new_df = pd.concat([pd.DataFrame(X_res), pd.DataFrame(y_res)], axis=1)

    return new_df

