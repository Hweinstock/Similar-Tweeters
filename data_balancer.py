from imblearn.over_sampling import SMOTE
import pandas as pd

# for reproducibility
seed = 100

# SMOTE number of neighbors
k = 1

df = pd.read_csv('comps.csv')[["top_n_word_comparison",
                               "average_word_length_comparison",
                               "top_n_sentence_lengths_comparison",
                               "punctuation_comparison",
                               'same_author']]

# Remove Dead Data i.e NaN
df = df.fillna(method='ffill')


X = df.loc[:, df.columns != 'same_author']
y = df.same_author

oversampler = SMOTE(sampling_strategy='auto',
                    k_neighbors=k,
                    random_state=seed)

X_res, y_res = oversampler.fit_resample(X, y)
df = pd.concat([pd.DataFrame(X_res), pd.DataFrame(y_res)], axis=1)
df.to_csv('balanced_comps.csv', index=False, encoding='utf-8')


