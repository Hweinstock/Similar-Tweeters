import argparse


def prepare_args():

    parser = argparse.ArgumentParser()

    parser.add_argument("-l",
                        "--load-from-save",
                        help="Whether or not to load model from save or train a fresh one",
                        action="store",
                        type=str,
                        dest="load_from_save",
                        default=None)

    parser.add_argument("-s",
                        "--save-model",
                        help="Whether or not to save model after running",
                        action="store_true",
                        dest="save_model",
                        default=False)

    parser.add_argument("-d",
                        "--dataset",
                        help="Path to CSV file to read in.",
                        action="store",
                        type=str,
                        default=None,
                        dest="dataset")

    parser.add_argument("-u",
                        "--dont-balance-data",
                        help="Whether or not to balance data",
                        action="store_true",
                        default=False,
                        dest="dont_balance")

    parser.add_argument("--text-objects",
                        help="Path to Pickle file to load in textObjects",
                        action="store",
                        type=str,
                        default=None,
                        dest="text_objects")

    parser.add_argument("--text-object-type",
                        help="Type of text object to create.",
                        choices=['discord_message', 'book'],
                        type=str,
                        default='book',
                        dest="text_object_type")

    return parser

