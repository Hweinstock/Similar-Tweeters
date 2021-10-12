import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def simple_plot():
    df = pd.read_csv("comps.csv")

    # sns.set_style("whitegrid")
    # sns.FacetGrid(df, hue="same_author", height=4) \
    #               .map(plt.scatter, 'punctuation_comparison', "top_n_sentence_lengths_comparison") \
    #               .add_legend()
    # plt.show()


    sns.set_style("whitegrid")
    sns.pairplot(df, hue="same_author", height=3)
    plt.legend()
    plt.show()
