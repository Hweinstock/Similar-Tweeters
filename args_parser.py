import argparse


def prepare_args():

    parser = argparse.ArgumentParser()
    run_group = parser.add_argument_group()

    run_group.add_argument("-l",
                           "--load-from-save",
                           help="Whether or not to load model from save or train a fresh one",
                           action="store",
                           type=str,
                           dest="load_from_save",
                           default=None)

    run_group.add_argument("-s",
                           "--save-model",
                           help="Whether or not to save model after running",
                           action="store_true",
                           dest="save_model",
                           default=False)

